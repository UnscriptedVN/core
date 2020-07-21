#
# inter.rpy
# Unscripted Core - Minigame (Interactive Mode)
#
# Created by Marquis Kurt on 07/21/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#

init offset = 10

init screen mg_interactive_input():
    tag minigame
    zorder 15
    modal True
    style_prefix "mg_inter"

    default repl_input = ""

    key "K_RETURN" action Return(repl_input)

    frame:
        xalign 0.5
        yalign 0.9
        xsize 600
        ysize 64

        window:
            hbox:
                yalign 0.5
                input default "" length 64 value ScreenVariableInputValue("repl_input")

style mg_inter_input is input:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"
    size 18
    color current_theme().syntaxes().SOURCE_TEXT.value

style mg_inter_window is window:
    background Frame("#00000015", 8, 8, 8, 8, tile=False)
    padding (8, 8)
    ysize 36
