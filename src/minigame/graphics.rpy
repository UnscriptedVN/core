#
# graphics.rpy
# Unscripted Core - Minigame (Graphics)
#
# Created by Marquis Kurt on 04/06/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 10

image mg_bg = "#212121"
image mg_bg_alt = "#000909"
image mg_floor = MG_CONFIG["assets_path"] + "floor.png"
image mg_floor_alt = MG_CONFIG["assets_path"] + "floor_alt.png"
image mg_wall_full = MG_CONFIG["assets_path"] + "wall_full.png"
image mg_wall = MG_CONFIG["assets_path"] + "wall.png"
image mg_exit = MG_CONFIG["assets_path"] + "exit.png"
image mg_coin = MG_CONFIG["assets_path"] + "coin.png"
image mg_air = "#00000000"

# image mg_player:
#     block:
#         MG_CONFIG["assets_path"] + "player_idle_1.png"
#         pause 0.5
#         MG_CONFIG["assets_path"] + "player_idle_2.png"
#         pause 0.5
#         repeat

image mg_player = MG_CONFIG["assets_path"] + "sprite/idle.png"

image mg_player_move:
    block:
        MG_CONFIG["assets_path"] + "sprite/walk1.png"
        pause 0.5
        MG_CONFIG["assets_path"] + "sprite/walk2.png"
        pause 0.5
        "mg_player"

image mg_player_confused:
    block:
        MG_CONFIG["assets_path"] + "sprite/confused1.png"
        pause 0.5
        MG_CONFIG["assets_path"] + "sprite/confused2.png"
        pause 0.5
        "mg_player"

image mg_player_cry:
    block:
        MG_CONFIG["assets_path"] + "sprite/cry1.png"
        pause 0.5
        MG_CONFIG["assets_path"] + "sprite/cry2.png"
        pause 0.5
        repeat

image mg_player_happy:
    block:
        MG_CONFIG["assets_path"] + "sprite/smile1.png"
        pause 0.5
        MG_CONFIG["assets_path"] + "sprite/smile2.png"
        pause 0.5
        repeat
