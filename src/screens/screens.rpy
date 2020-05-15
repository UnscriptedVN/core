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
            xpos 80
            spacing 8
            if main_menu:
                textbutton _("Start") action Start()

            else:
                textbutton _("Chat History") action ShowMenu("history")
                textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")

            if main_menu:
                if uconf["features"]["enable_dreams"]:
                    textbutton _("Dreams") action ShowMenu("dreams")

                if uconf["analytics"]["enable_bug_reports"]:
                    textbutton _("Report a Bug") action Confirm("You are about to open the bug reporter\nin your web browser, which may collect data.\n\nAre you sure you want to continue?", yes=Function(open_issues_url))

            textbutton _("Settings") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)
            if renpy.variant("pc"):
                textbutton _("Help") action ShowMenu("help")

        hbox:
            xalign 0.8

            if not main_menu:
                textbutton _("Main Menu") action MainMenu()
            textbutton _("Quit") action Quit(confirm=not main_menu)
            textbutton _("Back to Game") action Return()
            if not main_menu:
                null width 24


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

    add "assets/gui/player.png":
        size (48, 48)
        xalign 1.0
        xoffset -16
        ypos 8

    add "assets/gui/icon.png":
        size (48, 48)
        xpos 16
        ypos 8

    use navigation

    label title

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


# MARK: Preferences

screen preferences():

    tag menu

    use game_menu(_("Settings"), scroll="viewport"):

        default settings_page = "general"
        vbox:
            xfill True

            hbox:
                style_prefix "pref_tab_group"
                xalign 0.5
                textbutton _("General") action SetScreenVariable("settings_page", "general")
                textbutton _("Sound") action SetScreenVariable("settings_page", "sound")
                textbutton _("Minigame") action SetScreenVariable("settings_page", "minigame")
                textbutton _("Accessibility") action SetScreenVariable("settings_page", "accessibility")
                textbutton _("Extras") action SetScreenVariable("settings_page", "extras")

            null height (4 * gui.pref_spacing)

            if settings_page == "general":
                use general_settings()
            elif settings_page == "sound":
                use sound_settings()
            elif settings_page == "minigame":
                use minigame_settings()
            elif settings_page == "accessibility":
                use accessibility_settings()
            elif settings_page == "extras":
                use extras_settings()
            else:
                text "The Settings page you requested doesn't exist.":
                    style "pref_text"

screen general_settings():
    style_prefix "pref"
    hbox:
        box_wrap True

        if renpy.variant("pc"):

            vbox:
                style_prefix "radio"
                label _("Display view:")
                textbutton _("As a window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

        vbox:
            style_prefix "radio"
            label _("When rolling back: ")
            textbutton _("Don't roll back") action Preference("rollback side", "disable")
            textbutton _("Roll to the left") action Preference("rollback side", "left")
            textbutton _("Roll to the right") action Preference("rollback side", "right")

        vbox:
            style_prefix "check"
            label _("When skipping, skip:")
            textbutton _("Unseen text") action Preference("skip", "toggle")
            textbutton _("After choices") action Preference("after choices", "toggle")
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

        vbox:
            style_prefix "slider"
            label "Automatic play"
            text "Automatic play allows you to play the game without needing to control it.":
                style "pref_text"

            label _("Text Speed")

            bar value Preference("text speed")

            $ cps = round(preferences.text_cps) or "max"
            text "About [cps] characters per second":
                style "pref_text"

            label _("Advance to the next line after:")

            bar value Preference("auto-forward time")

            $ afm_time = str(round(preferences.afm_time)) + " seconds" or "Don't auto-advance to the next line"
            text afm_time:
                style "pref_text"

        vbox:
            style_prefix "check"
            spacing 10
            vbox:
                textbutton _("Show save screenshots") action ToggleField(persistent, "use_detailed_saves")
                text "Show the screenshot from the moment of time in the save file instead of the chapter image.":
                    style "pref_text"
            vbox:
                textbutton _("Announce chapter names") action ToggleField(persistent, "announce_chapters")
                text "Show a toast with the chapter number and name when entering a new chapter.":
                    style "pref_text"

screen sound_settings():
    style_prefix "pref"
    hbox:
        style_prefix "slider"
        box_wrap True

        vbox:

            label "Sounds"

            if config.has_music:
                label _("Music Volume")

                hbox:
                    bar value Preference("music volume")

                $ music_vl = int(_preferences.get_volume('music') * 100)

                text "[music_vl]% volume":
                    style "pref_text"

            label _("Ambient Volume")

            hbox:
                bar value Preference("mixer ambient volume")

            $ ambient_vl = int(_preferences.get_volume('ambient') * 100)

            text "[ambient_vl]% volume":
                style "pref_text"

            if config.has_sound:

                label _("Sound Effects Volume")

                hbox:
                    bar value Preference("sound volume")

                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)
                $ sound_vl = int(_preferences.get_volume("sfx") * 100)
                text "[sound_vl]% volume":
                    style "pref_text"


            if config.has_voice:
                label _("Voice Volume")

                hbox:
                    bar value Preference("voice volume")

                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)


        vbox:

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Mute all sounds and music"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"

                textbutton _("Emphasize sound effects"):
                    action Preference("emphasize audio", "toggle")
                    style "mute_all_button"
                text "When enabled, the music volume will be adjusted so\nyou can hear sound effects and ambience more clearly.":
                    style "pref_text"

