#
# confirm.rpy
# Unscripted Core - Screens (Confirm)
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add current_theme().overlays().CONFIRM.value

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([current_theme().frames().BASIC.value], Borders(0, 0, 0, 0), tile=gui.frame_tile)
    xalign .5
    yalign .5
    padding (24, 24)

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    size 20
    font AS_FONTS_DIR + "Medium.ttf"

style confirm_button:
    properties gui.button_properties("confirm_button")
    background Frame(current_theme().buttons(), gui.confirm_button_borders, tile=gui.button_tile)

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    size 16
    font AS_FONTS_DIR + "Medium.ttf"
