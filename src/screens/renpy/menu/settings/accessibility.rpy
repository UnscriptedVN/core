#
# accessibility.rpy
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

screen accessibility_settings():
    style_prefix "pref"
    hbox:
        box_wrap True

        vbox:
            style_prefix "check"
            spacing 10
            vbox:
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

        vbox:
            style_prefix "check"
            spacing 10
            vbox:
                label "Interactions"
                textbutton _("Enable minigame experience") action ToggleField(persistent, "mg_enabled")
                text "This may be optimal if you are encountering accessibility issues with the input methods or prefer a kinetic experience.":
                    style "pref_text"

                textbutton _("Enable item interactions") action ToggleField(persistent, "enable_item_callbacks")
                text "When enabled, scenes with inventory item interactions will prompt you to use items.":
                    style "pref_text"
