#
# io.rpy
# Unscripted Core - Screens (I/O, Files, Dreams)
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

screen dreams():
    tag menu
    use dream_slots()

screen save():
    tag menu
    use file_slots(_("Save"))


screen load():
    tag menu
    use file_slots(_("Load"))


# MARK:  File Slot
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        fixed:
            order_reverse True

            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    python:
                        chapter = FileJson(slot, key="chapter_name")
                        save_name = "gui/saves/" + (chapter.lower() if chapter is not None else "stateless") + ".png"
                        saved_player_instance = FileJson(slot, key="player")

                        if saved_player_instance:
                            player_name = saved_player_instance["name"]
                        else:
                            player_name = None

                    button:
                        action FileAction(slot)

                        has vbox:

                            if persistent.use_detailed_saves:
                                add FileScreenshot(slot) xalign 0.5
                            else:
                                add save_name xalign 0.5
                            null height 4

                            hbox:
                                xfill True
                                spacing 4
                                vbox:
                                    xalign 0.0
                                    text "%s, %s" % (player_name or "Foo Bar", FileJson(slot, key="chapter_name") or "Stateless"):
                                        style "slot_name_text"

                                    text FileTime(slot, format=_("{#file_time}%B %d, %Y at %H:%M"), empty=_("Empty Project")):
                                        style "slot_time_text"

                                if FileLoadable(slot):
                                    button action FileDelete(slot):
                                        background None
                                        xalign 1.0
                                        xysize (32, 32)
                                        padding (2, 2)

                                        has vbox:
                                            add get_feather_icon("trash"):
                                                size (28, 28)

                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.95

                spacing gui.page_spacing

                textbutton _("‹ Previous Page") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

#                 ## range(1, 10) gives the numbers from 1 to 9.
#                 for page in range(1, 10):
#                     textbutton "[page]" action FilePage(page)

                textbutton _("Next Page ›") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 8

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    idle_color current_theme().colors().INTERFACE.value
    size 18

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

style slot_name_text is slot_button_text:
    font AS_FONTS_DIR + "Bold.ttf"
    idle_color current_theme().colors().INTERFACE.value

style slot_time_text is slot_button_text:
    idle_color current_theme().colors().INTERFACE_SECONDARY.value
