#
# screens.rpy
# Unscripted
#
# Created by Marquis Kurt on 07/01/19.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

init -1 python:
    import webbrowser
    import logging

    def open_api_docs():
        """Open the API documentation for Advanced Mode of the minigame."""
        url = "file://" + config.basedir + "/game/docs/index.html"
        webbrowser.open(url)
        renpy.notify("The documentation has been opened in your browser.")

# MARK: Say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"


        if who is not None:

            window:
                style "namebox"
                hbox:
                    spacing 8
                    add "gui/history/" + get_history_name(who) + ".png":
                        size (24, 24)
                        xalign 0.0

                    text who id "who"

        text what id "what"

    if quick_menu:
        use quick_menu

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0, yoffset=4)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=False)
    xalign gui.name_xalign
    yalign 0.5
    color gui.text_color
    size 20

style say_dialogue is normal

# MARK: Input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


# MARK: Choice

default choice_timeout = None

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            if i.caption:
                textbutton i.caption action i.action

    if choice_timeout:
        timer choice_timeout action [Function(logging.warn, "Choice timed out. Selecting last choice automatically."),
                                     Return(len(items) - 1)]


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


# MARK: Quick menu
screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.965
            spacing 8

            if config.developer:
                textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Use Item") action ShowTransient("InventoryHUD")
            textbutton _("Desktop") action ShowTransient("ASDesktopShellView")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Settings") action ShowMenu('preferences')
            key "e" action ShowTransient("InventoryHUD")

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")


style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font AS_FONTS_DIR + "Regular.ttf"


# MARK: Navigation

screen navigation():

    hbox:
        style_prefix "navigation"
        xfill True
        ypos 12

        hbox:
            xpos 24
            spacing 8

            button action Return():
                style "navigation_icon_button"
                add get_feather_icon("arrow-left"):
                    size (28, 28)

            if main_menu:
                textbutton _("Start") action Start()

            else:
                textbutton _("Chat History") action ShowMenu("history")
                textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")

            if main_menu:
                if uconf["features"]["enable_dreams"]:
                    textbutton _("Dreams") action ShowMenu("dreams")

            textbutton _("Settings") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)
            if renpy.variant("pc"):
                textbutton _("Help") action ShowMenu("help")

        hbox:
            xalign 1.0
            xoffset -24
            spacing 8

            if uconf["analytics"]["enable_bug_reports"]:
                button action Confirm("You are about to open the bug reporter\nin your web browser, which may collect data.\n\nAre you sure you want to continue?", yes=Function(open_issues_url)):
                    style "navigation_icon_button"
                    add get_feather_icon("message-square"):
                        size (28, 28)

            if not main_menu:
                button action MainMenu():
                    style "navigation_icon_button"
                    add get_feather_icon("log-out"):
                        size (28, 28)

            button action Quit(confirm=not main_menu):
                style "navigation_icon_button"
                add get_feather_icon("power"):
                    size (28, 28)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    # size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font AS_FONTS_DIR + "medium.ttf"
    color "#ffffff"
    hover_color "#05C1FD"
    size 16
    text_align 0.0

style navigation_icon_button is gui_button:
    hover_background gui.accent_color + "20"

# MARK: Game menu

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    # if main_menu:
    #     add gui.main_menu_background
    # else:
    add "gui/overlay/game_menu.png"

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    label title

    hbox:
        yalign 1.0
        yoffset -16
        xoffset 16
        spacing -8

        add "assets/gui/icon.png":
            size (32, 32)

        $ _channel = uconf["features"]["channel"]
        text "[config.name!t] v[config.version]. Release channel: [_channel]\n© 2020 Marquis Kurt. All rights reserved."

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_text is gui_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    # background "gui/overlay/game_menu.png"

style game_menu_content_frame:
    # background Frame("gui/game_menu_content_frame.png", gui.frame_borders, gui.frame_tile)
    left_margin 16
    right_margin 16
    top_padding 24
    bottom_padding 8
    left_padding 8
    right_padding 8
    xfill True

style game_menu_viewport:
    xsize 1216
    xoffset 16

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 32
    ypos 80

style game_menu_text:
    xpos 32
    yalign 0.975
    size 12
    color "#f4f4f4"

style game_menu_label_text:
    font AS_FONTS_DIR + "Bold.ttf"
    color "#f4f4f4"
    yalign 0.5
    size 32

# MARK: About

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


# MARK: Load/Save

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

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
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

            ## Buttons to access other pages.
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
    size 18

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

style slot_name_text is slot_button_text:
    font AS_FONTS_DIR + "Bold.ttf"
    idle_color "#f4f4f4"

# MARK: History
screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("Chat History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
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
    background Frame("assets/gui/narrative_bubble.png", 32, 32, 32, 32, tile=False)
    padding (16, 8)

# MARK: Confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    size 20
    font AS_FONTS_DIR + "Medium.ttf"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    size 16
    font AS_FONTS_DIR + "Medium.ttf"



# MARK: Skip

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    xpos gui.skip_xpos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size
    color "#ffffff"

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


# MARK: Notify

default notify_timeout = 3.25

screen notify(message):

    zorder 500
    style_prefix "notify"

    frame at notify_appear:
        text message

    if notify_timeout:
        timer notify_timeout action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    xpos gui.notify_xpos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    color "#ffffff"


# MARK: NVL


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



# MARK: Mobile Variants
style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
