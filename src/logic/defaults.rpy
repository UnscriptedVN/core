#
# defaults.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/30/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

# Save Data
default chapter_name = None
default default_chapter_names = [
    "Arrival",
    "Faces",
    "Possibility",
    "Shell",
    "Establishment",
    "Perspective",
    "Forks",
    "Exhibit",
    "Focus"
]

# Settings
default persistent.use_discord = uconf["discord"]["enable_rpc"]
default persistent.lexend_width = 1
default persistent.use_detailed_saves = False

default persistent.mg_speed = 1.0
default persistent.mg_adv_mode = False
default persistent.mg_condensed_font = False
default persistent.mg_vm_show_all = False
default persistent.mg_vm_force_editor = True