screen accessibility_settings():
    style_prefix "pref"
    hbox:
        box_wrap True

        vbox:
            style_prefix "check"
            label "Self-Voicing"
            textbutton "Use self voicing" action Preference("self voicing", "toggle")
            text "Self-voicing will read out the current\nline and any interface elements.":
                style "pref_text"

        vbox:
            label "Readability" style "check_label"
            textbutton "Use Lexend font" action gui.TogglePreference("text_font", "gui/font/lexend/" + lexend_font_name(persistent.lexend_width) + "-Regular.ttf", AS_FONTS_DIR + "Medium.ttf") style "check_button"
            text "Using Lexend may improve readability. Adjusting the width will require for this setting to be turned on again.":
                style "pref_text"

            label "Lexend Font Width" style "check_label"
            bar value FieldValue(persistent, "lexend_width", 6, max_is_zero=False, style="slider_slider", offset=1, step=1, action=None)

            $ lexend_font_width = lexend_font_name(persistent.lexend_width)
            text "Font width: [lexend_font_width]":
                style "pref_text"

    null height 76

    text "This is a preview of the font choice for the game.":
        style "pref_access_preview"
        xalign 0.5

screen minigame_settings():
    style_prefix "pref"

    hbox:
        box_wrap True
        spacing 10

        if uconf["features"]["enable_minigame_adv_mode"]:
            vbox:
                spacing 10
                vbox:
                    label "Game Mode"
                    vbox:
                        style_prefix "radio"
                        textbutton "Basic mode" action SetField(persistent, "mg_adv_mode", False)
                        text "Basic mode uses a GUI with buttons to solve puzzles. The GUI compiles the NadiaVM code for you.":
                            style "pref_text"
                        textbutton "Advanced mode" action SetField(persistent, "mg_adv_mode", True)
                        text "Advanced mode lets you write code to solve puzzles, either using the {a=https://fira.marquiskurt.net}Fira API{/a} and Python or another tool and NadiaVM.":
                            style "pref_text"
                    null height 2
                    if persistent.mg_adv_mode:
                        add "assets/gui/previews/mg_advanced.png"
                    else:
                        add "assets/gui/previews/mg_basic.png"

        vbox:
            label "Preview Animation Speed"
            text "When showing the code running step-by-step, run at the provided speed."

            vbox:
                style_prefix "radio"
                textbutton "Normal (1x)" action SetField(persistent, "mg_speed", 1.0)
                textbutton "Faster (~1.5x)" action SetField(persistent, "mg_speed", 0.75)
                textbutton "Fastest (~2x)" action SetField(persistent, "mg_speed", 0.5)
                textbutton "Warp Speed (~10x)" action SetField(persistent, "mg_speed", 0.1)

        vbox:
            style_prefix "check"
            label "Basic Editor"
            vbox:
                spacing 10
                vbox:
                    textbutton "Reduce spacing in VM input" action ToggleField(persistent, "mg_condensed_font")
                    text "Enabling this option will reduce the spacing between commands in the VM preview pane in Basic Mode.":
                        style "pref_text"
                vbox:
                    textbutton "Show hidden VM commands" action ToggleField(persistent, "mg_vm_show_all")
                    text "Enabling this option will show all virtual machine commands in the VM preview pane.":
                        style "pref_text"

        vbox:
            label "Advanced"

            vbox:
                spacing 10
                vbox:
                    style_prefix "check"
                    textbutton "Force Python compiler" action ToggleField(persistent, "mg_vm_force_editor")
                    text "Show the editor preview and compile using Python, even if VM code exists.":
                        style "pref_text"
                vbox:
                    style_prefix "standard"
                    textbutton "Open Scripts Folder" action Function(open_directory, config.savedir + "/minigame")
                    text "Save directory: " + config.savedir + "/minigame":
                        style "pref_text"
                vbox:
                    style_prefix "standard"
                    textbutton "Documentation" action Function(open_api_docs)
                    text "Documentation is also available in Help.":
                        style "pref_text"

