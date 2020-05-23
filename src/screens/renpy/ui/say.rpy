#
# say.rpy
# Unscripted Core - Screens (Say)
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

screen say(who, what):
    style_prefix "say"

    window:
        id "window"


        if who is not None:

            window:
                style "namebox"
                hbox:
                    spacing 8
                    add "gui/history/" + get_history_name(who) + ".png":
                        size (24, 24)
                        xalign 0.0

                    text who id "who"

        text what id "what"

    if quick_menu:
        use quick_menu

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0, yoffset=4)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=False)
    xalign gui.name_xalign
    yalign 0.5
    color gui.text_color
    size 20

style say_dialogue is normal
