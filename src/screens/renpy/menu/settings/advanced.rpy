#
# advanced.rpy
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
