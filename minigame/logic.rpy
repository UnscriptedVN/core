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

    class MinigameLogicHandler(object):
        def __init__(self, level):
            self.level = level
            self.map = CSWorldConfigReader("core/minigame/levels/level%s.toml" % (level),
                                           exists=renpy.loadable,
                                           load=renpy.file)

            path = [config.savedir,
                    "minigame",
                    "compiled",
                    "%s_lvl%s.nvm"
                        % ("adv" if persistent.mg_adv_mode else "base",self.level)
                    ]
            self.vm_path = os.path.join(path)

            self.writer = CSNadiaVMWriterBuilder(self.vm_path)

            vm_files = os.listdir(os.path.join(config.savedir, "minigame", "compiled"))
            fn_name = os.path.basename(self.vm_path)
            if fn_name in vm_files:
                self.vm = CSNadiaVM(self.vm_path, self.map.data.to_grid().first("PLAYER"))
            else:
                logging.warning("VM file for level %s will need to be compiled first.", self.level)

        def _compile_advanced(self):
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

            self.vm = CSNadiaVM(self.vm_path, self.map.data.to_grid().first("PLAYER"))

        def _compile_basic(self):
            if self.writer.instructions:
                self.writer.clear()

            coins = self.map.data.coins().as_list()

            if len(coins) > 0:
                self.writer.alloc("world_coins", len(coins))
                self.writer.alloc("inventory", len(coins))

                for coin in coins:
                    self.writer.set(coin)
                    self.writer.push("world_coins", coins.index(coin))

            renpy.call_screen("mg_editor", self.map, self.writer, self.level)

            self.vm = CSNadiaVM(self.vm_path, self.map.data.to_grid().first("PLAYER"))

        def _preview(self):
            return renpy.call_in_new_context("mg_preview", self.vm, self.map)

        def run(self):
            solved = False
            run_editor = True

            if not persistent.mg_vm_force_editor:
                vm_files = os.listdir(os.path.join(config.savedir, "minigame", "compiled"))
                fn_name = os.path.basename(self.vm_path)
                if fn_name not in vm_files:
                    logging.warning("Cannot load requested VM file. Calling editor...")
                else:
                    run_editor = False
                    logging.info("Reading from existing VM code at %s", self.vm_path)

            while not solved:
                if run_editor:
                    if persistent.mg_adv_mode:
                        self._compile_advanced()
                    else:
                        self._compile_basic()

                if "vm" in self.__dict__:
                    logging.info("Starting preview...")
                    self._preview()

                    if mg_return_code != 0:
                        renpy.call_screen("ASNotificationAlert",
                                        "Uh oh!",
                                        "It looks like you didn't reach the goal. Try again!")
                    else:
                        solved = True
                        logging.info("Minigame level succeeded.")
