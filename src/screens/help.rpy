#
# help.rpy
# Unscripted Core - Screens (Help)
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#

init offset = -1

init -1 python:
    import toml
    import logging

    glossary = {}
    if renpy.loadable("core/glossary.toml"):
        with renpy.file("core/glossary.toml") as gloss:
            glossary = toml.load(gloss)["game"]["dictionary"]
        logging.info("Glossary from glossary file updated.")
    else:
        logging.warn("Glossary file couldn't be loaded.")

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
                if uconf["features"]["enable_minigame_adv_mode"]:
                    textbutton _("Documentation") action Function(open_api_docs)
                if "enable-glossary" in uconf["labs"]["current"]:
                    textbutton _("Glossary") action SetScreenVariable("tab", "glossary")
                textbutton _("Keyboard") action SetScreenVariable("tab", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("tab", "mouse")
                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("tab", "gamepad")

            use expression tab + "_help"

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
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "D"
        text _("Opens the AliceOS Desktop.")

    hbox:
        label "E"
        text _("Opens the inventory HUD.")

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

screen glossary_help():
    for word in sorted(glossary):
        python:
            wd = word.replace("_", " ")
            definition = glossary[word]
        hbox:
            label "[wd!cl]"
            text "[definition]"

screen license_help():
    default license = ""

    python:
        with renpy.file("../LICENSE.txt") as file:
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
            font "gui/font/lexend/Deca-Regular.ttf"
            size 64
    text "A visual novel about software development":
        xalign 0.5
        text_align 0.5
    null height 16
    hbox:
        label "Game Version"
        text "[config.version]"
    hbox:
        $ _cv = uconf["features"]["channel"]
        label "Release Channel"
        text "[_cv!c] %s"  % ("(demo)" if uconf["demo"]["demo"] else "")
    hbox:
        python:
            import uvn_fira
            _fv = uvn_fira.__version__
        label "Fira API Version"
        text "[_fv]"
    hbox:
        label "AliceOS Version"
        text "[AS_SYS_INFO[COMMON_NAME]] ([AS_SYS_INFO[VERSION]]) [AS_SYS_INFO[BUILD_ID]]"
    hbox:
        $ _rv = renpy.version().replace("Ren'Py", "")
        label "Ren'Py Version"
        text "[_rv]"

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
    font AS_FONTS_DIR + "Bold.ttf"

style help_text is gui_text:
    size gui.text_size

style help_license_text is help_text:
    font "gui/font/JetBrainsMono-Regular.ttf"
    size 16

style help_small_text is help_text:
    size 16
    color "#666666"

style help_vbox is gui_vbox:
    xfill True
