#
# navbar.rpy
# Unscripted Core - Screens (Navbar)
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

screen navigation():

    hbox:
        style_prefix "navigation"
        xfill True
        ypos 12

        hbox:
            xpos 24
            spacing 8

            button action Return():
                style "navigation_icon_button"
                add get_feather_icon("arrow-left"):
                    size (28, 28)

            if main_menu:
                textbutton _("Start") action Start()

            else:
                textbutton _("Chat History") action ShowMenu("history")
                textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")

            if main_menu:
                if uconf["features"]["enable_dreams"]:
                    textbutton _("Dreams") action ShowMenu("dreams")

            textbutton _("Settings") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)
            if renpy.variant("pc"):
                textbutton _("Help") action ShowMenu("help")

        hbox:
            xalign 1.0
            xoffset -24
            spacing 8

            if uconf["analytics"]["enable_bug_reports"]:
                button action Confirm("You are about to open the bug reporter\nin your web browser, which may collect data.\n\nAre you sure you want to continue?", yes=Function(open_issues_url)):
                    style "navigation_icon_button"
                    add get_feather_icon("message-square"):
                        size (28, 28)

            if not main_menu:
                button action MainMenu():
                    style "navigation_icon_button"
                    add get_feather_icon("log-out"):
                        size (28, 28)

            button action Quit(confirm=not main_menu):
                style "navigation_icon_button"
                add get_feather_icon("power"):
                    size (28, 28)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    # size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font AS_FONTS_DIR + "medium.ttf"
    color "#ffffff"
    hover_color "#05C1FD"
    size 16
    text_align 0.0

style navigation_icon_button is gui_button:
    hover_background gui.accent_color + "20"
