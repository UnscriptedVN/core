#
# preview.rpy
# Unscripted Core - Minigame (Preview)
#
# Created by Marquis Kurt on 04/06/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 10

# Transform for fading in matrix elements
transform minigame_matrix_pos(x,y):
    alpha 0.0
    pos (x, y)
    size (MG_CONFIG["tile_size"], MG_CONFIG["tile_size"])
    linear 0.1 alpha 1.0

# Transform for moving the player
transform minigame_player_pos(x,y):
    size (MG_CONFIG["tile_size"], MG_CONFIG["tile_size"])
    easein_cubic (1.5 * persistent.mg_speed) pos (x, y)

label mg_preview(vm, world):
    window hide

    # Set up the environment based on the provided world data and the NadiaVM that we will read
    # instructions from.
    python:
        quick_menu = config.allow_skipping = allow_skipping = skipping = False
        floor_grid = []
        mg_return_code = 0
        mg_rows, mg_columns = world.data.to_grid().shape()
        mg_preview_player_pos = 0, 0
        mg_player_pos = world.data.to_grid().first("PLAYER")
        mg_exit_pos = world.data.to_grid().first("EXIT")

    # Start rendering the scene.
    scene mg_bg_alt with dissolve
    pause 0.5

    python:
        import logging
        element_image_names = {
            "WALL": "mg_wall",
            "COIN": "mg_device_off",
            "EXIT": "mg_exit",
            "PLAYER": "mg_player"
        }

        # Render a floor underneath the world grid, and then render the grid.
        for _r in range(mg_rows):
            for _c in range(mg_columns):

                curr_tag = "matrix_base_%s_%s" % (_r, _c)
                floor_grid.append(curr_tag)
                img_xpos, img_ypos = matrix_to_scene((_r, _c), (mg_rows, mg_columns))
                use_alt_design = _c % 2 == 0

                renpy.show("mg_floor_alt" if use_alt_design else "mg_floor",
                           at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                           tag=curr_tag)

                element = world.data.to_grid().element_at(_r, _c)
                img_name = element_image_names.get(element, "mg_air")

                if element == "WALL" and is_full_wall(world.data.to_grid().grid, (_r, _c)):
                    img_name += "_full"

                if element == "PLAYER":
                    mg_player_pos = img_xpos, img_ypos

                if element == "EXIT":
                    img_name += "_" + stairway_type(world.data.walls().as_list(), (_r, _c))[0]
                curr_tag = "player" if element == "PLAYER" else "matrix_%s_%s_%s" \
                                        % (element, _r, _c)
                renpy.show(img_name,
                           at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                           tag=curr_tag,
                           zorder=3 if element == "PLAYER" else 2)

        renpy.show("mg_overlay", zorder=10)
        # Pause before starting the VM execution.
        renpy.pause(1.5, hard=True)

        # Run through the VM loop while there are still instructions.
        while vm.has_more_instructions():
            current_instruction = vm.preview_next_instruction()
            logging.info("Current instruction in VM stack: %s", current_instruction)
            vm.next()

            # If the current instruction is a game-related instruction and not a VM management
            # command, play the required animations.
            if current_instruction not in ["alloc", "set", "push", "pop"]:
                if current_instruction == "move":
                    mg_player_pos = vx, vy = vm.get_position()

                    # Display a confused animation if the player is in an invalid position.
                    if vx > mg_rows - 1 or vy > mg_columns - 1 \
                        or world.data.to_grid().element_at(vx, vy) == "WALL":
                        logging.warn("Position %s is not valid. Skipping move command.",
                                     mg_player_pos)
                        renpy.show("mg_player_confused",
                                   at_list=[minigame_player_pos(mg_player_x, mg_player_y)],
                                   tag="player",
                                   zorder=3)
                        renpy.pause(1.5 * persistent.mg_speed, hard=True)
                        continue

                    logging.info("New position set: %s", mg_player_pos)
                    mg_player_x, mg_player_y = matrix_to_scene(mg_player_pos, (mg_rows, mg_columns))
                    mg_preview_player_pos = mg_player_x, mg_player_y
                    renpy.show("mg_player_move",
                            at_list=[minigame_player_pos(mg_player_x, mg_player_y)],
                            tag="player",
                            zorder=3)

                # Turn on the device if available.
                elif current_instruction == "collect":
                    img_xpos, img_ypos = matrix_to_scene(mg_player_pos, (mg_rows, mg_columns))
                    renpy.hide("matrix_COIN_%s_%s" % (vm.get_position()))
                    renpy.show("mg_device_on",
                               at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                               tag="matrix_COIN_%s_%s" % (vm.get_position()))
                else:
                    pass

                renpy.pause(1.5 * persistent.mg_speed, hard=True)

        # Increase the return code if there's an issue.
        if "player-at-exit" in world.checks and mg_player_pos != mg_exit_pos:
            logging.warning("Check player-at-exit failed: %s (player) vs. %s (exit)",
                            mg_player_pos,
                            mg_exit_pos)
            mg_return_code = 1
        if ("player-collects-all" in world.checks or
            "player-powers-all-devices" in world.checks) and len(
                list(filter(lambda a: a is not None, vm.get_namespace("world_coins")))
            ) > 0:
            if "player-collects-all" in world.checks:
                logging.warning("Check player-collects-all is deprecated. Use %s instead.",
                                "player-powers-all-devices")
            logging.warning("Check player-collects-all failed: %s (world coins) vs. %s (inventory)",
                            vm.get_namespace("world_coins"),
                            vm.get_namespace("inventory"))
            mg_return_code = 1

        # Play the closing animations and re-enable the quick menu.
        if mg_return_code != 0:
            logging.warning("Not all checks succeeded. Marking minigame run as incomplete.")
            renpy.show("mg_player_cry",
                        at_list=[minigame_player_pos(mg_preview_player_pos[0],
                                                     mg_preview_player_pos[1])],
                        tag="player",
                        zorder=3)
        else:
            renpy.show("mg_player_happy",
                        at_list=[minigame_player_pos(mg_preview_player_pos[0],
                                                     mg_preview_player_pos[1])],
                        tag="player",
                        zorder=3)
        renpy.pause(1.5 * persistent.mg_speed, hard=True)
        quick_menu = allow_skipping = config.allow_skipping = True
    scene mg_bg with dissolve
    return
