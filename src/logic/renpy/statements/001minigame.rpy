#
# 001minigame.rpy
# Unscripted
#
# Created by Marquis Kurt on 11/14/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

python early:

    def _parse_mg_statement(lex):
        puzzle_id = lex.integer()
        return puzzle_id

    def _empty_lint(lex):
        pass

    def _execute_mg_statement(o):
        call_puzzle(int(o))

    renpy.register_statement(
        "puzzle",
        parse=_parse_mg_statement,
        lint=_empty_lint,
        execute=_execute_mg_statement
    )
