#
# audio.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/11/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# All background music herein is owned and licensed by Stray Objects.
# For more information on licensing for this project, contact Stray
# Objects at <admin@strayobjects.com> or visit https://strayobjects.com.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

# MARK: Additional channels
init -50 python:
    renpy.music.register_channel("ambient", mixer="ambient", loop=True)

# Ambient channel setup
init 1000 python hide:
    if not persistent._set_preferences:
        _preferences.set_volume("ambient", 0.2)

# Switch to the old theme music if passed in via arguments.
init -10 python:
    import logging
    _theme_music = "bgm/theme.ogg"
    if "use-classic-music" in arguments and arguments["use-classic-music"]:
        logging.warn("use-classic-music argument will be deprecated in a future build.")
        _theme_music = "bgm/otheme.ogg"     # Simulated Reality

# MARK: BGM
define audio.theme = _theme_music
define audio.t1 = "bgm/t1.ogg"              # Euphoria
define audio.t2 = "bgm/t2.ogg"              # Winter
define audio.t3 = "bgm/t3.ogg"              # Calm
define audio.t4 = "bgm/t4.ogg"              # Dreaming of Another World
define audio.t5 = "bgm/t5.ogg"              # Halls of Tibet
define audio.t6 = "bgm/t6.ogg"              # Life

# MARK: Ambience
define audio.town = "ambient/town.ogg"
define audio.waves = "ambient/waves.ogg"

# MARK: SFX
define audio.knock = "sfx/knock.ogg"
define audio.beep = "sfx/mbeep.ogg"
