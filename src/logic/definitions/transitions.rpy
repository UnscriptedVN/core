#
# transitions.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/6/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

# MARK: Scene Transitions
define immersive_dissolve = Fade(1.0, 2.5, 5.0)
define longfade = Fade(1.0, 2.5, 1.0)
define longdissolve = Dissolve(3.0)
define id_wipeleft = ImageDissolve("core/assets/transitions/id_wipeleft.png", 1.25, ramplen=32)
define id_eyes = ImageDissolve("core/assets/transitions/id_eyes.png", 3.0, ramplen=32)
