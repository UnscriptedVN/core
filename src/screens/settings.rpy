#
# settings.rpy
# Unscripted
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

screen preferences():
    tag menu

    use game_menu(_("Settings"), scroll="viewport"):
        default settings_page = "general"
        vbox:
            xfill True

            hbox:
                style_prefix "pref_tab_group"
                xalign 0.5
                textbutton _("General") action SetScreenVariable("settings_page", "general")
                textbutton _("Sound") action SetScreenVariable("settings_page", "sound")
                textbutton _("Minigame") action SetScreenVariable("settings_page", "minigame")
                textbutton _("Accessibility") action SetScreenVariable("settings_page", "accessibility")
                textbutton _("Extras") action SetScreenVariable("settings_page", "extras")

            null height (4 * gui.pref_spacing)

            if settings_page == "general":
                use general_settings()
            elif settings_page == "sound":
                use sound_settings()
            elif settings_page == "minigame":
                use minigame_settings()
            elif settings_page == "accessibility":
                use accessibility_settings()
            elif settings_page == "extras":
                use extras_settings()
            else:
                text "The Settings page you requested doesn't exist.":
                    style "pref_text"

screen general_settings():
    style_prefix "pref"
    hbox:
        box_wrap True

        if renpy.variant("pc"):
            vbox:
                style_prefix "radio"
                label _("Display view:")
                textbutton _("As a window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

        vbox:
            style_prefix "radio"
            label _("When rolling back: ")
            textbutton _("Don't roll back") action Preference("rollback side", "disable")
            textbutton _("Roll to the left") action Preference("rollback side", "left")
            textbutton _("Roll to the right") action Preference("rollback side", "right")

        vbox:
            style_prefix "check"
            label _("When skipping, skip:")
            textbutton _("Unseen text") action Preference("skip", "toggle")
            textbutton _("After choices") action Preference("after choices", "toggle")
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

        vbox:
            style_prefix "slider"
            label "Automatic play"
            text "Automatic play allows you to play the game without needing to control it.":
                style "pref_text"

            label _("Text Speed")

            bar value Preference("text speed")

            $ cps = round(preferences.text_cps) or "max"
            text "About [cps] characters per second":
                style "pref_text"

            label _("Advance to the next line after:")

            bar value Preference("auto-forward time")

            $ afm_time = str(round(preferences.afm_time)) + " seconds" or "Don't auto-advance to the next line"
            text afm_time:
                style "pref_text"

        vbox:
            style_prefix "check"
            spacing 10
            vbox:
                textbutton _("Show save screenshots") action ToggleField(persistent, "use_detailed_saves")
                text "Show the screenshot from the moment of time in the save file instead of the chapter image.":
                    style "pref_text"
            vbox:
                textbutton _("Announce chapter names") action ToggleField(persistent, "announce_chapters")
                text "Show a toast with the chapter number and name when entering a new chapter.":
                    style "pref_text"

screen sound_settings():
    style_prefix "pref"
    hbox:
        style_prefix "slider"
        box_wrap True

        vbox:
            label "Sounds"

            if config.has_music:
                label _("Music Volume")

                hbox:
                    bar value Preference("music volume")

                $ music_vl = int(_preferences.get_volume('music') * 100)

                text "[music_vl]% volume":
                    style "pref_text"

            label _("Ambient Volume")

            hbox:
                bar value Preference("mixer ambient volume")

            $ ambient_vl = int(_preferences.get_volume('ambient') * 100)

            text "[ambient_vl]% volume":
                style "pref_text"

            if config.has_sound:

                label _("Sound Effects Volume")

                hbox:
                    bar value Preference("sound volume")

                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)
                $ sound_vl = int(_preferences.get_volume("sfx") * 100)
                text "[sound_vl]% volume":
                    style "pref_text"


            if config.has_voice:
                label _("Voice Volume")

                hbox:
                    bar value Preference("voice volume")

                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)


        vbox:
            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Mute all sounds and music"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"

                textbutton _("Emphasize sound effects"):
                    action Preference("emphasize audio", "toggle")
                    style "mute_all_button"
                text "When enabled, the music volume will be adjusted so\nyou can hear sound effects and ambience more clearly.":
                    style "pref_text"

screen accessibility_settings():
    style_prefix "pref"
    hbox:
        box_wrap True

        vbox:
            style_prefix "check"
            label "Self-Voicing"
            textbutton "Use self voicing" action Preference("self voicing", "toggle")
            text "Self-voicing will read out the current\nline and any interface elements.":
                style "pref_text"

        vbox:
            label "Readability" style "check_label"
            textbutton "Use Lexend font" action gui.TogglePreference("text_font", "gui/font/lexend/" + lexend_font_name(persistent.lexend_width) + "-Regular.ttf", AS_FONTS_DIR + "Medium.ttf") style "check_button"
            text "Using Lexend may improve readability. Adjusting the width will require for this setting to be turned on again.":
                style "pref_text"

            label "Lexend Font Width" style "check_label"
            bar value FieldValue(persistent, "lexend_width", 6, max_is_zero=False, style="slider_slider", offset=1, step=1, action=None)

            $ lexend_font_width = lexend_font_name(persistent.lexend_width)
            text "Font width: [lexend_font_width]":
                style "pref_text"

    null height 76

    text "This is a preview of the font choice for the game.":
        style "pref_access_preview"
        xalign 0.5

