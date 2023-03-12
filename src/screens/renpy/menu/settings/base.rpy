#
# base.rpy
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
                textbutton _("Accessibility") action SetScreenVariable("settings_page", "accessibility")
                textbutton _("Extras") action SetScreenVariable("settings_page", "extras")

            null height (4 * gui.pref_spacing)

            use expression settings_page + "_settings"
