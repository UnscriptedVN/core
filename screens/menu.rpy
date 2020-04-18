#
# menu.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/9/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init -1 python:
    import webbrowser

    def open_yt_url():
        url = "https://1n.pm/" + ("5twP3" if uconf["features"]["channel"] == "beta" else "AsuXE")
        webbrowser.open(url)

# MARK: Main menu

screen main_menu():

    tag menu
    style_prefix "main_menu"

    if persistent.use_discord:
        timer 0.10 action Function(discord.update_presence, title="Idle", detail="Main Menu")

    add gui.main_menu_background
    add "#0000001A"

    frame:
        pass

    vbox:
        xalign 0.5
        yalign 0.15

        hbox:
            add "gui/icon.png":
                size (96, 96)
            vbox:
                text "Unscripted":
                    style "main_menu_title"
                if uconf["demo"]["demo"]:
                    text "DEMO":
                        xalign 1.0
                        style "main_menu_version"
                elif uconf["features"]["channel"] == "beta":
                    text "BETA":
                        xalign 1.0
                        style "main_menu_version"

        null height 16

    vbox:
        xalign 0.025
        yalign 0.9
        xsize 300

        use navigation_button(icon="plus", title="Start Demo" if uconf["demo"]["demo"] else "Start Game", action=Start())
        use navigation_button(icon="folder", title="Load Game", action=ShowMenu('load'))
        if uconf["features"]["enable_dreams"]:
            use navigation_button(icon="moon", title="Dreams", action=ShowMenu('dreams'))
        use navigation_button(icon="settings", title="Settings", action=ShowMenu('preferences'))
        use navigation_button(icon="help-circle", title="Help", action=ShowMenu('help'))
        use navigation_button(icon="x", title="Quit Game", action=Quit(confirm=False))

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_test_box:
    background "#00ff00"

style main_menu_frame:
#     xsize 280
#     yfill True
#
    background None

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    xalign 0.0

style main_menu_title:
    properties gui.text_properties("title")
    font "gui/font/lexend/Deca-Regular.ttf"
    size 76
    color "#f4f4f4"
    text_align 0.5
    xalign 0.5

style main_menu_version:
    properties gui.text_properties("version")
    size 18
    color "#E5E4E2"
    outlines [(0.5, "#333333")]
    text_align 0.5
    xalign 0.5

style main_menu_save_button_text:
    properties gui.text_properties("version")
    size 14
    color "#f4f4f4"
    hover_color "#999"


screen navigation_button(icon=None, title="", subtitle=None, action):
    tag nav_button
    style_prefix "nav_button"

    vbox:
        xalign 0.0
        xfill True

        button action action:
            xfill True
            style "nav_button_base"
            hbox:
                spacing 6
                null width 4
                if icon:
                    add get_feather_icon(icon):
                        size (24, 24)
                        yalign 0.5
                vbox:
                    xalign 0
                    if subtitle:
                        yalign 0
                    else:
                        yalign 0.5
                    label title:
                        if not subtitle:
                            style "nav_button_title_large"
                        else:
                            style "nav_button_title"
                    if subtitle:
                        text subtitle:
                            style "nav_button_subtitle"
                null width 4

style nav_button_base:
    hover_background "#21212199"
    ypadding 6

style nav_button_title_large is gui_text

style nav_button_title_large_text is gui_text:
    properties gui.text_properties("version")
    color "#f4f4f4"
    outlines [(1, "#21212199")]
    size 24

style nav_button_title_text is gui_text:
    properties gui.text_properties("version")
    color "#f4f4f4"
    bold True
    size 16

style nav_button_subtitle is gui_text:
    properties gui.text_properties("version")
    color "#f4f4f4"
    size 11
