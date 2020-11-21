#
# settings.rpy
# Unscripted Core - Default Settings
#
# Created by Marquis Kurt on 05/11/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

# The following file contains the additional settings parameters for the game. Each settings group
# is broken up into categories, separated with MARK. For settings that have been deprecated but not
# removed, see the bottom of the file in the 'DEPRECATED' category.



# - MARK: APPEARANCE

# Whether to use the dynamic background on the main menu.
default persistent.prefers_dynamic_bg = True

# The width variant for the Lexend font family.
default persistent.lexend_width = 1

# Whether to show screenshots in the save/load menu.
default persistent.use_detailed_saves = False

# Whether to announce chapter names when a chapter starts.
default persistent.announce_chapters = False



# - MARK: MINIGAME

# Whether to run the minigame. This can be turned off for those that may encounter accessibility
# issues with the minigame or wish for a kinetic experience.
default persistent.mg_enabled = True

# The execution speed for the animations in the minigame.
default persistent.mg_speed = 1.0

# Whether the minigame's Advanced Mode is enabled.
default persistent.mg_adv_mode = False

# Whether to forcible display the editor window, even if pre-compiled code exists.
default persistent.mg_vm_force_editor = True



# - MARK: CONNECTIVITY

# Whether to connect to the Discord client.
default persistent.use_discord = uconf["discord"]["enable_rpc"] or False



# MARK: - DEPRECATED

# Whether to use the condensed font option in the preview.
default persistent.mg_condensed_font = False

# Whether to show all commands in the preview.
default persistent.mg_vm_show_all = False
