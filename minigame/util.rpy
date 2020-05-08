#
# util.rpy
# Unscripted Core - Minigame (Utilities)
#
# Created by Marquis Kurt on 01/13/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 5

init python:
    def update_position(player, direction):
        transforms = {
            "north": (-1, 0),
            "south": (1, 0),
            "west": (0, -1),
            "east": (0, 1)
        }
        trans_x, trans_y = transforms.get(direction, "east")
        curr_x, curr_y = player
        pplayer = curr_x + trans_x, curr_y + trans_y
        return pplayer

    def smart_collect(vm_writer, data, curr_pos):
        """Run a smarter version of vm.collect.

        Arguments:
            vm_writer (CSNadiaVMWriterBuilder): The VM writer to write commands with.
            data (CSWorldDataGenerator): The world data.
            pos (tuple): The current world position of the player.
        """
        coins = data.coins().as_list()
        if curr_pos in coins:
            index = coins.index(curr_pos)
            vm_writer.pop("world_coins", index)
            vm_writer.push("inventory", index)
        vm_writer.collect()

    def py_sandbox():
        """Create a list of allowed Python modules for use with the Advanced Mode.

        Returns:
            environment: A dictionary containing the allowed modules in the minigame execution
                space.
        """
        return {'renpy': renpy}
    def call_puzzle(lvl=0):
        """Call the minigame in a new context.

        Args:
            lvl: The level number.
        """
        quick_menu = False
        renpy.show("mg_bg", at_list=[], zorder=5)
        renpy.with_statement(dissolve)
        __puzzle = MinigameLogicHandler(lvl)
        if lvl == 0:
            renpy.call_screen("ASNotificationAlert",
                              "Let's help Masti!",
                              "Guide Masti through the world and collect every coin by clicking" +
                              " on the command buttons at the top. For an extra challenge, try" +
                              " the Advanced Mode and solve the puzzles by writing Python code!")
        renpy.invoke_in_new_context(__puzzle.run)
        renpy.hide("mg_bg")
        renpy.with_statement(dissolve)
        quick_menu = True

    def matrix_to_scene(coords, shape):
        """Translate a matrix coordinate into a Ren'Py image coordinate."""
        row, column = coords
        shape_rows, shape_columns = shape
        x = (1280 / shape_columns) * 2 + MG_CONFIG["tile_size"] * column
        y = (720 / shape_rows) + MG_CONFIG["tile_size"] * row
        return x, y

    def get_move_direction(direction):
        mapping = {
            "north": "up",
            "south": "down",
            "east": "right",
            "west": "left"
        }

        return mapping.get(direction, None)

    def is_full_wall(matrix, current_pos):
        """Determine whether a wall is "full" in a given position.

        Args:
            matrix: The grid of elements to look through. (The layout)
            current_pos: The wall's current position.

        Returns:
            Whether the wall is in a vertical series and is not in the
            final row.
        """
        x, y = current_pos

        vertical = matrix[x + 1 if x + 1 < len(matrix) else 0][y] == "WALL"
        not_end = x + 1 < len(matrix)

        return vertical and not_end

    def visible_command(ins):
        return not ins.startswith("alloc") \
            and not ins.startswith("push") \
            and not ins.startswith("pop") \
            and not ins.startswith("set")