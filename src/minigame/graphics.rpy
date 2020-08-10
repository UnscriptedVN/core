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

image mg_overlay = "#1c0b190D"

image mg_window:
    MG_CONFIG["assets_path"] + "/gui/textbox.png"
    nearest True
    xalign 0.5
    yalign 1.1

image mg_floor:
    MG_CONFIG["assets_path"] + "/tilemap/floor.png"
    nearest True

image mg_floor_alt:
    MG_CONFIG["assets_path"] + "/tilemap/floor.png"
    nearest True

image mg_wall_full:
    MG_CONFIG["assets_path"] + "tilemap/wall_top.png"
    nearest True

image mg_wall:
    MG_CONFIG["assets_path"] + "tilemap/wall_side.png"
    nearest True

image mg_exit_n:
    MG_CONFIG["assets_path"] + "tilemap/exit_stairway_north.png"
    nearest True

image mg_exit_e:
    MG_CONFIG["assets_path"] + "tilemap/exit_stairway_east.png"
    nearest True

image mg_exit_w:
    MG_CONFIG["assets_path"] + "tilemap/exit_stairway_west.png"
    nearest True

image mg_exit_s:
    MG_CONFIG["assets_path"] + "tilemap/exit_stairway_south.png"
    nearest True

image mg_compass:
    MG_CONFIG["assets_path"] + "elements/compass.png"
    nearest True

image mg_beanbag:
    MG_CONFIG["assets_path"] + "elements/beanbag.png"
    nearest True

image mg_device_off:
    MG_CONFIG["assets_path"] + "elements/device_off.png"
    nearest True

image mg_device_on:
    choice:
        MG_CONFIG["assets_path"] + "elements/device_on.png"
    choice:
        MG_CONFIG["assets_path"] + "elements/device_on2.png"
    choice:
        MG_CONFIG["assets_path"] + "elements/device_on3.png"
    nearest True

image mg_air = "#00000000"

image mg_player:
    MG_CONFIG["assets_path"] + "sprite/idle.png"
    nearest True

image mg_player_move:
    nearest True
    block:
        MG_CONFIG["assets_path"] + "sprite/walk1.png"
        pause 0.5
        MG_CONFIG["assets_path"] + "sprite/walk2.png"
        pause 0.5
        "mg_player"

image mg_player_confused:
    nearest True
    block:
        MG_CONFIG["assets_path"] + "sprite/confused1.png"
        pause 0.5
        MG_CONFIG["assets_path"] + "sprite/confused2.png"
        pause 0.5
        "mg_player"

image mg_player_cry:
    nearest True
    block:
        MG_CONFIG["assets_path"] + "sprite/cry1.png"
        pause 0.5
        MG_CONFIG["assets_path"] + "sprite/cry2.png"
        pause 0.5
        repeat

image mg_player_happy:
    nearest True
    block:
        MG_CONFIG["assets_path"] + "sprite/smile1.png"
        pause 0.5
        MG_CONFIG["assets_path"] + "sprite/smile2.png"
        pause 0.5
        repeat
