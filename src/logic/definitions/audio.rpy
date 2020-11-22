#
# audio.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/11/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# Apart from the theme music written by Marek Domagała, all background music
# herein is owned and licensed by Stray Objects. For more information on
# licensing for this project, contact Stray Objects at <admin@strayobjects.com>
# or visit https://strayobjects.com.
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

# Switch to the old theme music if passed in via arguments.
init -10 python:
    import logging
    if "use-classic-music" in arguments and arguments["use-classic-music"]:
        logging.warn("use-classic-music has been removed.")

# MARK: BGM
define audio.theme = "bgm/theme.ogg"

# TODO: Replace the audio segments with the dynamic music from Marek. Implementations of the music
# in the story will need to be updated as well, respective to the tracks provided. Current tracks
# from Stray Objects can be used in the minigame scenes instead.
define audio.p1 = "bgm/perc/p1.ogg"
define audio.p2 = "bgm/perc/p2.ogg"
define audio.p3 = "bgm/perc/p3.ogg"
define audio.p4 = "bgm/perc/p4.ogg"

define audio.p1c = "bgm/perc/p1c.ogg"
define audio.p2c = "bgm/perc/p2c.ogg"
define audio.p3c = "bgm/perc/p3c.ogg"
define audio.p4c = "bgm/perc/p4c.ogg"

define audio.t1_new = "bgm/layer/t1.ogg"
define audio.t1b_new = "bgm/layer/t1b.ogg"

define audio.t3_new = "bgm/layer/t3.ogg"
define audio.t4_new = "bgm/layer/t4.ogg"
define audio.t5_new = "bgm/layer/t5.ogg"
define audio.t6_new = "bgm/layer/t6.ogg"

define audio.tz = "bgm/char/tz.ogg"
define audio.tk = "bgm/char/tk.ogg"
define audio.tc = "bgm/char/tc.ogg"
define audio.tf = "bgm/char/tf.ogg"

define audio.tzc = "bgm/char/tzc.ogg"
define audio.tkc = "bgm/char/tkc.ogg"
define audio.tcc = "bgm/char/tcc.ogg"
define audio.tfc = "bgm/char/tfc.ogg"

define audio.mg_interactive = "bgm/mg_inter.ogg"

# NOTE: These tracks will be deprecated in a future release.
define audio.t1 = "bgm/deprecated/t1.ogg"              # Euphoria
define audio.t2 = "bgm/deprecated/t2.ogg"              # Winter
define audio.t3 = "bgm/deprecated/t3.ogg"              # Calm
define audio.t4 = "bgm/deprecated/t4.ogg"              # Dreaming of Another World
define audio.t5 = "bgm/mg_inter.ogg"                   # Halls of Tibet
define audio.t6 = "bgm/deprecated/t6.ogg"              # Life

# MARK: Ambience
define audio.town = "ambient/town.ogg"
define audio.waves = "ambient/waves.ogg"

# MARK: SFX
define audio.knock = "sfx/knock.ogg"
define audio.beep = "sfx/mbeep.ogg"
