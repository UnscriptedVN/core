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

screen preferences(pre_tab="general"):
    tag menu

    use game_menu(_("Settings"), scroll="viewport"):
        default settings_page = pre_tab
        vbox:
            xfill True

            hbox:
                style_prefix "pref_tab_group"
                xalign 0.5
                textbutton _("General") action SetScreenVariable("settings_page", "general")
                textbutton _("Appearance") action SetScreenVariable("settings_page", "appearance")
                textbutton _("Sound") action SetScreenVariable("settings_page", "sound")
                textbutton _("Minigame") action SetScreenVariable("settings_page", "minigame")
                textbutton _("Accessibility") action SetScreenVariable("settings_page", "accessibility")
                textbutton _("Extras") action SetScreenVariable("settings_page", "extras")

            null height (4 * gui.pref_spacing)

            use expression settings_page + "_settings"

screen general_settings():
    style_prefix "pref"
    hbox:
        box_wrap True

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

            $ cps = round(preferences.text_cps) or "∞"
            text "About [cps] characters per second":
                style "pref_text"

            label _("Advance to the next line after:")

            bar value Preference("auto-forward time")

            $ afm_time = str(round(preferences.afm_time)) + " seconds" or "Don't auto-advance to the next line"
            text afm_time:
                style "pref_text"

