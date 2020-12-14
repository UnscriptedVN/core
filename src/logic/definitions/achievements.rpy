#
# achievements.rpy
# Unscripted
#
# Created by Marquis Kurt on 12/13/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init python:
    for id in range(3):
        achievement.register("UVN" + str(id))
    achievement.sync()
