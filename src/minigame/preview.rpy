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
        from uvn_fira import CSWorldConfigBugType

        quick_menu = config.allow_skipping = allow_skipping = skipping = False
        floor_grid = []
        mg_return_code = 0
        mg_rows, mg_columns = world.data.to_grid().shape()
        mg_preview_player_pos = 0, 0
        mg_player_pos = world.data.to_grid().first("PLAYER")
        mg_exit_pos = world.data.to_grid().first("EXIT")
        _mg_bugs_list = world.bugs

        # Add the necessary casts and binds, if available.
        if not vm.is_interactive:
            vm.is_interactive = True

        if CSWorldConfigBugType.missing_bindings not in _mg_bugs_list:
            vm.input("bind poweron collect")
            vm.input("cast left west")
            vm.input("cast up north")
            vm.input("cast right east")
            vm.input("cast down south")
        vm.is_interactive = False

    # Start rendering the scene.
    scene mg_bg_alt with dissolve
    pause 0.5

    python:
        import logging
        element_image_names = {
            "WALL": "mg_wall",
            "DESK": "mg_device_off",
            "EXIT": "mg_exit",
            "PLAYER": "mg_player",
            "VOID": "mg_air"
        }

        random_seed = renpy.random.randint(1, 50)

        # Render a floor underneath the world grid, and then render the grid.
        for _r in range(mg_rows):
            for _c in range(mg_columns):
                element = world.data.to_grid().element_at(_r, _c)

                curr_tag = "matrix_base_%s_%s" % (_r, _c)
                floor_grid.append(curr_tag)
                img_xpos, img_ypos = matrix_to_scene((_r, _c), (mg_rows, mg_columns))
                use_alt_design = _c % 2 == 0

                _use_void = element == "VOID"
                _mg_img_name = "mg_air" if _use_void else ("mg_floor")

                renpy.show(_mg_img_name,
                           at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                           tag=curr_tag)

                img_name = element_image_names.get(element, "mg_air")

                if element == "WALL" and is_full_wall(world.data.to_grid().grid, (_r, _c)):
                    img_name += "_full"

                if element == "PLAYER":
                    mg_preview_player_pos = img_xpos, img_ypos

                if element == "EXIT":
                    img_name += "_" + stairway_type(world.data.walls().as_list(), (_r, _c))[0]

                if element == "AIR":
                    if random_seed >= 49:
                        img_name = "mg_beanbag"
                        element = "BEANBAG"

                curr_tag = "player" if element == "PLAYER" else "matrix_%s_%s_%s" \
                                        % (element, _r, _c)
                renpy.show(img_name,
                           at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                           tag=curr_tag,
                           zorder=3 if element == "PLAYER" else 2)

        renpy.show("mg_overlay", zorder=10)
        renpy.show("mg_compass", at_list=[compass_transform], zorder=11)

        # Pause before starting the VM execution.
        renpy.pause(1.5, hard=True)

        # Set up the initial state.
        _mg_states = MinigameStateManager(
            mg_player_pos,
            mg_exit_pos,
            0,
            len(world.data.devices().as_list())
        )

        # Run through the VM loop while there are still instructions.
        _mg_state = _mg_states.get_state()
        while vm.has_more_instructions():
            current_instruction = vm.preview_next_instruction()
            logging.info("Current instruction in VM stack: %s", current_instruction)
            vm.next()
            _mg_current_count = _mg_state.count

            # If the current instruction is a game-related instruction and not a VM management
            # command, play the required animations.
            if current_instruction not in ["alloc", "set", "push", "pop"]:
                mg_player_x, mg_player_y = matrix_to_scene(mg_player_pos, (mg_rows, mg_columns))
                if current_instruction == "move":
                    vx, vy = vm.get_position()
                    _reached_max = vx > _mg_rows - 1 or vy > _mg_columns - 1
                    _colliding = world.data.to_grid().element_at(vx, vy) in ["WALL", "VOID"]

                    # Display a confused animation if the player is in an invalid position.
                    if CSWorldConfigBugType.skip_collisions in _mg_bugs_list:
                        if _reached_max or _colliding:
                            logging.warn("Position %s is not valid. Skipping move command.",
                                        mg_player_pos)
                            renpy.show("mg_player_confused",
                                    at_list=[minigame_player_pos(mg_player_x, mg_player_y)],
                                    tag="player",
                                    zorder=3)
                            renpy.pause(1.5 * persistent.mg_speed, hard=True)
                            continue

                    mg_player_pos = vm.get_position()
                    logging.info("New position set: %s", mg_player_pos)
                    mg_player_x, mg_player_y = matrix_to_scene(mg_player_pos, (mg_rows, mg_columns))
                    mg_preview_player_pos = mg_player_x, mg_player_y

                    if CSWorldConfigBugType.skip_collisions in _mg_bugs_list\
                        and (_reached_max or _colliding):
                        renpy.show("effect glitch")
                    else:
                        renpy.hide("effect glitch")

                    renpy.show("mg_player_move",
                            at_list=[minigame_player_pos(mg_player_x, mg_player_y)],
                            tag="player",
                            zorder=3)

                # Turn on the device if available.
                elif current_instruction == "collect":
                    if mg_player_pos not in world.data.devices().as_list():
                        renpy.show("mg_player_confused",
                                   at_list=[minigame_player_pos(mg_player_x, mg_player_y)],
                                   tag="player",
                                   zorder=3)
                    else:
                        _mg_current_count += 1
                        img_xpos, img_ypos = matrix_to_scene(mg_player_pos, (mg_rows, mg_columns))
                        renpy.hide("matrix_DESK_%s_%s" % (vm.get_position()))
                        renpy.show("mg_device_on",
                                at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                                tag="matrix_DESK_%s_%s" % (vm.get_position()))
                else:
                    pass

                renpy.pause(1.5 * persistent.mg_speed, hard=True)

            _mg_states.update_state(mg_player_pos, _mg_current_count)
            _mg_state = _mg_states.get_state()

        # Increase the return code if there's an issue.
        if False in _mg_state.checks:
            logging.warning("Not all checks have passed. Last known state: %s",
                            _mg_state)
            mg_return_code += 1

        # Play the closing animations and re-enable the quick menu.
        if mg_return_code != 0:
            logging.warning("Marking minigame run as incomplete.")
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