screen appearance_settings():
    style_prefix "pref"
    hbox:
        box_wrap True

        vbox:
            style_prefix "radio"
            label "Theme"
            # textbutton "Ring" action gui.SetPreference("theme", "ring")
            textbutton "Ayu Light Blue" action gui.SetPreference("theme", "ruby-light")
            textbutton "Ayu Mirage Blue" action gui.SetPreference("theme", "ruby-mirage")
            textbutton "Ayu Dark Blue" action gui.SetPreference("theme", "ruby-dark")

        vbox:
            if renpy.variant("pc"):
                vbox:
                    style_prefix "radio"
                    label _("Display view:")
                    textbutton _("As a window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                spacing 10
                vbox:
                    label "Save screenshots"
                    textbutton _("Show save screenshots") action ToggleField(persistent, "use_detailed_saves")
                    text "Show the screenshot from the moment of time in the save file instead of the chapter image.":
                        style "pref_text"

        vbox:
            spacing 10

            vbox:
                style_prefix "radio"

                label "Dialogue font"

                textbutton "Inter (default)" action gui.SetPreference("text_font", AS_FONTS_DIR + "Medium.ttf")
                textbutton "Merriweather" action gui.SetPreference("text_font", "core/assets/fonts/merriweather/Merriweather-Regular.ttf"):
                    style "pref_font_mwthr"
                textbutton "JetBrains Mono" action gui.SetPreference("text_font", "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"):
                    style "pref_font_mono"
                textbutton "OpenDyslexic" action gui.SetPreference("text_font", "core/assets/fonts/opendys/OpenDyslexic-Regular.otf"):
                    style "pref_font_opendys"
                textbutton "Lexend..." action SetScreenVariable("settings_page", "lexend"):
                    selected "lexend" in gui.text_font
                    style "pref_font_deca"

                text "The font selected will be used in the textbox when a character is speaking. This does not affect the user interface fonts.":
                    style "pref_text"

        vbox:
            style_prefix "radio"
            label "Dialogue font size"

            textbutton "Small" action gui.SetPreference("text_size", 18)
            textbutton "Medium (default)" action gui.SetPreference("text_size", 20)
            textbutton "Large" action gui.SetPreference("text_size", 22)

            text "For some fonts, changing the text size to larger sizes may cut off dialogue.":
                style "pref_text"

screen lexend_settings():
    style_prefix "pref"

    textbutton "‹ Appearance" action SetScreenVariable("settings_page", "appearance"):
        style "pref_navigation_button"

    label "Lexend Font"
    text "Lexend is a font with multiple widths. Select the width you want to use below.":
        style "pref_text"

    vbox:
        style_prefix "radio"

        textbutton "Lexend Deca" action gui.SetPreference("text_font", "core/assets/fonts/lexend/Deca-Regular.ttf"):
            style "pref_font_deca"
        textbutton "Lexend Exa" action gui.SetPreference("text_font", "core/assets/fonts/lexend/Exa-Regular.ttf"):
            style "pref_font_exa"
        textbutton "Lexend Giga" action gui.SetPreference("text_font", "core/assets/fonts/lexend/Giga-Regular.ttf"):
            style "pref_font_giga"
        textbutton "Lexend Mega" action gui.SetPreference("text_font", "core/assets/fonts/lexend/Mega-Regular.ttf"):
            style "pref_font_mega"
        textbutton "Lexend Peta" action gui.SetPreference("text_font", "core/assets/fonts/lexend/Peta-Regular.ttf"):
            style "pref_font_peta"
        textbutton "Lexend Tera" action gui.SetPreference("text_font", "core/assets/fonts/lexend/Tera-Regular.ttf"):
            style "pref_font_tera"
        textbutton "Lexend Zetta" action gui.SetPreference("text_font", "core/assets/fonts/lexend/Zetta-Regular.ttf"):
            style "pref_font_zetta"


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
            style_prefix "check"
            spacing 10
            vbox:
                label "Chapter names"
                textbutton _("Announce chapter names") action ToggleField(persistent, "announce_chapters")
                text "Show a toast with the chapter number and name when entering a new chapter.":
                    style "pref_text"

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
                        if "mg-classic-mode" in arguments:
                            text "Basic mode uses a GUI with buttons to solve puzzles. The GUI compiles the NadiaVM code for you.":
                                style "pref_text"
                        else:
                            text "Basic mode lets you type NadiaVM commands into an interpreter to solve puzzles. No code is compiled and happens in real time.":
                                style "pref_text"
                        textbutton "Advanced mode" action SetField(persistent, "mg_adv_mode", True)
                        text "Advanced mode lets you write code to solve puzzles, either using the {a=https://fira.marquiskurt.net}Fira API{/a} and Python or another tool and NadiaVM.":
                            style "pref_text"
                    null height 2
                    if persistent.mg_adv_mode:
                        add "core/assets/interface/previews/mg_advanced.png"
                    elif "mg-classic-mode" in arguments:
                        add "core/assets/interface/previews/mg_classic.png"
                    else:
                        add "core/assets/interface/previews/mg_basic.png"

        vbox:
            label "Preview Animation Speed"
            text "When showing the code running step-by-step, run at the provided speed."

            vbox:
                style_prefix "radio"
                textbutton "Normal (1x)" action SetField(persistent, "mg_speed", 1.0)
                textbutton "Faster (~1.5x)" action SetField(persistent, "mg_speed", 0.75)
                textbutton "Fastest (~2x)" action SetField(persistent, "mg_speed", 0.5)
                textbutton "Warp Speed (~10x)" action SetField(persistent, "mg_speed", 0.1)

        if "mg-classic-mode" in arguments:
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
        else:
            vbox:
                null height 8

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

style pref_navigation_button is gui_button
style pref_navigation_button_text is gui_button_text

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

style pref_navigation_button_text:
    font AS_FONTS_DIR + "Medium.ttf"
    idle_color current_theme().colors().INTERFACE.value
    size 20

style pref_font_mwthr is radio_button
style pref_font_mwthr_text is radio_button_text:
    font "core/assets/fonts/merriweather/Merriweather-Regular.ttf"

style pref_font_mono is radio_button
style pref_font_mono_text is radio_button_text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"

style pref_font_opendys is radio_button
style pref_font_opendys_text is radio_button_text:
    font "core/assets/fonts/opendys/OpenDyslexic-Regular.otf"

style pref_font_deca is radio_button
style pref_font_deca_text is radio_button_text:
    font "core/assets/fonts/lexend/Deca-Regular.ttf"

style pref_font_exa is radio_button
style pref_font_exa_text is radio_button_text:
    font "core/assets/fonts/lexend/Exa-Regular.ttf"

style pref_font_giga is radio_button
style pref_font_giga_text is radio_button_text:
    font "core/assets/fonts/lexend/Giga-Regular.ttf"

style pref_font_mega is radio_button
style pref_font_mega_text is radio_button_text:
    font "core/assets/fonts/lexend/Mega-Regular.ttf"

style pref_font_peta is radio_button
style pref_font_peta_text is radio_button_text:
    font "core/assets/fonts/lexend/Peta-Regular.ttf"

style pref_font_tera is radio_button
style pref_font_tera_text is radio_button_text:
    font "core/assets/fonts/lexend/Tera-Regular.ttf"

style pref_font_zetta is radio_button
style pref_font_zetta_text is radio_button_text:
    font "core/assets/fonts/lexend/Zetta-Regular.ttf"

style check_vbox:
    spacing gui.pref_button_spacing

style slider_vbox:
    xsize 450

style pref_text:
    size 14
    color current_theme().colors().INTERFACE_SECONDARY.value

style standard_vbox:
    spacing gui.pref_button_spacing

style pref_access_preview is gui_text:
    font gui.preference("text_font")

style pref_tab_group_button is tab_group_button
style pref_tab_group_button_text is tab_group_button_text
