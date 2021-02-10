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

image splash_bg = "core/assets/artwork/2.png"
image splash = "gui/load.png"
image team = "gui/splash.png"

define in_splash = False
label splashscreen:
    stop music
    python:
        import logging
        import os

        in_splash = True

        # If the Roland boot manager is available, load Candella.
        if "roland" in vars():
            roland.boot(run_setup=False)

        # If the user directory does not exist, create it and the default user session.
        if not os.path.isdir(config.savedir + "/.causerland"):
            logging.warn("Userland folder doesn't exist yet. Creating default user session 'candella'.")
            CAAccountsService().add_user("candella")
            CAAccountsService().change_current_user("candella")
            logging.info("Default user session created. Restarting game to ensure changes take effect.")
            renpy.utter_restart()

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

            if not config.developer and uconf["info"]["channel"] == "stable":
                config.keymap["open_desktop"].append("D")
    return

label quit:
    python:
        import logging

        # If the Roland boot manager is available, shut down Candella via Roland.
        if "roland" in vars():
            roland.shutdown()

        # Try to disconnect the Discord client if enabled.
        if 'uconf' not in vars():
            logging.error("Build configuration is missing or could not be loaded.")
        if 'uconf' in vars() \
            and uconf["discord"]["enable_rpc"] \
            and persistent.use_discord \
            and 'discord' in vars():
            discord.disconnect()
    return
