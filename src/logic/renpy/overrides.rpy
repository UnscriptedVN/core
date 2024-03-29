#
# overrides.rpy
# Unscripted
#
# Created by Marquis Kurt on 2019-2020-08-26
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init 10 python:
    import os
    import logging
    from uvn_fira.core import generate_template

    # If the minigame folder is missing from the save directory, create the necessary
    # folders and copy over the Python scripts.
    if "minigame" not in os.listdir(config.savedir):
        logging.warn("Minigame folder is missing from save directory. Re-creating...")
        os.mkdir(os.path.join(config.savedir, "minigame"))

    if "compiled" not in os.listdir(os.path.join(config.savedir, "minigame")):
        logging.warn("Compilation folder is missing from save directory. Re-creating...")
        os.mkdir(os.path.join(config.savedir, "minigame", "compiled"))

    only_levels = lambda a: a.endswith(".toml") and a.startswith("core/src/minigame/levels/level")

    all_levels = list(filter(only_levels, renpy.list_files()))
    for level in range(len(all_levels)):
        if "level%s.py" % (level) not in os.listdir(os.path.join(config.savedir, "minigame")):
            logging.warn("Script for level %s is missing. Creating from a new template..." % (level))
            generate_template(os.path.join(config.savedir,
                                           "minigame",
                                           "level%s.py" % (level)),
                              level)


init 1000:
    # Override the Desktop image picture.
    define AS_DESKTOP_IMG = "core/assets/artwork/wallpaper.png"
