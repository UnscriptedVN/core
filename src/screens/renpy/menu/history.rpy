#
# history.rpy
# Unscripted Core - Screens (History)
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

screen history():
    tag menu
    predict False

    use game_menu(_("Chat History"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"

        for h in _history_list:
            window:
                has fixed:
                    yfit True

                if h.who:
                    if get_history_name(h.who) != "player":
                        add "gui/history/" + get_history_name(h.who) + ".png":
                            xpos gui.history_name_xpos
                            zoom 0.8
                        text h.what
                    else:
                        text h.what:
                            text_align 1.0
                            xalign 0.9
                        add "gui/history/" + get_history_name(h.who) + ".png":
                            xalign 1.0
                            zoom 0.8
                else:
                    window:
                        style "history_narrative_box"
                        xalign 0.5

                        has hbox:
                            spacing 16

                            text h.what:
                                style "history_narrative_text"
                                xmaximum 700
                                text_align 0.5

        if not _history_list:
            label _("The chat history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_narrative_text is gui_text:
    size 18
    color gui.insensitive_color
    xalign 0.5

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    # xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

style history_narrative_box:
    background Frame(current_theme().frames().NARRATIVE.value, 32, 32, 32, 32, tile=False)
    padding (16, 8)
