#
# console.rpy
# Unscripted
#
# Created by Marquis Kurt on 07/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init -1000 python:
    def command(help=None):
        def wrap(f):
            f.help = help
            config.console_commands[f.__name__] = f
            return f

        return wrap

init 1000 python:
    @command(_("puzzle <int>: Call the specified level from the minigame."))
    def puzzle(l):
        call_puzzle(int(l.rest().split(" ")[0]))
