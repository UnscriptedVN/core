#
# inter.rpy
# Unscripted Core - Minigame (Interactive Mode)
#
# Created by Marquis Kurt on 07/21/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#

init offset = 10

# The screen to handle all input scenarios. Returns the command that the player submits to it.
init screen mg_interactive_input():
    tag minigame
    zorder 15
    modal True
    style_prefix "mg_inter"

    default repl_input = ""

    key "K_RETURN" action Return(repl_input)

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
                    label "move player <direction>"
                    text "Moves Mia in a particular direction."
                hbox:
                    label "poweron"
                    text "Turns on a computer in Mia's position."
                hbox:
                    label "<NadiaVM expression>"
                    text "Evaluates the NadiaVM expression."

            hbox:
                yalign 1.0
                spacing 16

                text ">":
                    style "mg_inter_caret"
                input default "" length 64 value ScreenVariableInputValue("repl_input")

# Styles for input window.
style mg_inter_frame is frame:
    background Frame(current_theme().colors().BACKGROUND.value + "32", 8, 8, 8, 8, tile=False)
    margin (0, 0)
    padding (16, 10)

style mg_inter_text is text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"
    size 12
    color current_theme().syntaxes().SOURCE_TEXT.value

style mg_inter_label_text is mg_inter_text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Bold.ttf"
    size 14
    color current_theme().syntaxes().COMMENTS.value

style mg_inter_input is mg_inter_text:
    size 14
    color current_theme().syntaxes().SOURCE_TEXT.value

style mg_inter_help_text is mg_inter_text

style mg_inter_help_label_text is mg_inter_label_text:
    size 12
    color current_theme().syntaxes().KEYWORDS.value

style mg_inter_caret is mg_inter_help_label_text:
    color current_theme().syntaxes().NUMBERS.value
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
        quick_menu = config.allow_skipping = allow_skipping = skipping = False
        floor_grid = []
        mg_rows, mg_columns = world.data.to_grid().shape()
        mg_preview_player_pos = 0, 0
        mg_player_pos = world.data.to_grid().first("PLAYER")
        mg_exit_pos = world.data.to_grid().first("EXIT")
        _mg_current_command = None

        def _player_arrived():
            """Returns whether the player is at the exit."""
            return mg_player_pos == mg_exit_pos

        def _player_powered_all():
            """Returns whether the player has powered on all devices."""
            is_none = lambda a: a is not None
            all_devices = list(filter(is_none, vm.get_namespace("world_coins")))
            return len(all_devices) <= 0

        # Add interactive capabilities.
        if not vm.is_interactive:
            logging.warn("VM interactivity was disabled. Adding interactive capabilities to VM...")
            vm.is_interactive = True

        if vm.has_more_instructions():
            logging.warning("VM already includes instructions. Clearing...")
            vm.clear()

        # Add pre-existing commands.
        _mg_devices = world.data.devices().as_list()
        if len(_mg_devices) > 0:
            vm.input("alloc world_coins %s" % (len(_mg_devices)))
            vm.input("alloc inventory %s" % (len(_mg_devices)))

            for coin in _mg_devices:
                vm.input("set constant %s" % str(coin))
                vm.input("push world_coins %s" % _mg_devices.index(coin))

        # Execute all pre-loaded commands before starting.
        while vm.has_more_instructions():
            vm.next()
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
                    mg_preview_player_pos = img_xpos, img_ypos

                if element == "EXIT":
                    img_name += "_" + stairway_type(world.data.walls().as_list(), (_r, _c))[0]
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

        # Keep receiving instructions until the player has completed the map.
        state = [_player_arrived(), _player_powered_all()]
        while False in state:
            _mg_current_command = renpy.call_screen("mg_interactive_input")
            current_instruction = _mg_current_command.split(" ")[0]
            logging.info("VM received command: %s", current_instruction)
            _mg_binding = vm.get_binding(current_instruction)
            if _mg_binding:
                logging.info("Note: %s is a binding of %s.", current_instruction, _mg_binding)
                current_instruction = _mg_binding
            try:
                _ret_stack = vm.input(_mg_current_command)
                logging.info("VM return stack: %s", _ret_stack)
            except:
                logging.error("Command %s failed." % (current_instruction))
                renpy.show("mg_player_confused",
                            at_list=[minigame_player_pos(mg_player_x, mg_player_y)],
                            tag="player",
                            zorder=3)
                renpy.pause(1.5 * persistent.mg_speed, hard=True)
                continue
            renpy.show("mg_player",
                        at_list=[minigame_player_pos(mg_preview_player_pos[0],
                                                    mg_preview_player_pos[1])],
                        tag="player",
                        zorder=3)

            # If the current instruction is a game-related instruction and not a VM management
            # command, play the required animations.
            if current_instruction not in ["alloc", "set", "push", "pop", "bind", "cast"]:
                mg_player_x, mg_player_y = matrix_to_scene(mg_player_pos, (mg_rows, mg_columns))

                if current_instruction == "move":
                    vx, vy = vm.get_position()

                    # Display a confused animation if the player is in an invalid position.
                    if vx > mg_rows - 1 or vy > mg_columns - 1 \
                        or world.data.to_grid().element_at(vx, vy) == "WALL":
                        logging.warn("Position %s is not valid. Skipping move command.",
                                     (vx, vy))
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
                    renpy.show("mg_player_move",
                            at_list=[minigame_player_pos(mg_player_x, mg_player_y)],
                            tag="player",
                            zorder=3)

                # Turn on the device if available. Otherwise, display a confused look.
                elif current_instruction == "collect":
                    if mg_player_pos not in world.data.devices().as_list():
                        renpy.show("mg_player_confused",
                                   at_list=[minigame_player_pos(mg_player_x, mg_player_y)],
                                   tag="player",
                                   zorder=3)
                    else:
                        _mg_item_index = world.data.devices().as_list().index(mg_player_pos)
                        vm.input("pop world_coins %s" % _mg_item_index)
                        vm.input("push inventory %s" % _mg_item_index)

                        img_xpos, img_ypos = matrix_to_scene(mg_player_pos, (mg_rows, mg_columns))
                        renpy.hide("matrix_DESK_%s_%s" % (vm.get_position()))
                        renpy.show("mg_device_on",
                                at_list=[minigame_matrix_pos(img_xpos, img_ypos)],
                                tag="matrix_DESK_%s_%s" % (vm.get_position()))
                elif current_instruction == "exit":
                    if False in state:
                        renpy.show("mg_player_cry",
                                    at_list=[minigame_player_pos(mg_preview_player_pos[0],
                                                                mg_preview_player_pos[1])],
                                    tag="player",
                                    zorder=3)
                else:
                    logging.warn("Command seems to have no effect.")
                    pass
                renpy.pause(1.5 * persistent.mg_speed, hard=True)

            state = [_player_arrived(), _player_powered_all()]
            logging.info("Current check state: %s", state)

        renpy.show("mg_player_happy",
                    at_list=[minigame_player_pos(mg_preview_player_pos[0],
                                                 mg_preview_player_pos[1])],
                    tag="player",
                    zorder=3)
        renpy.pause(1.5 * persistent.mg_speed, hard=True)
        quick_menu = allow_skipping = config.allow_skipping = True
    scene mg_bg with dissolve
    return
