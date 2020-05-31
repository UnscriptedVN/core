#
# terminal.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/15/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

image terminal_background:
    "#06071DFA"
    top
    alpha 0.8
    size (600, 200)

style terminal_text:
    font "core/assets/fonts/jb_mono/BrainsMono-Regular.ttf"
    size 15
    color "#E0E0E0"
    outlines []

style terminal_input is terminal_text:
    slow_cps 35

screen terminal(i="", o=""):
    tag terminal
    zorder 100
    modal False
    style_prefix "ASInterface"

    frame:
        xpos 16
        ypos 16
        xalign 0.0
        yalign 0.0
        xsize 550
        ysize 250

        has vbox:
            xalign 0.0
            box_wrap True

            use ASInterfaceTitlebar("Hostless - Commander", onClose=NullAction())

            text "> " + i:
                style "terminal_input"
            text o:
                style "terminal_text"
                at transform:
                    alpha 0.0
                    pause ((len(i) / 30) + 1)
                    alpha 1.0

    timer ((len(i) / 30) + 1) + 3 action Return(0)
