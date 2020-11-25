#
# sound.rpy
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
