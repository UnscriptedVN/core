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
    background "#212121"
    margin (0, 0)
    padding (16, 16)

style mg_editor_frame_vbox is gui_vbox

style mg_editor_toolbar is gui_hbox:
    background "#000000"
    spacing 8
    xfill True

style mg_editor_toolbar_buttons_hbox is gui_hbox:
    xalign 1.0
    spacing 4
    yoffset 4

style mg_editor_toolbar_buttons_button is ASInterfacePushButton
style mg_editor_toolbar_buttons_button_text is ASInterfacePushButton_text

style mg_editor_main_view_hbox is gui_hbox:
    xfill True

style mg_editor_main_view_vbox is gui_vbox:
    xmaximum 616

style mg_editor_programmable_buttons_hbox is gui_hbox:
    spacing 4
    xfill True

style mg_editor_programmable_buttons_button is gui_button:
    hover_foreground Frame(MG_CONFIG["assets_path"] + "gui/button_hover_overlay.png", MG_CONFIG["button_size"], MG_CONFIG["button_size"], tile=False)
    xysize (MG_CONFIG["button_size"] + 8, MG_CONFIG["button_size"] + 8)
    padding (0, 0)
    margin (0, 0)

style mg_vm_input is gui_frame:
    xsize 584
    margin (0, 0)
    padding (16, 16)
    background "#191919"

style mg_vm_viewport is ASInterfaceScrollbar
style mg_vm_viewport_vscrollbar is ASInterfaceScrollbar_vscrollbar

style mg_vm_viewport_vbox is gui_vbox:
    spacing 4

style mg_vm_viewport_text is gui_text:
    font "gui/font/JetBrainsMono-Regular.ttf"
    size 20

