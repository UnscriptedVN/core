#
# main.rpy
# Unscripted Core - Screens (Game Menu)
#
# Created by Marquis Kurt on 07/01/19.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

screen game_menu(title, scroll=None):

    style_prefix "game_menu"
    add current_theme().overlays().GAME.value

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    label title

    frame:
        yalign 1.0
        padding (16, 16)
        style "pref_footer"
        has hbox:
            xfill True

            hbox:
                spacing -8
                add "assets/gui/icon.png":
                    size (32, 32)

                $ _channel = uconf["info"]["channel"]
                text "[config.name!t] v[config.version]. Release channel: [_channel]\n© 2020 Marquis Kurt. All rights reserved."

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_text is gui_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

style game_menu_content_frame:
    left_margin 16
    right_margin 16
    top_padding 24
    bottom_padding 8
    left_padding 8
    right_padding 8
    xfill True

style game_menu_viewport:
    xsize 1216
    xoffset 16

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 32
    ypos 80

style game_menu_text:
    xpos 32
    yalign 0.975
    size 12
    color current_theme().colors().INTERFACE_SECONDARY.value

style game_menu_label_text:
    font get_font("Interface", variant="Bold")
    color current_theme().colors().INTERFACE.value
    yalign 0.5
    size 32

style pref_footer is gui_frame:
    margin (0, 0)
    padding (0, 8)
    background current_theme().colors().BACKGROUND.value + "DE"
