#
# splashscreen.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/6/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init 1 python:
    # Connect to Discord RPC, if possible.
    if persistent.use_discord and 'discord' in vars():
        discord.connect()

image splash_bg = "gui/randart/2.png"
image splash = "gui/load.png"
image team = "gui/splash.png"

define in_splash = False
label splashscreen:
    stop music
    python:
        import logging

        in_splash = True

        # Update the rich presence.
        if 'uconf' not in vars():
            logging.error("uconf isn't defined.")
            raise UnscriptedCoreConfigError("The build configuration for Unscripted is missing.")

        if uconf["discord"]["enable_rpc"] and persistent.use_discord:
            discord.update_presence("Just started playing"); discord.refresh_client()

        # Disable skipping.
        config.allow_skipping = False
        skipping = False
        config.allow_skipping = True

    # Display the "Created by Marquis Kurt" splashscreen.
    scene black
    show team at truecenter with dissolve
    $ renpy.pause(1.0, hard=True)
    hide team with dissolve
    show splash at truecenter zorder 2 with dissolve
    show splash_bg at truecenter zorder 1
    $ renpy.pause(0.5, hard=True)
    hide splash with dissolve

    python:
        # Try to connect to Discord again if it failed the first time.
        if uconf["discord"]["enable_rpc"] and persistent.use_discord:
            discord.connect()
        in_splash = False
    return

label before_main_menu:
    python:
        # Update the rich presence to indicate idling on the main menu.
        if uconf["discord"]["enable_rpc"] and persistent.use_discord:
            discord.update_presence("Idle - Main Menu")

        if not config.keymap["open_desktop"]:
            config.keymap["open_desktop"].append("d")

            if not config.developer and uconf["features"]["channel"] == "stable":
                config.keymap["open_desktop"].append("D")
    return

label quit:
    python:
        import logging

        # Try to disconnect the Discord client if enabled.
        if 'uconf' not in vars():
            logging.error("Build configuration is missing or could not be loaded.")
        if 'uconf' in vars() \
            and uconf["discord"]["enable_rpc"] \
            and persistent.use_discord \
            and 'discord' in vars():
            discord.disconnect()
    return
