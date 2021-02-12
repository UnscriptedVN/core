#
# appearance.rpy
# Unscripted Core - Settings UI
#
# Created by Marquis Kurt on 11/25/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

screen appearance_settings():
    style_prefix "pref"
    hbox:
        box_wrap True

        vbox:
            vbox:
                style_prefix "radio"
                label "Theme"
                # textbutton "Ring" action gui.SetPreference("theme", "ring")
                textbutton "Ayu Light Blue" action gui.SetPreference("theme", "ruby-light")
                textbutton "Ayu Mirage Blue" action gui.SetPreference("theme", "ruby-mirage")
                textbutton "Ayu Dark Blue" action gui.SetPreference("theme", "ruby-dark")
            vbox:
                style_prefix "check"
                label "Main menu"
                textbutton "Use dynamic backgrounds" action ToggleField(persistent, "prefers_dynamic_bg")
                text "When dynamic backgrounds are enabled, the main menu background will change depending on the time of day in your location.":
                    style "pref_text"


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

                textbutton "Inter (default)" action gui.SetPreference("text_font", get_font("Interface", variant="Medium"))
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


# MARK: - LEXEND
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
