#
# logic.rpy
# Unscripted Core - Minigame (Logic)
#
# Created by Marquis Kurt on 04/06/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init 10 python:
    import os
    import logging
    from uvn_fira.core import CSNadiaVM, CSNadiaVMWriterBuilder, CSWorldConfigReader
    from store.CADeprecated import deprecated

    class MinigameLogicHandler(object):
        """The minigame puzzle logic component.

        This class is responsible for handling all of the inner components that will read and write
            VM files and call the preview scene to handle them.

        Class Attributes:
            level (int): The level's number.
            map (CSWorldConfigReader): The configuration for the level specified.
            vm_path (str): The path to the VM file to read/write from.
            writer (CSNadiaVMWriterBuilder): The VM writer builder for this level. Typically used
                in basic mode.
            vm: The virtual machine for this level.
        """
        def __init__(self, level):
            """Initialize the logic handler.

            The construction will handle generating the configuration and setting up both the VM
                and VM writer for this level. If the VM file for this level isn't found, the VM's
                instantiation is deferred until the VM writer compiles the file.

            Arguments:
                level (int): The level to create the logic handler from.
            """
            self.level = level
            self.map = CSWorldConfigReader("core/src/minigame/levels/level%s.toml" % (level),
                                           exists=renpy.loadable,
                                           load=renpy.file)
            path = [config.savedir,
                    "minigame",
                    "compiled",
                    "%s_lvl%s.nvm"
                        % ("adv" if persistent.mg_adv_mode else "bas",self.level)
                    ]
            self.vm_path = os.path.join(*path)
            self.writer = CSNadiaVMWriterBuilder(self.vm_path)

            if not persistent.mg_adv_mode:
                if not renpy.loadable(self.vm_path):
                    with open(self.vm_path, "w+") as filewrite:
                        filewrite.write("")

            if os.path.isfile(self.vm_path):
                self.vm = CSNadiaVM(path=self.vm_path,
                                    player_origin=self.map.data.to_grid().first("PLAYER"))
                logging.info("Loaded VM from %s.", self.vm_path)
            else:
                logging.warning("VM file for level %s will need to be compiled first.", self.level)

        @deprecated('2.1.0', reason="New advanced mode will be old interactive experience.")
        def _compile_advanced(self):
            """Run the advanced compiler editor."""
            renpy.call_screen("mg_editor", self.map, self.writer, self.level)
            code_stream = ""
            with open(os.path.join(config.savedir, "minigame")
                      + "/level%s.py" % (self.level), "r") as file_stream:
                          code_stream = file_stream.read()
            executable = compile(code_stream,
                                 os.path.join(config.savedir, "minigame") + "/level%s.py" % (self.level),
                                 "exec")

            try:
                exec executable in py_sandbox()
                logging.info("Compiled code to %s", self.vm_path)
            except Exception as e:
                logging.error("Error in advanced mode compilation: %s" % (e.message))
                renpy.call_screen("ASNotificationAlert", "Compile Error", e.message)
                return

            self.vm = CSNadiaVM(path=self.vm_path,
                                player_origin=self.map.data.to_grid().first("PLAYER"))
            logging.info("Loaded VM from %s.", self.vm_path)

        @deprecated('2.1.0', reason="No longer in use.")
        def _compile_basic(self):
            """Compile the basic compiler editor.

            In levels that contain coins, the writer will automatically add the respective alloc
                and push commands to instantiate the coins in the virtual machine.
            """
            renpy.call_screen("ASNotificationAlert",
                              "Classic Mode is unsupported.",
                              "The classic mode GUI may not be called anymore.")
            raise Exception("Classic mode is unsupported.")

        def _preview(self):
            """Run the preview scene with the current map and virtual machine.

            The preview scene will blindly read the virtual machine code and attempt to solve the
                puzzle. If the preview scene does not result in a solution, the preview scene will
                set mg_return_code to a non-zero value.

            If the VM has not been defined or loaded yet, mg_return_code will automatically return
                9001.
            """
            if "vm" not in self.__dict__:
                logging.error("The VM for level %s is not defined.", self.level)
                mg_return_code = 9001
            return renpy.call_in_new_context("mg_preview", self.vm, self.map)

        def run(self):
            """Run the editor and preview scene.

            If the "Force Python compiler" option is not turned on, the first iteration will skip
                the editor by making `show_editor` false. If the first iteration results in a bad
                solution, `show_editor` will be re-enabled and will run on subsequent runs.
            """
            self.vm = CSNadiaVM(path=self.vm_path,
                                player_origin=self.map.data.to_grid().first("PLAYER"),
                                is_interactive=True)
            renpy.call_in_new_context("mg_interactive_experience", self.vm, self.map)
