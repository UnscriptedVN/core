#
# inter.rpy
# Unscripted Core - Minigame (Interactive Mode)
#
# Created by Marquis Kurt on 07/21/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 10

# Composable screen element for the minigame buttons.
init screen mg_button(command, image_name):
    button action Return(command):
        xysize (96, 94)
        add MG_CONFIG["assets_path"] + "gui/" + image_name + ".png":
            size (96, 94)
            nearest True

# The screen to handle all input scenarios via GUI. Returns the command that the player submits to it.
init screen mg_interactive_buttons(last=""):
    tag minigame
    zorder 15
    modal True
    style_prefix "mg_inter"

    key "K_UP" action Return("move player north")
    key "K_LEFT" action Return("move player west")
    key "K_DOWN" action Return("move player south")
    key "K_RIGHT" action Return("move player east")
    key "g" action NullAction()
    key "d" action NullAction()

    key "p" action Return("collect")
    key "e" action Return("collect")

    if last:
        key "r" action Return(last)
        key "K_RETURN" action Return(last)
    else:
        key "K_RETURN" action NullAction()

    hbox:
        align (0.5, 0.95)
        xsize 1248
        xfill True

        vbox:
            xalign 0.15
            hbox:
                null width 96
                use mg_button("move player north", "move_up")
                null width 96
            hbox:
                use mg_button("move player west", "move_left")
                use mg_button("move player south", "move_down")
                use mg_button("move player east", "move_right")

        hbox:
            xalign 0.85
            use mg_button("collect", "poweron")
            # if last:
            #     use mg_button(last, "repeat")

# The screen to handle all input scenarios. Returns the command that the player submits to it.
init screen mg_interactive_input(last=""):
    tag minigame
    zorder 15
    modal True
    style_prefix "mg_inter"

    default repl_input = ""

    key "K_RETURN" action Return(repl_input)
    key "K_UP" action [SetScreenVariable("repl_input", last)]


    frame:
        xalign 0.5
        yalign 1.0
        xsize 600
        ysize 175

        vbox:
            yalign 0.0
            yfill True

            vbox:
                style_prefix "mg_inter_help"

                label "Cheat Sheet":
                    style "mg_inter_label"

                hbox:
                    label "move player <direction|cardinal>"
                    text "Moves Mia in a particular direction."
                hbox:
                    label "poweron"
                    text "Turns on a computer in Mia's position."
                hbox:
                    label "<NadiaVM expression>"
                    text "Evaluates the NadiaVM expression."
                hbox:
                    label "help"
                    text "Opens the NadiaVM reference book."

            hbox:
                yalign 1.0
                spacing 16

                text ">":
                    style "mg_inter_caret"
                input default "" length 64 value ScreenVariableInputValue("repl_input")

# Styles for input window.
style mg_inter_frame is frame:
    background Frame(gtheme("ruby-dark").colors().BACKGROUND.value + "CC", 8, 8, 8, 8, tile=False)
    margin (0, 0)
    padding (16, 10)

style mg_inter_text is text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"
    size 12
    color gtheme("ruby-dark").syntaxes().SOURCE_TEXT.value

style mg_inter_label_text is mg_inter_text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Bold.ttf"
    size 14
    color gtheme("ruby-dark").syntaxes().COMMENTS.value

style mg_inter_input is mg_inter_text:
    size 14
    color gtheme("ruby-dark").syntaxes().SOURCE_TEXT.value

style mg_inter_help_text is mg_inter_text

style mg_inter_help_label_text is mg_inter_label_text:
    size 12
    color gtheme("ruby-dark").syntaxes().KEYWORDS.value

style mg_inter_caret is mg_inter_help_label_text:
    color gtheme("ruby-dark").syntaxes().NUMBERS.value
    size 11

style mg_inter_window is window:
    background Frame("#00000015", 8, 8, 8, 8, tile=False)
    padding (8, 8)
    ysize 36

transform compass_transform:
    xalign 1.0
    yalign 0.0
    xoffset -16
    yoffset 16

