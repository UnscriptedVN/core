#
# choice.rpy
# Unscripted Core - Screens (Choice)
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

default choice_timeout = None

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            if i.caption:
                textbutton i.caption action i.action

    if choice_timeout:
        timer choice_timeout action [Function(logging.warn, "Choice timed out. Selecting last choice automatically."),
                                     Return(len(items))]

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    background Frame(current_theme().buttons(), gui.choice_button_borders, tile=gui.button_tile)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
