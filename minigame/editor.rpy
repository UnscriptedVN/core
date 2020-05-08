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
    default var_ppos = grid.first("PLAYER")
    default world_matrix = grid.grid
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
                    add MG_CONFIG["assets_path"] + "player_idle_1.png":
                        size 44, 44
                    vbox:
                        text "[config.title] (Level [lvl])"

                        if persistent.mg_adv_mode:
                            text "Minigame - Advanced Mode":
                                style "pref_text"
                        else:
                            text "Minigame":
                                style "pref_text"

                hbox:
                    style_prefix "mg_editor_toolbar_buttons"

                    if not persistent.mg_adv_mode:
                        textbutton "Undo" action Function(vm_writer.undo, ignore_collect=False)
                        textbutton "Clear" action Function(vm_writer.clear)
                        null width 8
                    else:
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
                vbox:
                    if not persistent.mg_adv_mode:
                        hbox:
                            style_prefix "mg_editor_programmable_buttons"
                            if "move" in config.allowed:
                                hbox:
                                    xfill False
                                    vbox:
                                        button action [Function(vm_writer.move, "north"), SetScreenVariable("var_ppos", update_position(var_ppos, "north"))]:
                                            add MG_CONFIG["assets_path"] + "gui/button_move_up.png":
                                                size (MG_CONFIG["button_size"] + 8, MG_CONFIG["button_size"] + 8)
                                        text "Move north":
                                            xalign 0.5 size 12
                                    vbox:
                                        button action [Function(vm_writer.move, "south"), SetScreenVariable("var_ppos", update_position(var_ppos, "south"))]:
                                            add MG_CONFIG["assets_path"] + "gui/button_move_down.png":
                                                size (MG_CONFIG["button_size"] + 8, MG_CONFIG["button_size"] + 8)
                                        text "Move south":
                                            xalign 0.5 size 12
                                    vbox:
                                        button action [Function(vm_writer.move, "west"), SetScreenVariable("var_ppos", update_position(var_ppos, "west"))]:
                                            add MG_CONFIG["assets_path"] + "gui/button_move_left.png":
                                                size (MG_CONFIG["button_size"] + 8, MG_CONFIG["button_size"] + 8)
                                        text "Move west":
                                            xalign 0.5 size 12
                                    vbox:
                                        button action [Function(vm_writer.move, "east"), SetScreenVariable("var_ppos", update_position(var_ppos, "east"))]:
                                            add MG_CONFIG["assets_path"] + "gui/button_move_right.png":
                                                size (MG_CONFIG["button_size"] + 8, MG_CONFIG["button_size"] + 8)
                                        text "Move east":
                                            xalign 0.5 size 12
                            hbox:
                                xfill False

                                if "collect" in config.allowed:
                                    vbox:
                                        button action Function(smart_collect, vm_writer, config.data, var_ppos):
                                            add MG_CONFIG["assets_path"] + "gui/button_collect.png":
                                                size (MG_CONFIG["button_size"] + 8, MG_CONFIG["button_size"] + 8)
                                        text "Get coin":
                                            xalign 0.5 size 12
                                if "exit" in config.allowed:
                                    vbox:
                                        button action Function(vm_writer.exit):
                                            add MG_CONFIG["assets_path"] + "gui/button_exit.png":
                                                size (MG_CONFIG["button_size"] + 8, MG_CONFIG["button_size"] + 8)
                                        text "Exit map":
                                            xalign 0.5 size 12
                    else:
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
                    xsize tile_size * __c
                    ysize tile_size * __r
                    spacing 0

                    for row in range(__r):
                        hbox:
                            for column in range(__c):
                                if column % 2 != 0:
                                    add "mg_floor_alt":
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
                                    add "mg_exit":
                                        size (tile_size, tile_size)
                                elif element == "COIN":
                                    add "mg_coin":
                                        size (tile_size, tile_size)
                                elif element == "PLAYER":
                                    add MG_CONFIG["assets_path"] + "player_idle_1.png":
                                        size (tile_size, tile_size)
                                else:
                                    null width tile_size

            if not persistent.mg_adv_mode:
                $ _mg_spacing = -16 if persistent.mg_condensed_font else 4
                vbox:
                    text "Virtual Machine Input"

                    frame:
                        style "mg_vm_input"
                        viewport:
                            mousewheel True
                            yfill True
                            scrollbars "vertical"
                            style_prefix "mg_vm_viewport"

                            vbox:
                                spacing _mg_spacing
                                for ins in code:
                                    if persistent.mg_vm_show_all:
                                        text "[ins]":
                                            if not visible_command(ins):
                                                style "mg_vm_viewport_hidden_text"
                                    else:
                                        if visible_command(ins):
                                            text "[ins]"
        null height 16
        null height 16