# Interactive scene itself. Mostly derives from the preview scene with a few modifications.
label mg_interactive_experience(vm, world):
    window hide

    # Set up the environment based on the provided world data and the NadiaVM that we will read
    # instructions from.
    python:
        import logging
        from uvn_fira import CSWorldConfigBugType

        quick_menu = config.allow_skipping = allow_skipping = skipping = False
        _mg_floor_grid = []
        _mg_rows, _mg_columns = world.data.to_grid().shape()
        _mg_prev_player_pos = 0, 0
        _mg_player_pos = world.data.to_grid().first("PLAYER")
        _mg_exit_pos = world.data.to_grid().first("EXIT")
        _mg_current_command = None
        _mg_bugs_list = world.bugs
        _mg_last_command = ""

        # Add interactive capabilities.
        if not vm.is_interactive:
            logging.warn("VM interactivity was disabled. Adding interactive capabilities to VM...")
            vm.is_interactive = True

        if vm.has_more_instructions():
            logging.warning("VM already includes instructions. Clearing...")
            vm.clear()

        # Add the respective bindings, if the config allows it.
        if CSWorldConfigBugType.missing_bindings not in _mg_bugs_list:
            vm.input("bind poweron collect")
            vm.input("cast left west")
            vm.input("cast up north")
            vm.input("cast right east")
            vm.input("cast down south")

        _mg_devices = world.data.devices().as_list()

        # Add pre-existing commands.
        if len(_mg_devices) > 0:
            vm.input("alloc world_coins %s" % (len(_mg_devices)))
            vm.input("alloc inventory %s" % (len(_mg_devices)))

            for coin in _mg_devices:
                vm.input("set constant %s" % str(coin))
                vm.input("push world_coins %s" % _mg_devices.index(coin))

        # Execute all pre-loaded commands before starting.
        # while vm.has_more_instructions():
        #     vm.next()
        logging.info("Pre-populated VM with namespaces and commands.")
        logging.info("Current origin: %s.", world.data.to_grid().first("PLAYER"))

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

        # Set up default values for random seed generation and exit locations.
        _mg_exit_set = False
        random_seed = renpy.random.randint(1, 50)

        # Render a floor underneath the world grid, and then render the grid.
        for _r in range(_mg_rows):
            for _c in range(_mg_columns):
                element = world.data.to_grid().element_at(_r, _c)

                curr_tag = "matrix_base_%s_%s" % (_r, _c)
                _mg_floor_grid.append(curr_tag)
                img_xpos, img_ypos = matrix_to_scene((_r, _c), (_mg_rows, _mg_columns))
                use_alt_design = _c % 2 == 0

                _use_void = element == "VOID"
                _mg_img_name = "mg_air" if _use_void else ("mg_floor")

                renpy.show(_mg_img_name,
                           at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                           zorder=999,
                           tag=curr_tag)

                img_name = element_image_names.get(element, "mg_air")

                if element == "WALL" and is_full_wall(world.data.to_grid().grid, (_r, _c)):
                    img_name += "_full"

                if element == "PLAYER":
                    _mg_prev_player_pos = img_xpos, img_ypos

                # If the level's bugs don't include the exit, place it as-is.
                if element == "EXIT" and CSWorldConfigBugType.random_exit not in _mg_bugs_list\
                    and not _mg_exit_set:
                    img_name += "_" + stairway_type(world.data.walls().as_list(), (_r, _c))[0]
                    _mg_exit_set = True

                # Treat the exit as air if the random exit is a part of the bugs for this level.
                if element == "EXIT" and CSWorldConfigBugType.random_exit in _mg_bugs_list:
                    img_name = "mg_air"
                    element = "AIR"

                if element == "AIR":
                    if random_seed >= 49:
                        img_name = "mg_beanbag"
                        element = "BEANBAG"

                    # Randomly assign the location for the exit based on air blocks if the random
                    # exit is a part of the level's bugs.
                    elif not _mg_exit_set and (CSWorldConfigBugType.random_exit in _mg_bugs_list):
                        exit_seed = renpy.random.randint(1, 10)
                        _is_last_air_block = (_r, _c) == world.data.to_grid().last("AIR")
                        _is_even_seed = exit_seed % 2 == 0
                        if _is_last_air_block or _is_even_seed:
                            img_name = "mg_exit_" + stairway_type(
                                world.data.walls().as_list(),
                                (_r, _c)
                            )[0]
                            element = "EXIT"
                            _mg_exit_set = True
                            _mg_exit_pos = _r, _c

                curr_tag = "player" if element == "PLAYER" else "matrix_%s_%s_%s" \
                                        % (element, _r, _c)

                print("Now showing " + img_name)
                renpy.show(img_name,
                           at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                           tag=curr_tag,
                           zorder=3 if element == "PLAYER" else 2)

        renpy.show("mg_overlay", zorder=10)
        renpy.show("mg_compass", at_list=[compass_transform], zorder=11)

        # Pause before starting the VM execution.
        renpy.pause(1.5, hard=True)

        # Set up the state manager.
        _mg_state_manager = MinigameStateManager(
            _mg_player_pos,
            _mg_exit_pos,
            0,
            len(_mg_devices)
        )

        # Keep receiving instructions until the player has completed the map.
        _mg_state = _mg_state_manager.get_state()
        while False in _mg_state.checks:
            _mg_current_command = renpy.call_screen(
                "mg_interactive_input" if persistent.mg_adv_mode else "mg_interactive_buttons",
                last=_mg_last_command
            )
            _current_instruction = _mg_current_command.split(" ")[0]
            logging.info("VM received command: %s", _current_instruction)

            if _current_instruction == "help":
                logging.info("Help command detected. Opening reference page...")
                open_nvm_reference()
                continue

            _mg_binding = vm.get_binding(_current_instruction)
            _mg_current_count = _mg_state.count
            _mg_last_command = _mg_current_command
            if _mg_binding:
                logging.info("Note: %s is a binding of %s.", _current_instruction, _mg_binding)
                _current_instruction = _mg_binding.value
            try:
                _virtual = vm.test_input(_mg_current_command)
                _ret_stack = _virtual.get_vm_stack()
                logging.info("VM return stack: %s", _ret_stack)
            except Exception as error:
                _mg_player_x, _mg_player_y = matrix_to_scene(_mg_player_pos, (_mg_rows, _mg_columns))
                logging.error("Command %s failed. Reason: %s" % (_current_instruction, str(error)))
                renpy.show("mg_player_confused",
                            at_list=[minigame_player_pos(_mg_player_x, _mg_player_y)],
                            tag="player",
                            zorder=3)
                renpy.pause(1.5 * persistent.mg_speed, hard=True)
                continue
            renpy.show("mg_player",
                        at_list=[minigame_player_pos(_mg_prev_player_pos[0],
                                                    _mg_prev_player_pos[1])],
                        tag="player",
                        zorder=3)

            # If the current instruction is a game-related instruction and not a VM management
            # command, play the required animations.
            if _current_instruction not in ["alloc", "set", "push", "pop", "bind", "cast"]:
                _mg_player_x, _mg_player_y = matrix_to_scene(_mg_player_pos, (_mg_rows, _mg_columns))

                if _current_instruction == "move":
                    vx, vy = _virtual.get_position()
                    _reached_max = vx > _mg_rows - 1 or vy > _mg_columns - 1
                    _reached_min = vx < 0 or vy < 0
                    try:
                        _element_at = world.data.to_grid().element_at(vx, vy)
                        _colliding = _element_at in ["WALL", "VOID"]
                    except:
                        _reached_max = True
                        _colliding = True

                    # Display a confused animation if the player is in an invalid position.
                    if CSWorldConfigBugType.skip_collisions not in _mg_bugs_list:
                        if _reached_max or _reached_min or _colliding:
                            logging.warn("Position %s is not valid. Skipping move command.",
                                        (vx, vy))
                            renpy.show("mg_player_confused",
                                    at_list=[minigame_player_pos(_mg_player_x, _mg_player_y)],
                                    tag="player",
                                    zorder=3)
                            renpy.pause(1.5 * persistent.mg_speed, hard=True)
                            continue

                    vm.input(_mg_current_command)
                    _mg_player_pos = vm.get_position()
                    logging.info("New position set: %s", _mg_player_pos)
                    _mg_player_x, _mg_player_y = matrix_to_scene(
                        _mg_player_pos,
                        (_mg_rows, _mg_columns)
                    )
                    _mg_prev_player_pos = _mg_player_x, _mg_player_y

                    if CSWorldConfigBugType.skip_collisions in _mg_bugs_list\
                        and (_reached_max or _colliding):
                        renpy.show("effect glitch")
                    else:
                        renpy.hide("effect glitch")

                    renpy.show("mg_player_move",
                            at_list=[minigame_player_pos(_mg_player_x, _mg_player_y)],
                            tag="player",
                            zorder=3)

                # Turn on the device if available. Otherwise, display a confused look.
                elif _current_instruction == "collect":
                    if _mg_player_pos not in world.data.devices().as_list():
                        renpy.show("mg_player_confused",
                                   at_list=[minigame_player_pos(_mg_player_x, _mg_player_y)],
                                   tag="player",
                                   zorder=3)
                    else:
                        vm.input(_mg_current_command)
                        _mg_item_index = world.data.devices().as_list().index(_mg_player_pos)
                        if not vm.get_namespace("inventory")[_mg_item_index]:
                            _mg_current_count += 1
                            vm.input("pop world_coins %s" % _mg_item_index)
                            vm.input("push inventory %s" % _mg_item_index)

                        img_xpos, img_ypos = matrix_to_scene(_mg_player_pos, (_mg_rows, _mg_columns))
                        renpy.hide("matrix_DESK_%s_%s" % (vm.get_position()))
                        renpy.show("mg_device_on",
                                at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                                tag="matrix_DESK_%s_%s" % (vm.get_position()))
                elif _current_instruction == "exit":
                    if False in _mg_state.checks:
                        renpy.show("mg_player_cry",
                                    at_list=[minigame_player_pos(_mg_prev_player_pos[0],
                                                                _mg_prev_player_pos[1])],
                                    tag="player",
                                    zorder=3)
                else:
                    logging.warn("Command seems to have no effect.")
                    renpy.show("mg_player_confused",
                            at_list=[minigame_player_pos(_mg_player_x, _mg_player_y)],
                            tag="player",
                            zorder=3)
                    pass
                renpy.pause(1.5 * persistent.mg_speed, hard=True)
            else:
                vm.input(_mg_current_command)

            _mg_state_manager.update_state(_mg_player_pos, _mg_current_count)
            _mg_state = _mg_state_manager.get_state()
            logging.info("Current check state: %s", _mg_state)

        renpy.show("mg_player_happy",
                    at_list=[minigame_player_pos(_mg_prev_player_pos[0],
                                                 _mg_prev_player_pos[1])],
                    tag="player",
                    zorder=3)
        renpy.pause(1.5 * persistent.mg_speed, hard=True)
        quick_menu = allow_skipping = config.allow_skipping = True
    scene mg_bg with dissolve
    return