screen minigame_settings():
    style_prefix "pref"

    hbox:
        box_wrap True
        spacing 10

        if uconf["features"]["enable_minigame_adv_mode"]:
            vbox:
                spacing 10
                vbox:
                    label "Game Mode"
                    vbox:
                        style_prefix "radio"
                        textbutton "Basic mode" action SetField(persistent, "mg_adv_mode", False)
                        text "Basic mode uses a GUI with buttons to solve puzzles. The GUI compiles the NadiaVM code for you.":
                            style "pref_text"
                        textbutton "Advanced mode" action SetField(persistent, "mg_adv_mode", True)
                        text "Advanced mode lets you write code to solve puzzles, either using the {a=https://fira.marquiskurt.net}Fira API{/a} and Python or another tool and NadiaVM.":
                            style "pref_text"
                    null height 2
                    if persistent.mg_adv_mode:
                        add "assets/gui/previews/mg_advanced.png"
                    else:
                        add "assets/gui/previews/mg_basic.png"

        vbox:
            label "Preview Animation Speed"
            text "When showing the code running step-by-step, run at the provided speed."

            vbox:
                style_prefix "radio"
                textbutton "Normal (1x)" action SetField(persistent, "mg_speed", 1.0)
                textbutton "Faster (~1.5x)" action SetField(persistent, "mg_speed", 0.75)
                textbutton "Fastest (~2x)" action SetField(persistent, "mg_speed", 0.5)
                textbutton "Warp Speed (~10x)" action SetField(persistent, "mg_speed", 0.1)

        vbox:
            style_prefix "check"
            label "Basic Editor"
            vbox:
                spacing 10
                vbox:
                    textbutton "Reduce spacing in VM input" action ToggleField(persistent, "mg_condensed_font")
                    text "Enabling this option will reduce the spacing between commands in the VM preview pane in Basic Mode.":
                        style "pref_text"
                vbox:
                    textbutton "Show hidden VM commands" action ToggleField(persistent, "mg_vm_show_all")
                    text "Enabling this option will show all virtual machine commands in the VM preview pane.":
                        style "pref_text"

        vbox:
            label "Advanced"

            vbox:
                spacing 10
                vbox:
                    style_prefix "check"
                    textbutton "Force Python compiler" action ToggleField(persistent, "mg_vm_force_editor")
                    text "Show the editor preview and compile using Python, even if VM code exists.":
                        style "pref_text"
                vbox:
                    style_prefix "standard"
                    textbutton "Open Scripts Folder" action Function(open_directory, config.savedir + "/minigame")
                    text "Save directory: " + config.savedir + "/minigame":
                        style "pref_text"
                vbox:
                    style_prefix "standard"
                    textbutton "Documentation" action Function(open_api_docs)
                    text "Documentation is also available in Help.":
                        style "pref_text"

screen extras_settings():
    style_prefix "pref"
    hbox:
        box_wrap True
        spacing 8

        vbox:
            style_prefix "check"
            label "Rich Presence"

            python:
                import os
                def reset_game():
                   persistent._clear(progress=True)
                   renpy.utter_restart()

            if uconf["discord"]["enable_rpc"]:
                textbutton _("Enable Discord Presence") action ToggleField(persistent, "use_discord")
                text "When Discord is open and rich presence is enabled, Unscripted will connect and display information when playing.\n\nChanges to this setting apply upon restarting.":
                    style "pref_text"

        vbox:
            style_prefix "standard"

            label "Advanced"
            textbutton "Manage app permissions" action Function(appManager.applicationWillLaunch)
            text "Clicking this button will open AliceOS's App Manager and let you manage permissions of apps in-game.":
                style "pref_text"

            null height 8

            textbutton "Open Logs" action Function(open_uvn_log)
            text "Clicking this button will open the Unscripted logs, which may be useful for troubleshooting.":
                style "pref_text"

style pref_tab_group is hbox
style pref_tab_group_button is gui_button
style pref_tab_group_button_text is gui_text

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_text is gui_text
style pref_access_preview is gui_text
style pref_vbox is vbox
style pref_hbox is hbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style standard_label is pref_label
style standard_label_text is pref_label_text
style standard_button is gui_button
style standard_button_text is gui_button_text
style standard_vbox is pref_vbox

style pref_tab_group is hbox:
    background Frame("gui/tab_group_frame.png", 16, 2, 16, 2, tile=False)

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2
    font AS_FONTS_DIR + "Medium.ttf"

style pref_label_text:
    font AS_FONTS_DIR + "Medium.ttf"
    size 20
    yalign 1.0

style pref_vbox:
    xsize 275

style pref_hbox:
    spacing gui.pref_button_spacing

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    color gui.interface_text_color
    hover_color gui.hover_color
    size 18

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    color gui.interface_text_color
    hover_color gui.hover_color
    size 18

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

style pref_text:
    size 14
    color "#999999"

style standard_button:
    properties gui.button_properties("quick_button")

style standard_button_text:
    properties gui.button_text_properties("quick_button")
    size 12

style standard_vbox:
    spacing gui.pref_button_spacing

style pref_access_preview is gui_text:
    font gui.preference("text_font")

style pref_tab_group_button is gui_button:
    background Frame("gui/button/tab_group_[prefix_]background.png", Borders(16, 4, 16, 4), tile=False)
    xpadding 24
    ypadding 20

style pref_tab_group_button_text is gui_button_text:
    color "#ffffff"
    selected_font AS_FONTS_DIR + "Medium.ttf"
    size 16
