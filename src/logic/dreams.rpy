# 
# dreams.rpy
# Unscripted
# 
# Created by Marquis Kurt on 01/03/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 

init 10 python:
    def get_dreams():
        """Get all of the labels marked as Dreams.

        This works by effectively searching for scripts that start with
        'script_dream_'.
        """
        return filter(lambda label: label.startswith("script_dream_"),
                      renpy.get_all_labels())

# This is the bootstrap for a Dream. The Dreams screen calls this bootstrap
# to set up the dream so that developers do not need to write any pre-setup
# code to start the scene.
label dream_bootstrap(dream_label=None):
    stop music fadeout 2.0
    scene black with fade
    $ quick_menu = True
    call expression dream_label
    scene black with fade
    $ quick_menu = False
    call screen ASNotificationAlert("Dream Ended",
                                    "The following dream has ended. Thank you for participating.")
    return

screen dream_slots():
    default dreams_list = []

    python:
        dreams_list = get_dreams()

    use game_menu("Dreams"):

        hbox:
            style_prefix "dream_slot"

            xalign 0.5
            yalign 0.5
            box_wrap True

            spacing gui.slot_spacing

            if dreams_list:
            
                for dream in dreams_list:

                    python:
                        dream_name = dream.replace("script_dream_", "").replace("_", " ").title()
                        dream_file = dream.replace("script_", "")

                    button:
                        if dream:
                            action Function(renpy.call_in_new_context,
                                            "dream_bootstrap",
                                            dream_label=dream)
                        else:
                            action NullAction()

                        has vbox
                        
                        if dream:
                            add "gui/dreams/%s.png" % (dream_file,) xalign 0.5
                        else:
                            add "gui/saves/stateless.png" xalign 0.5

                        null height 4

                        text "[dream_name]":
                            style "slot_time_text"

            else:
                vbox:
                    xalign 0.5
                    yalign 0.5
                    yfill True
                    xmaximum 650

                    vbox:
                        yalign 0.5
                        spacing 8
                        add get_feather_icon("moon"):
                            size (84, 84)
                            xalign 0.5
                        null height 8
                        label "No Dreams Found":
                            style "dream_title"
                            xalign 0.5
                        text "Dreams are small modifications to Unscripted that allow you to play custom scenes. To add a dream, download one and place it in the dream folder of the game files.":
                            xalign 0.5
                            text_align 0.5
                            style "dream_text"

style dream_slot_button is slot_button:
    properties gui.button_properties("slot_button")
    background "gui/button/dream_slot_idle_background.png"

style dream_title is gui_label
style dream_title_text is gui_label_text:
    font AS_FONTS_DIR + "Bold.ttf"
style dream_text is gui_text:
    size 18
    color "#666666"