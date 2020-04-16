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
    from uvn_fira.core import CSNadiaVM, CSNadiaVMWriterBuilder, CSWorldConfigReader

    class MinigameLogicHandler(object):
        def __init__(self, level):
            self.level = level
            self.map = CSWorldConfigReader("core/minigame/levels/level%s.toml" % (level),
                                           exists=renpy.loadable,
                                           load=renpy.file)
            self.writer = CSNadiaVMWriterBuilder(os.path.join(config.savedir, "minigame/compiled/")
                                                              + ("lvl%s.nvm" % (level)))

            if renpy.loadable(config.savedir + "/minigame/compiled/lvl%s.nvm" % (level)):
                self.vm = CSNadiaVM(os.path.join(config.savedir, "minigame/compiled/")
                    + ("lvl%s.nvm" % (level)),
                    self.map.data.to_grid().first("PLAYER"))

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
            except Exception as e:
                print(e)
                renpy.call_screen("ASNotificationAlert", "Compile Error", e.message)
                return

            self.vm = CSNadiaVM(os.path.join(config.savedir, "minigame/compiled/")
                    + ("lvl%s.nvm" % (self.level)),
                    self.map.data.to_grid().first("PLAYER"))

        def _compile_basic(self):
            if self.writer.instructions:
                self.writer.clear()

            coins = self.map.data.coins().as_list()

            if len(coins) > 0:
                self.writer.alloc("world_coins", len(coins))
                self.writer.alloc("inventory", len(coins))

                for coin in coins:
                    self.writer.set(coin)
                    self.writer.push("World.coins", coins.index(coin))

            renpy.call_screen("mg_editor", self.map, self.writer, self.level)

            self.vm = CSNadiaVM(os.path.join(config.savedir, "minigame/compiled/")
                    + ("lvl%s.nvm" % (self.level)),
                    self.map.data.to_grid().first("PLAYER"))

        def _preview(self):
            return renpy.call_in_new_context("mg_preview", self.vm, self.map)

        def run(self):
            solved = False
            while not solved:
                if persistent.mg_adv_mode:
                    self._compile_advanced()
                else:
                    self._compile_basic()

                if "vm" in self.__dict__:
                    self._preview()

                    if mg_return_code != 0:
                        renpy.call_screen("ASNotificationAlert",
                                        "Uh oh!",
                                        "It looks like you didn't reach the goal. Try again!")
                    else:
                        solved = True