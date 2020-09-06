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
    import logging

    def fallthrough_quit():
        """Force-throw out of a context."""
        renpy.jump_out_of_context("quit")

    def call_puzzle(lvl=0):
        """Call the minigame in a new context.

        If the minigame encounters a raised exception that causes the minigame to crash, the game
            will step out of the context and rollback to the last known checkpoint in Ren'Py's
            rollback system.

        If the level is first level (level 0), an alert will be displayed that tells the player
            what to do to solve the minigame puzzle.

        Additionally, if `disable-minigame` is present in the game's arguments file, this function
            will do nothing and exit out of the minigame session.

        Args:
            lvl (int): The level number. Defaults to 0.
        """
        if "disable-minigame" in arguments and arguments["disable-minigame"]:
            logging.info(
                "Minigame level has been skipped because the disable-minigame argument is present."
            )
            return
        quick_menu = False
        renpy.show("mg_bg", at_list=[], zorder=5)
        renpy.with_statement(dissolve)
        __puzzle = MinigameLogicHandler(lvl)
        old_quit = renpy.config.quit_action
        if lvl == 0:
            quick_menu = False
            mia_speak("Ugh...")
            mia_speak("Where... did everyone go?")
            mia_speak("Maybe everyone went home. How long have I been here?")
            mia_speak("Jeez, I must've been here all night...")
            mia_speak(
                "Well, I guess since I'm here early enough, "
                + "I might as well start turning things on..."
            )
            mia_speak("And maybe get some clues about what happened.")
        try:
            renpy.config.quit_action = fallthrough_quit
            renpy.invoke_in_new_context(__puzzle.run)

        # In cases where the user is actually trying to quit, exit out of the context and
        # prompt the quit dialog.
        except renpy.game.JumpException as err:
            renpy.config.quit_action = old_quit
            renpy.run(Quit(confirm=True))

        except Exception as err:
            print(type(err))
            logging.error("Minigame failed to run: %s. Rolling back to last checkpoint...",
                          str(err) if err is not None else "unknown error")
            renpy.rollback()
            renpy.notify("The minigame couldn't run, so the game has rolled back.")
        finally:
            renpy.config.quit_action = old_quit
        renpy.hide("mg_bg")
        renpy.with_statement(dissolve)
        quick_menu = True

    def update_position(player, direction):
        """Get the coordinates of a player when moved in a specific direction.

        Arguments:
            player (tuple): The player's coordinates
            direction (str): The direction that the player will head to.

        Returns:
            pplayer (tuple): The new coordinates of the player.
        """
        transforms = {
            "north": (-1, 0),
            "south": (1, 0),
            "west": (0, -1),
            "east": (0, 1)
        }
        trans_x, trans_y = transforms.get(direction, transforms["east"])
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
            environmen (dict): A dictionary containing the allowed modules in the minigame
                execution space.
        """
        return {'renpy': renpy}

    def matrix_to_scene(coords, shape):
        """Translate a matrix coordinate into a Ren'Py image coordinate.

        Returns:
            coords (tuple): The coordinates for the Ren'Py image.
        """
        row, column = coords
        shape_rows, shape_columns = shape
        x = (1280 / shape_columns) * 2 + MG_CONFIG["tile_size"] * column
        y = (720 / shape_rows) + MG_CONFIG["tile_size"] * row
        return x, y

    def get_move_direction(direction):
        """Get the lable for which direction to move."""
        mapping = {
            "north": "up",
            "south": "down",
            "east": "right",
            "west": "left"
        }

        return mapping.get(direction, None)

    def is_full_wall(matrix, current_pos):
        """Determine whether a wall is "full" in a given position.

        Arguments:
            matrix (list): The grid of elements to look through. (The layout)
            current_pos (tuple): The wall's current position.

        Returns:
            vertical (bool): Whether the wall is in a vertical series and is not in the final row.
        """
        x, y = current_pos

        vertical = matrix[x + 1 if x + 1 < len(matrix) else 0][y] == "WALL"
        not_end = x + 1 < len(matrix)

        return vertical and not_end

    def visible_command(ins):
        """Determine whether the VM command should be displayed on the screen.

        Arguments:
            ins (str): The full VM command with its  arguments.

        Returns:
            visible (bool): Whether the VM command should be displayed on the screen.
        """
        return not ins.startswith("alloc") \
            and not ins.startswith("push") \
            and not ins.startswith("pop") \
            and not ins.startswith("set")

    def stairway_type(matrix, exit_location):
        """Determine what orientation the exit stairway should be.

        Args:
            matrix (list): The matrix containing all walls
            exit_location: The location of the exit

        Returns:
            cardinal (str): String containing the direction the stairs should be.
        """
        ex, ey = exit_location

        radius = [(ex, ey - 1), (ex + 1, ey), (ex, ey + 1), (ex - 1, ey)]
        walls = tuple([cardinal in matrix for cardinal in radius])

        options = {
            (True, True, False, True): "west",
            (True, True, True, False): "north",
            (False, True, True, True): "east",
            (True, False, True, True): "south"
        }

        return options.get(walls, "north")

    def mia_speak(what):
        """Bootstrapper to get Mia to speak in-game."""
        mi(
            what,
            what_font="core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf",
            what_color="#f4f4f4",
            who_font="core/assets/fonts/jb_mono/JetBrainsMono-Bold.ttf",
            who_color="#f4f4f4"
        )
