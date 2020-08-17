#
# editor.rpy
# Unscripted Core - Minigame (Editor)
#
# Created by Marquis Kurt on 04/06/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 10

screen mg_editor(config, vm_writer, lvl=0):
    style_prefix "mg_editor"
    tag mg_editor
    zorder 150
    modal True

    default grid = config.data.to_grid()
    default player_position = grid.first("PLAYER")
    default exit_position = grid.first("EXIT")
    default var_ppos = grid.first("PLAYER")
    default world_matrix = grid.grid
    default walls = config.data.walls().as_list()
    default tile_size = MG_CONFIG["tile_size"]
    default dimensions = config.data.size()
    default code = vm_writer.instructions

    python:
        __r, __c = dimensions

        mg_scripts_dir = renpy.config.savedir + "/minigame"
        if not persistent.mg_adv_mode:
            if __c > 8 or __r > 7:
                tile_size = MG_CONFIG["tile_size"] - (MG_CONFIG["tile_size"] / __r) * (__c / 4)
        else:
            if __c > 10 or __r > 9:
                tile_size = MG_CONFIG["tile_size"] - (MG_CONFIG["tile_size"] / __r) * (__c / 4)

    frame:
        has vbox:
            xfill True
            yfill True

            hbox:
                style_prefix "mg_editor_toolbar"
                style "mg_editor_toolbar"

                hbox:
                    add "mg_player":
                        size 44, 44
                    vbox:
                        text "[config.title] (Level [lvl])"
                        text "Minigame - Advanced Mode":
                            style "pref_text"

                hbox:
                    style_prefix "mg_editor_toolbar_buttons"
                    textbutton "Help" action Function(open_api_docs)
                    textbutton "Open Folder" action Function(open_directory, mg_scripts_dir)
                    null width 8
                    textbutton "Run" action [Function(vm_writer.write), Return()]

        null height 16

        hbox:
            style_prefix "mg_editor_main_view"
            xfill True

            null width 4

            vbox:
                spacing 0
                vbox:
                    vbox:
                        xalign 0.5
                        xsize tile_size * __c

                        text "Start coding here.":
                            xalign 0.5
                        text "Edit the script provided in the scripts folder and then click \"Run\" to compile it.":
                            style "pref_text"
                            xalign 0.5
                    null height 10
                vbox:
                    spacing 0
                    vbox:
                        xsize tile_size * __c
                        ysize tile_size * __r
                        spacing 0

                        for row in range(__r):

                            hbox:
                                for column in range(__c):
                                    $ _is_void = grid.element_at(row, column) == "VOID"
                                    if _is_void:
                                        add "mg_air":
                                            size (tile_size, tile_size)
                                    else:
                                        add "mg_floor":
                                            size (tile_size, tile_size)
                    vbox:
                        yoffset tile_size * -1 * __r
                        xsize tile_size * __c
                        ysize tile_size * __r
                        spacing 0

                        for row in range(__r):
                            hbox:
                                spacing 0
                                for column in range(__c):
                                    $ element = grid.element_at(row, column)

                                    if element == "WALL":
                                        $ full_wall =  is_full_wall(world_matrix, (row, column))
                                        if full_wall:
                                            add "mg_wall_full":
                                                size (tile_size, tile_size)
                                        else:
                                            add "mg_wall":
                                                size (tile_size, tile_size)
                                    elif element == "EXIT":
                                        $ _direction = stairway_type(walls, exit_position)[0]
                                        add "mg_exit_[_direction]":
                                            size (tile_size, tile_size)
                                    elif element == "DESK":
                                        add "mg_device_off":
                                            size (tile_size, tile_size)
                                    elif element == "PLAYER":
                                        add "mg_player":
                                            size (tile_size, tile_size)
                                    elif element == "VOID":
                                        add "mg_air":
                                            size (tile_size, tile_size)
                                    else:
                                        null width tile_size
        null height 16
        null height 16
