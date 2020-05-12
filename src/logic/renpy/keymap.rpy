#
# keymap.rpy
# Unscripted Core - Keymap
#
# Created by Marquis Kurt on 05/09/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init -10 python:
    # Remove the mouse scroll rollback function in the game when not in developer mode (or if the)
    if not config.developer and uconf["features"]["channel"] == "stable":
        config.keymap["rollback"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK']

    # Set the keymap binding for opening the logs.
    config.keymap["open_log"] = ['l', 'L']
    config.keymap["open_desktop"] = ['d', 'D']


init -130 python:
    def open_uvn_log():
        """Open the logs for Unscripted."""
        open_directory(log_filename)
        renpy.notify("The log file has been opened or selected in your file browser.")

    def open_desktop():
        renpy.invoke_in_new_context(renpy.call_screen, "ASDesktopShellView")

    # Create a custom keymap with the respective functions and details.
    _uvn_keymap = renpy.Keymap(
        open_log = open_uvn_log,
        open_desktop = open_desktop
    )

    # Append the keymap to the existing keymap.
    config.underlay.append(_uvn_keymap)
