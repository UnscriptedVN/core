#
# editor.css.rpy
# Unscripted Core - Minigame (Editor, Styles)
#
# Created by Marquis Kurt on 04/06/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 10

style mg_editor_frame is gui_frame:
    background current_theme().colors().BACKGROUND.value
    margin (0, 0)
    padding (16, 16)

style mg_editor_frame_vbox is gui_vbox:
    spacing 0

style mg_editor_toolbar is gui_hbox:
    background "#000000"
    spacing 8
    xfill True

style mg_editor_toolbar_buttons_hbox is gui_hbox:
    xalign 1.0
    spacing 4
    yoffset 4

style mg_editor_toolbar_buttons_button is standard_button
style mg_editor_toolbar_buttons_button_text is standard_button_text

style mg_editor_main_view_hbox is gui_hbox:
    xfill True

style mg_editor_main_view_vbox is gui_vbox:
    xmaximum 616
    spacing 0
