#
# inventory_use.rpy
# Unscripted
#
# Created by Marquis Kurt on 11/15/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen inventory_use():
    zorder 100
    modal False

    add get_feather_icon("box", mode="light") at icon_flash:
        size (38, 38)
        xalign 0.95
        yalign 0.05
        xoffset 1
        yoffset 2
        alpha 0.25

    add get_feather_icon("box", mode="dark") at icon_flash:
        size (36, 36)
        xalign 0.95
        yalign 0.05

transform icon_flash:
    block:
        linear 2.0 alpha 1.0
        linear 2.0 alpha 0.0
        repeat
