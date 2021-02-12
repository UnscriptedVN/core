#
# submit.rpy
# Unscripted
#
# Created by Marquis Kurt on 11/30/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen asc_submit():
    tag asc
    style_prefix "asc"
    zorder 100
    modal True

    add current_theme().overlays().GAME.value

    frame:
        xfill True
        yfill True

        has vbox:
            hbox:
                yoffset -16
                spacing 16
                xfill True

                text "PackStore Factory":
                    style "asc_name"

                hbox:
                    xalign 0.5
                    spacing 10
                    text "Software"
                    text "Analytics"
                    text "Trends"
                    text "Sales Reports"
                    text "Agreements"

                hbox:
                    xalign 1.0
                    text "[player.name]"

            hbox:
                xfill True
                spacing 4
                yoffset 24
                hbox:
                    spacing 8
                    add "core/assets/minigame/elements/compass.png":
                        size (38, 38)
                    text "Command Escape":
                        style "asc_game_title"
                hbox:
                    xalign 1.0
                    style_prefix "standard"

                    textbutton "Submit for Review" action Confirm("Are you sure you want to submit this game for review?\nChanges cannot be made to the game until it has been reviewed.", Return(0))
            vbox:
                yoffset 32
                style_prefix "asc_detail"
                xfill True
                hbox:
                    vbox:

                        label "Game Preview"
                        add "images/cg/cg3/fg2.png" size (400, 225)

                        label "Game Author"
                        text "[player.name]"

                        label "Game Genre"
                        text "Puzzle"

                        label "Game Description"
                        text "Command Escape is an intriguing puzzle game in similar styles to Sokoban. You play as Mia, a colorful software engineer at Technology Plus Labs, as you look around the offices and find out where everybody went."
                    vbox:
                        $ __pname = player.name.replace(" ", "_").lower()
                        label "Game Bundle Identifier"
                        text "net.[__pname].command_escape"

                        label "Game Bundle Hash"
                        text "c7db138c6110a72b0b89582891874b9d":
                            style "asc_detail_mono_text"

                        label "PackStore SDK Version"
                        text "6.0":
                            style "asc_detail_mono_text"

                        label "Game Target"
                        text "MULTI":
                            style "asc_detail_mono_text"

                        label "Entitlements Present"
                        text "Yes"
                    vbox:
                        $ __fdir = get_font("Interface", variant="Bold")
                        label "Achievements"
                        text "{font=[__fdir]}Completionist (50){/font} - Complete the game."

                        label "Leaderboards"
                        text "None provided."

                        null height 16

                        label "Pricing Availability"
                        text "Paid - ($4.99)"

                        label "Includes In-app Purchases"
                        text "No"

style asc_frame is gui_frame:
    background None

style asc_text is gui_text:
    size 16

style asc_label is gui_label

style asc_label_text is gui_label_text:
    font get_font("Interface", variant="Bold")
    size 18

style asc_name is gui_text:
    font get_font("Interface", variant="Bold")
    size 18

style asc_game_title is gui_text:
    font get_font("Interface", variant="Bold")
    size 32

style asc_detail_hbox is gui_hbox:
    spacing 16

style asc_detail_vbox is gui_vbox:
    xsize 400
    spacing 10

style asc_detail_label is asc_label
style asc_detail_label_text is asc_label_text
style asc_detail_text is asc_text

style asc_detail_mono_text is asc_detail_text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"
