#
# rpc.py
# Unscripted Core - Discord Rich Presence
#
# Created by Marquis Kurt on 04/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init -10 python:
    import discord_rpc
    import time

    class DiscordRPC(object):
        """The Discord rich presence object.

        Attributes:
            client (discord_rpc): The rich present client module
            start (time): The time that the client started
            client_callbacks (dict): A dictionary containing the callbacks for the Discord client
        """
        def __init__(self, rpc):
            """Initialize a rich presence client.

            Arguments:
                rpc (discord_rpc): The module to use as the rich presence client
            """
            self.client = rpc
            self.start = time.time()
            self.client_callbacks = {
                'ready': self.ready_callback,
                'disconnected': self.disconnected_callback,
                'error': self.error_callback
            }

        def ready_callback(self, current_user):
            """Run this callback when the client has connected.

            Arguments:
                current_user (dict): A dictionary containing information about the current user.
            """
            renpy.notify("Connected to Discord as " + current_user["username"] + ".")

        def disconnected_callback(self, codeno, codemsg):
            """Run this callback when the client has disconnected."""
            print(0)

        def error_callback(self, errno, errmsg):
            """Run this callback when the client has encountered an error."""
            print(0)

        def refresh_client(self):
            """Update the client's connection and run callbacks."""
            self.client.update_connection()
            self.client.run_callbacks()

        def update_presence(self, title="Idle", **kwargs):
            """Update the rich presence and refresh the client.

            Arguments:
                title (str): The title to use

            Kwargs:
                detail (str): The supporting text to use
                image (str): The key of the image to display
            """
            details = "" if "detail" not in kwargs else kwargs["detail"]
            img = "game_icon_1024" if "image" not in kwargs else kwargs["image"]
            text = "" if "large_text" not in kwargs else kwargs["large_text"]

            self.client.update_presence(
                ** {
                    'state': title,
                    'details': details,
                    'start_timestamp': self.start,
                    'large_image_key': img,
                    'large_image_text': text
                }
            )
            self.refresh_client()

        def connect(self):
            """Connect the client to Discord."""
            self.client.initialize(uconf["discord"]["client_id"],
                                   callbacks=self.client_callbacks,
                                   log=config.developer)
            self.refresh_client()
            self.update_presence(title="Just started playing")
            self.refresh_client()

        def disconnect(self):
            """Disconnect the client from Discord."""
            self.client.shutdown()

init -5 python:
    if uconf["discord"]["enable_rpc"]:
        discord = DiscordRPC(discord_rpc)