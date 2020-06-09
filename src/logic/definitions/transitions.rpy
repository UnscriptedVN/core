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

# MARK: Fake Reload
image reload_bg = "#000"
image fake_reload = Text("{color=#fff}Reloading script...{/color}", size=40, style="_default")
image fake_reload2 = Text("{color=#fff}Reloading game...{/color}", size=40, style="_default")

# This label simulates Ren'Py's "Reloading script/Reloading game" loading
# screen whenever the script is updated or if auto-reload was turned on.
label reloading_game:
    stop music
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    window hide
    show reload_bg at truecenter
    show fake_reload at truecenter
    $ renpy.pause(1.0, hard=True)
    hide fake_reload
    $ renpy.pause(0.10, hard=True)
    show fake_reload2 at truecenter
    $ renpy.pause(2.5, hard=True)
    $ config.skipping = False
    $ config.allow_skipping = True
    $ allow_skipping = True
    $ quick_menu = True
    hide fake_reload2
    hide reload_bg
    window show
    return
