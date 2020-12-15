#
# audio.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/11/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# Music for this game is composed by Marek Domagała. See the LICENSE
# for details on what you can and can't do with the game music.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

# MARK: Additional channels
init -50 python:

    # The ambient channel is registered as the channel responsible for handling ambient sounds such
    # as town noises, beach waves, etc.
    renpy.music.register_channel("ambient", mixer="ambient", loop=True)

    # The following music channels are registered as a subset of the music channel and are used to
    # handle the dynamic music effect achieved for the soundtrack. These channels will host melodic
    # content over the base track in the standard music track.
    renpy.music.register_channel("music_char", mixer="music", loop=True)
    renpy.music.register_channel("music_mood", mixer="music", loop=True)

# Ambient channel setup
init 1000 python hide:
    if not persistent._set_preferences:
        _preferences.set_volume("ambient", 0.2)

# MARK: BGM
define audio.theme = "bgm/theme.ogg"

define audio.p1 = "bgm/perc/p1.ogg"
define audio.p2 = "bgm/perc/p2.ogg"
define audio.p3 = "bgm/perc/p3.ogg"
define audio.p4 = "bgm/perc/p4.ogg"

define audio.p1c = "bgm/perc/p1c.ogg"
define audio.p2c = "bgm/perc/p2c.ogg"
define audio.p3c = "bgm/perc/p3c.ogg"
define audio.p4c = "bgm/perc/p4c.ogg"

define audio.t1 = "bgm/layer/t1.ogg"
define audio.t1b = "bgm/layer/t1b.ogg"

define audio.t3 = "bgm/layer/t3.ogg"
define audio.t4 = "bgm/layer/t4.ogg"
define audio.t5 = "bgm/layer/t5.ogg"
define audio.t6 = "bgm/layer/t6.ogg"

define audio.tz = "bgm/char/tz.ogg"
define audio.tk = "bgm/char/tk.ogg"
define audio.tc = "bgm/char/tc.ogg"
define audio.tf = "bgm/char/tf.ogg"

define audio.tzc = "bgm/char/tzc.ogg"
define audio.tkc = "bgm/char/tkc.ogg"
define audio.tcc = "bgm/char/tcc.ogg"
define audio.tfc = "bgm/char/tfc.ogg"

# LICENSE NOTE: The interactive minigame track has been licensed to the Unscripted team by Stray
# Objects. For more information on licensing for this project, contact Stray Objects at
# <admin@strayobjects.com> or visit https://strayobjects.com.
define audio.mg_interactive = "bgm/mg_inter.ogg"

# MARK: Ambience
define audio.town = "ambient/town.ogg"
define audio.waves = "ambient/waves.ogg"

# MARK: SFX
define audio.knock = "sfx/knock.ogg"
define audio.beep = "sfx/mbeep.ogg"

# MARK: VOICE-OVER
define audio.vo_ch12_m0 = ""
define audio.vo_ch12_m1 = ""
define audio.vo_ch12_m2 = ""
define audio.vo_ch12_m3 = ""
define audio.vo_ch12_m4 = ""
define audio.vo_ch12_m5 = ""
