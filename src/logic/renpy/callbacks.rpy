#
# callbacks.rpy
# Unscripted Core
#
# Created by Marquis Kurt on 01/08/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

# Save files
init -10 python:
    import os

    def save_player(d):
        """Save a serialized version of the Player object
        to the Ren'Py save file.
        """
        d["player"] = store.player.serialize()

    def save_chaptername(d):
        """Save the current chapter name to the save file.
        """
        d["chapter_name"] = store.chapter_name


label after_load:
    python:
        logging.info("Loaded Chapter %s from save successfully.", store.chapter_count + 1)

        # Restore the player's inventory from the save file.
        clear_inventory()
        restore_inventory()
        logging.info("Restored player inventory.")

        # Update the presence to display the chapter name and
        # player name.
        if uconf["discord"]["enable_rpc"] and persistent.use_discord:
            change_playing_state()

        # Enable the quick menu if it was disabled.
        restore_vn_state()
    return
