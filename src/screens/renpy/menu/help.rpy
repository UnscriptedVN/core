#
# help.rpy
# Unscripted Core - Screens (Help)
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

init -1 python:
    CONTRIBS = {
        "Andy Kurnia": "kofi",
        "Jim Kearney": "kofi",
        "Christine Kearney-Kurt": "kofi",
        "Suspicious Yak": "kofi"
    }

screen help(pre_tab="about"):
    tag menu

    default tab = pre_tab

    use game_menu(_("Help"), scroll="viewport"):
        style_prefix "help"

        vbox:
            spacing 15

            hbox:
                xalign 0.5
                style_prefix "pref_tab_group"

                textbutton _("About") action SetScreenVariable("tab", "about")
                textbutton _("License") action SetScreenVariable("tab", "license")
                textbutton _("Contributors") action SetScreenVariable("tab", "contributors")
                textbutton _("Keyboard") action SetScreenVariable("tab", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("tab", "mouse")
                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("tab", "gamepad")

            use expression tab + "_help"
            null height 128

screen contributors_help():
    text "Thanks to the following people that helped make Unscripted possible!":
        xalign 0.5
    null height 16

    for contributor in CONTRIBS:
        python:
            _i = "coffee" if CONTRIBS[contributor] == "kofi" else "github"
        hbox:
            hbox:
                xsize 250
                add get_feather_icon(_i):
                    size (24, 24)
                    xalign 1.0
                    xoffset -20
            text "[contributor]"

screen keyboard_help():
    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S/F12"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "D"
        text _("Opens the AliceOS Desktop.")

    hbox:
        label "E"
        text _("Opens the Inventory HUD.")

    hbox:
        label "L"
        text _("Opens the Unscripted log file.")

    hbox:
        label "Shift + B"
        text _("Opens the bug reporter.")

screen mouse_help():
    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    if config.developer:
        hbox:
            label _("Mouse Wheel Up\nClick Rollback Side")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Mouse Wheel Down")
            text _("Rolls forward to later dialogue.")


screen gamepad_help():
    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()

screen license_help():
    default license = ""

    python:
        with renpy.open_file("../LICENSE.txt", encoding="utf-8") as file:
            license = file.read()

    hbox:
        label "License"
        text "[license]":
            style "help_license_text"

screen about_help():
    hbox:
        xalign 0.5
        spacing 4
        add "gui/icon.png":
            size (64, 64)
        text "Unscripted":
            font "core/assets/fonts/lexend/Deca-Regular.ttf"
            size 64
    text "A visual novel about software development":
        xalign 0.5
        text_align 0.5
    null height 16
    hbox:
        label "Game Version"
        text "[config.version]"
    hbox:
        $ _cv = uconf["info"]["channel"]
        label "Release Channel"
        text "[_cv!c] %s"  % ("(demo)" if uconf["demo"]["demo"] else "")
    hbox:
        python:
            import uvn_fira
            _fv = uvn_fira.__version__
        label "Fira API Version"
        text "[_fv]"
    hbox:
        label "Candella Version"
        text "[AS_SYS_INFO[VERSION]] ([AS_SYS_INFO[COMMON_NAME]], [AS_SYS_INFO[BUILD_ID]]) "
    hbox:
        $ _rv = renpy.version().replace("Ren'Py", "")
        label "Ren'Py Version"
        text "[_rv]"

    if uconf["info"]["channel"] != "stable":
        hbox:
            $ _gl2_enabled = config.gl2
            label "Model-based Render"
            text "[_gl2_enabled]"

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_vbox is gui_vbox

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
    font get_font("Interface", variant="Bold")

style help_text is gui_text:
    size gui.text_size
    color current_theme().colors().INTERFACE_SECONDARY.value

style help_license_text is help_text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"
    size 16

style help_small_text is help_text:
    size 16
    color "#666666"

style help_vbox is gui_vbox:
    xfill True
