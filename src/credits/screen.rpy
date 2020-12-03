#
# screen.rpy
# Unscripted Core - Credits (Screen)
#
# Created by Marquis Kurt on 04/14/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 10

screen credits(tokens=[]):
    tag credits
    zorder 100
    modal True
    layer "overlay"
    style_prefix "ce"

    default _token_list = tokens
    default _text_timer = 0
    default _current_row_count = 0

    key "game_menu" action NullAction()
    key "K_TAB" action NullAction()
    key "a" action NullAction()
    key "d" action NullAction()
    key "h" action NullAction()

    frame:
        has vbox:
            xfill True

            vbox:
                for row in tokens:
                    hbox:
                        spacing 1
                        for token in row:
                            python:
                                _ce_kind, _ce_name = token
                                if _ce_name == " {":
                                    _ce_name = " {{"
                                _text_timer += (len(_ce_name) / 60) + 0.5

                            text "%s" % (_ce_name):
                                style "ce_%s_text" % (_ce_kind)
                                at transform:
                                    alpha 0.0
                                    pause _text_timer
                                    linear 0.05 alpha 1.0


    timer _text_timer + 1.5 action Return()
