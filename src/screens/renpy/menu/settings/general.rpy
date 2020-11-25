#
# general.rpy
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

screen general_settings():
    style_prefix "pref"
    hbox:
        box_wrap True

        vbox:
            style_prefix "radio"

            python:
                rollback_image = "core/assets/interface/previews/rollback_" + preferences.desktop_rollback_side  + ".png"
            label _("Rollback gesture")
            add rollback_image:
                zoom 0.95

            textbutton _("Don't roll back") action Preference("rollback side", "disable")
            textbutton _("Click on the left side") action Preference("rollback side", "left")
            textbutton _("Click on the right side") action Preference("rollback side", "right")
            text "When enabled, clicking in the specified region will go back to the previous sentence.":
                style "pref_text"

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
