#
# transforms.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/8/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

default common_zoom_param = 0.4
default common_dual_left_param = 0.25
default common_dual_right_param = 0.75

default common_entry_zoom_param = common_zoom_param - 0.1

# MARK: Common Transforms
transform tcommon:
    alpha 1.0
    zoom common_zoom_param

    on start:
        easein 0.10 yalign 1.0 alpha 1.0 yoffset 0 zoom common_zoom_param

    on show:
        zoom 0.35
        alpha 0.0
        easein_cubic 0.25 zoom common_zoom_param alpha 1.0

transform hcommon:
    zoom common_zoom_param
    on start:
        easein_cubic 0.075 yalign 1.0 yoffset -24
        easeout_cubic 0.10 yalign 1.0 yoffset 0

transform scommon:
    zoom common_zoom_param
    on start:
        easein 0.75 yalign 1.0 yoffset 24

# MARK: Positioning (Regular)
transform tsingle:
    xalign 0.5
    yalign 1.0
    tcommon

    on show:
        easein_cubic 0.10 xalign 0.5 yalign 1.0 yoffset 0
        tcommon

    on replace:
        easein_cubic 0.10 xalign 0.5 yalign 1.0 yoffset 0
        tcommon

transform tdual1:
    alpha 1.0
    zoom common_zoom_param

    on show:
        xalign common_dual_left_param
        yalign 1.0
        tcommon

    on replace:
        easein_cubic 0.45 xalign common_dual_left_param yalign 1.0 alpha 1.0
        tcommon

transform tdual2:
    alpha 1.0
    zoom common_zoom_param

    on show:
        xalign common_dual_right_param
        yalign 1.0
        tcommon

    on replace:
        easein_cubic 0.45 xalign common_dual_right_param yalign 1.0 alpha 1.0
        tcommon

# MARK: Positioning (Hop)
transform hsingle:
    alpha 1.0
    zoom 0.8
    xalign 0.5
    yalign 1.0
    hcommon

transform hdual1:
    alpha 1.0
    zoom common_zoom_param
    xalign common_dual_left_param
    yalign 1.0
    hcommon

transform hdual2:
    alpha 1.0
    zoom common_zoom_param
    xalign common_dual_right_param
    yalign 1.0
    hcommon

# MARK: Positioning (Sink)
transform ssingle:
    alpha 1.0
    zoom common_zoom_param
    xalign 0.5
    yalign 1.0
    scommon

transform sdual1:
    alpha 1.0
    zoom common_zoom_param
    xalign common_dual_left_param
    yalign 1.0
    scommon

transform sdual2:
    alpha 1.0
    zoom common_zoom_param
    xalign common_dual_right_param
    yalign 1.0
    scommon

# MARK: Positioning (Special)

# Face
transform face:
    on start:
        linear 0.1 xalign 0.5 yalign 0.25 zoom 0.95

# Hides
transform thide:
    zoom common_zoom_param

    on hide:
        easeout_cubic 0.25 zoom common_entry_zoom_param alpha 0.0

transform lhide:
    zoom common_zoom_param

    on hide:
        easeout_cubic 0.25 xpos -1000
        linear 0.1 alpha 0.0

transform rhide:
    zoom common_zoom_param

    on hide:
        easeout_cubic 0.25 xpos 1000
        linear 0.1 alpha 0.0
