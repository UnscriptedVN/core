#
# minigame.rpy
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

screen minigame_settings():
    style_prefix "pref"

    hbox:
        box_wrap True
        spacing 10

        vbox:
            spacing 10
            vbox:
                label "Minigame Mode"
                vbox:
                    style_prefix "radio"
                    textbutton "Basic mode" action SetField(persistent, "mg_adv_mode", False)
                    text "Basic mode lets you push a series of buttons to guide the player. No code is required.":
                        style "pref_text"

                    textbutton "Advanced mode" action SetField(persistent, "mg_adv_mode", True)
                    text "Basic mode lets you type NadiaVM commands into an interpreter to solve puzzles. Commands happen in real time without compilation.":
                        style "pref_text"
                null height 4
                if persistent.mg_adv_mode:
                    add "core/assets/interface/previews/mg_advanced.png"
                else:
                    add "core/assets/interface/previews/mg_basic.png"

        vbox:
            if uconf["features"]["enable_minigame_adv_mode"]:
                label "Preview Animation Speed"
                text "When running code in Advanced Mode step-by-step, run at the selected speed."

                vbox:
                    style_prefix "radio"
                    textbutton "Normal (1x)" action SetField(persistent, "mg_speed", 1.0)
                    textbutton "Faster (~1.5x)" action SetField(persistent, "mg_speed", 0.75)
                    textbutton "Fastest (~2x)" action SetField(persistent, "mg_speed", 0.5)
                    textbutton "Warp Speed (~10x)" action SetField(persistent, "mg_speed", 0.1)
        vbox:
            null height 8

        vbox:
            label "Advanced"

            vbox:
                spacing 10

                if uconf["features"]["enable_minigame_adv_mode"]:
                    vbox:
                        style_prefix "check"
                        textbutton "Always show level preview" action ToggleField(persistent, "mg_vm_force_editor")
                        text "When enabled, a preview of the level will always appear before running the code preview, regardless if compiled code already exists.":
                            style "pref_text"
                    vbox:
                        python:
                            savedir = config.savedir + "/minigame"
                            if renpy.windows:
                                savedir = savedir.replace("/", "\\")

                            if renpy.windows:
                                file_manager = "File Explorer"
                            elif renpy.macintosh:
                                file_manager = "Finder"
                            else:
                                file_manager = "File Browser"

                        style_prefix "standard"
                        textbutton "Reveal scripts in [file_manager]" action Function(open_directory, config.savedir + "/minigame")
                        text "Save directory: " + savedir:
                            style "pref_text"
                vbox:
                    style_prefix "link"
                    label "Documentation"
                    text "The following links will open help pages that may assist you in playing the minigame or writing code in Advanced Mode.":
                        style "pref_text"

                    textbutton "NadiaVM Reference..." action Function(open_nvm_reference)
                    if uconf["features"]["enable_minigame_adv_mode"]:
                        textbutton "API Documentation..." action Function(open_api_docs)
