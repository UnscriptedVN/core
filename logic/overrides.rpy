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

init -10 python:
    # Remove the mouse scroll rollback function in the game when not in
    # developer mode to prevent accidental triggers on laptops.
    if not config.developer:
        config.keymap["rollback"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK']

init 10 python:
    import os
    from uvn_fira.core import generate_template

    # If the minigame folder is missing from the save directory, create the necessary
    # folders and copy over the Python scripts.
    if "minigame" not in os.listdir(config.savedir):
        print("[WARN] Minigame folder is missing from save directory. Re-creating...")
        os.mkdir(os.path.join(config.savedir, "minigame"))

    if "compiled" not in os.listdir(config.savedir + "/minigame"):
        print("[WARN] Compilation folder is missing from save directory. Re-creating...")
        os.mkdir(os.path.join(config.savedir, "minigame/compiled"))

    only_levels = lambda a: a.endswith(".toml") and a.startswith("core/minigame/levels/level")

    for level in range(len(filter(only_levels, renpy.list_files()))):
        if "level%s.py" % (level) not in os.listdir(os.path.join(config.savedir, "minigame")):
            print("[WARN] Script for level %s is missing. Creating from a new template..." % (level))
            generate_template(os.path.join(config.savedir, "minigame/")
                                + "level%s.py" % (level),
                              level)


init 1000:
    # Override the Desktop image picture.
    define AS_DESKTOP_IMG = "gui/as_desktop_img.png"