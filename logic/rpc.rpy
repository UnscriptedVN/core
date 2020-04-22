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
        def __init__(self, rpc):
            self.client = rpc
            self.start = time.time()
            self.client_callbacks = {
                'ready': self.ready_callback,
                'disconnected': self.disconnected_callback,
                'error': self.error_callback
            }

        def ready_callback(self, current_user):
            renpy.notify("Connected to Discord as " + current_user["username"] + ".")

        def disconnected_callback(self, codeno, codemsg):
            print(0)

        def error_callback(self, errno, errmsg):
            print(0)

        def refresh_client(self):
            self.client.update_connection()
            self.client.run_callbacks()

        def update_presence(self, title="Idle", detail=None):
            self.client.update_presence(
                ** {
                    'state': title,
                    'details': detail if detail is not None else '',
                    'start_timestamp': self.start,
                    'large_image_key': 'game_icon_1024'
                }
            )
            self.refresh_client()

        def connect(self):
            self.client.initialize(uconf["discord"]["client_id"],
                                   callbacks=self.client_callbacks,
                                   log=config.developer)
            self.refresh_client()
            self.update_presence(title="Just started playing")
            self.refresh_client()

        def disconnect(self):
            self.client.shutdown()

init -5 python:
    if uconf["discord"]["enable_rpc"]:
        discord = DiscordRPC(discord_rpc)