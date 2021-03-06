#
# ProfileNameView.rpy
# Unscripted
#
# Created by Marquis Kurt on 9/27/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen ProfileNameView():
    style_prefix "ProfileNameView"
    modal True
    zorder 105

    default player_name = "MC"
    default identify = "male"
    default language = "Python"
    default candella_profile = True

    if config.gl2:
        add dynamic_background("assets/gui/main/main.jpg", include=[TimeOfDay.day, TimeOfDay.night]):
            blur CABlurType["default"]

        add "#000000BB"

    vbox at main_menu_enter:
        xalign 0.5
        yalign 0.5
        # spacing 8
        xmaximum 1000
        ymaximum 550

        hbox:
            spacing 8

            add get_feather_icon("git-merge", mode="dark") size (128, 128)

            vbox:
                spacing 8
                yfit True
                ymaximum 976

                vbox:
                    spacing 8

                    label "Welcome to RepoHive"
                    text "Let's create your profile to make the experience unique to you."

                hbox:
                    spacing 10
                    hbox:
                        spacing 10
                        xmaximum 512

                        text "Name"
                        vbox:
                            xfill True
                            input default "" value ScreenVariableInputValue("player_name"):
                                length 16
                                allow "ABCDEFGHIJKLMNOPQRSTUVXWYZabcedfghijklmnopqurstuvwxyz ._"
                            text "Acceptable characters include alphanumeric characters, underscores, spaces, and periods.":
                                style "ProfileNameView_info_text"
                    vbox:
                        text "Personal Pronouns"
                        vbox:
                            style_prefix "radio"

                            textbutton "He/Him/His" action SetScreenVariable("identify", "male")
                            textbutton "She/Her/Hers" action SetScreenVariable("identify", "female")
                            textbutton "They/Them/Their" action SetScreenVariable("identify", "they")
                vbox:
                    vbox:
                        style_prefix "check"
                        null height 8
                        textbutton "Integrate with Candella" action ToggleScreenVariable("candella_profile")
                    text "Integrating with Candella will let you use a custom profile with your name, which lets you have custom settings such as the apps list and desktop wallpaper. You can switch user profiles by clicking on your name on the desktop.":
                        style "ProfileNameView_info_text"
                vbox:
                    text "Programming language"
                    text "New projects on RepoHive will set the language to the language specified here.":
                        style "ProfileNameView_info_text"

                    null height 8

                    vbox:
                        style_prefix "radio"

                        textbutton "Swift" action SetScreenVariable("language", "Swift")
                        textbutton "Python" action SetScreenVariable("language", "Python")
                        textbutton "C++" action SetScreenVariable("language", "C++")
                        textbutton "Kotlin" action SetScreenVariable("language", "Kotlin")

                null height 32

                vbox:
                    yalign 1.0
                    xalign 1.0

                    hbox:
                        xalign 1.0
                        yalign 1.0
                        style_prefix "standard"

                        textbutton "Back" action MainMenu()
                        textbutton "Start" action [Return((player_name or "MC", identify, language, candella_profile))]

style ProfileNameView_label is gui_label
style ProfileNameView_label_text is gui_label_text:
    font get_font("Interface", variant="Medium")
    color "#f4f4f4"
    size 28

style ProfileNameView_text is gui_text:
    font get_font("Interface")
    color "#999999"
    size 18

style ProfileNameView_info_text is gui_text:
    size 16
    color "#888888"