screen extras_settings():
    style_prefix "pref"
    hbox:
        box_wrap True
        spacing 8

        vbox:
            style_prefix "check"
            label "Rich Presence"

            python:
                import os
                def reset_game():
                   persistent._clear(progress=True)
                   renpy.utter_restart()

            if uconf["discord"]["enable_rpc"]:
                textbutton _("Enable Discord Presence") action ToggleField(persistent, "use_discord")
                text "When Discord is open and rich presence is enabled, Unscripted will connect and display information when playing.\n\nChanges to this setting apply upon restarting.":
                    style "pref_text"

        vbox:
            style_prefix "standard"

            label "Advanced"
            textbutton "Manage app permissions" action Function(appManager.applicationWillLaunch)
            text "Clicking this button will open AliceOS's App Manager and let you manage permissions of apps in-game.":
                style "pref_text"

            null height 8

            textbutton "Open Logs" action Function(open_uvn_log)
            text "Clicking this button will open the Unscripted logs, which may be useful for troubleshooting.":
                style "pref_text"

style pref_tab_group is hbox
style pref_tab_group_button is gui_button
style pref_tab_group_button_text is gui_text

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_text is gui_text
style pref_access_preview is gui_text
style pref_vbox is vbox
style pref_hbox is hbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style standard_label is pref_label
style standard_label_text is pref_label_text
style standard_button is gui_button
style standard_button_text is gui_button_text
style standard_vbox is pref_vbox

style pref_tab_group is hbox:
    background Frame("gui/tab_group_frame.png", 16, 2, 16, 2, tile=False)

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2
    font AS_FONTS_DIR + "Medium.ttf"

style pref_label_text:
    font AS_FONTS_DIR + "Medium.ttf"
    size 20
    yalign 1.0

style pref_vbox:
    xsize 275

style pref_hbox:
    spacing gui.pref_button_spacing

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    color gui.interface_text_color
    hover_color gui.hover_color
    size 18

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    color gui.interface_text_color
    hover_color gui.hover_color
    size 18

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

style pref_text:
    size 14
    color "#999999"

style standard_button:
    properties gui.button_properties("quick_button")

style standard_button_text:
    properties gui.button_text_properties("quick_button")
    size 12

style standard_vbox:
    spacing gui.pref_button_spacing

style pref_access_preview is gui_text:
    font gui.preference("text_font")

style pref_tab_group_button is gui_button:
    background Frame("gui/button/tab_group_[prefix_]background.png", Borders(16, 4, 16, 4), tile=False)
    xpadding 24
    ypadding 20

style pref_tab_group_button_text is gui_button_text:
    color "#ffffff"
    selected_font AS_FONTS_DIR + "Medium.ttf"
    size 16


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

# MARK: Help

screen help():

    tag menu

    default tab = "about"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:
                xalign 0.5
                style_prefix "pref_tab_group"

                textbutton _("About") action SetScreenVariable("tab", "about")
                textbutton _("License") action SetScreenVariable("tab", "license")
                if uconf["features"]["enable_minigame_adv_mode"]:
                    textbutton _("Documentation") action Function(open_api_docs)
                textbutton _("Keyboard") action SetScreenVariable("tab", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("tab", "mouse")
                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("tab", "gamepad")

            use expression tab + "_help"

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "D"
        text _("Opens the AliceOS Desktop.")

    hbox:
        label "E"
        text _("Opens the inventory HUD.")

    hbox:
        label "L"
        text _("Opens the Unscripted log file.")

    hbox:
        label "Shift + B"
        text _("Opens the bug reporter.")

screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()

screen license_help():

    default license = ""

    python:
        with renpy.file("../LICENSE.txt") as file:
            # license = """"""
            # for line in file:
            #     if not line.startswith("//"):
            #         license = license + line
            license = file.read()

    hbox:

        label "License"
        text "[license]":
            style "help_license_text"

screen about_help():
    hbox:
        xalign 0.5
        spacing 4
        add "gui/icon.png":
            size (64, 64)
        text "Unscripted":
            font "gui/font/lexend/Deca-Regular.ttf"
            size 64
    text "A visual novel about software development":
        xalign 0.5
        text_align 0.5
    null height 16
    hbox:
        label "Game Version"
        text "[config.version]"
    hbox:
        $ _cv = uconf["features"]["channel"]
        label "Release Channel"
        text "[_cv!c] %s"  % ("(demo)" if uconf["demo"]["demo"] else "")
    hbox:
        python:
            import uvn_fira
            _fv = uvn_fira.__version__
        label "Fira API Version"
        text "[_fv]"
    hbox:
        label "AliceOS Version"
        text "[AS_SYS_INFO[COMMON_NAME]] ([AS_SYS_INFO[VERSION]]) [AS_SYS_INFO[BUILD_ID]]"
    hbox:
        $ _rv = renpy.version().replace("Ren'Py", "")
        label "Ren'Py Version"
        text "[_rv]"

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_vbox is gui_vbox

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
    font AS_FONTS_DIR + "Bold.ttf"

style help_text is gui_text:
    size gui.text_size

style help_license_text is help_text:
    font "gui/font/JetBrainsMono-Regular.ttf"
    size 16

style help_small_text is help_text:
    size 16
    color "#666666"

style help_vbox is gui_vbox:
    xfill True

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




