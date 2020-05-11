#
# scene.rpy
# Unscripted Core - Credits (Scene)
#
# Created by Marquis Kurt on 04/14/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 10

image credits_bg = "#2b2b2b"

label credits:
    $ config.allow_skipping = allow_skipping = skipping = quick_menu = False
    $ config.keymap["game_menu"] = [ ]
    scene black with fade
    $ username = get_username()
    play music theme
    show credits_bg with dissolve
    python:
        for i in range(4):
            __lex = KtCreditsLexer("core/src/credits/kt/credits%s.kts" % (i))
            __toks = transform_tokens(__lex.tokenize())
            renpy.call_screen("credits", __toks)
    pause 2.0
    hide credits_bg with dissolve
    stop music fadeout 5.0
    pause 3.0
    python:
        config.allow_skipping = allow_skipping = quick_menu = True
        username = None
        config.keymap["game_menu"] = [ 'K_ESCAPE', 'K_MENU', 'mouseup_3' ]
    show splash_bg at truecenter with dissolve
    return