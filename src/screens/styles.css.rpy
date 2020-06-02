#
# styles.css.rpy
# Unscripted Core
#
# Created by Marquis Kurt on 04/24/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

style default:
    properties gui.text_properties()
    language gui.language

style normal is default:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style python is default:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"
    color "#FFE873"
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    text_align gui.dialogue_text_xalign

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=False)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame(current_theme().bars().LEFT.value, gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame(current_theme().bars().RIGHT.value, gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame(current_theme().bars().TOP.value, gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame(current_theme().bars().BOTTOM.value, gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame(current_theme().scrollbars().HORIZONTAL.value, gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(current_theme().scrollbars().HORIZONTAL_THUMB.value, gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame(current_theme().scrollbars().VERTICAL.value, gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(current_theme().scrollbars().VERTICAL_THUMB.value, gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame(current_theme().sliders().HORIZONTAL.value, gui.slider_borders, tile=gui.slider_tile)
    thumb current_theme().sliders().HORIZONTAL_THUMB.value

style vslider:
    xsize gui.slider_size
    base_bar Frame(current_theme().sliders().VERTICAL.value, gui.vslider_borders, tile=gui.slider_tile)
    thumb current_theme().sliders().VERTICAL_THUMB.value

style frame:
    padding gui.frame_borders.padding
    background Frame(current_theme().frames().BASIC.value, gui.frame_borders, tile=gui.frame_tile)

style radio_button:
    properties gui.button_properties("radio_button")
    foreground current_theme().radios().FOREGROUND.value

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    color gui.interface_text_color
    hover_color gui.hover_color
    size 18

style check_button:
    properties gui.button_properties("check_button")
    foreground current_theme().checkboxes().FOREGROUND.value

style check_button_text:
    properties gui.button_text_properties("check_button")
    color gui.interface_text_color
    hover_color gui.hover_color
    size 18

style standard_button:
    properties gui.button_properties("quick_button")
    background Frame(current_theme().buttons(), gui.button_borders, tile=gui.button_tile)

style standard_button_text:
    properties gui.button_text_properties("quick_button")
    hover_color current_theme().colors().INTERFACE_HIGHLIGHT.value
    size 12

style tab_group_button is gui_button:
    background Frame(current_theme().tabs(), Borders(16, 4, 16, 4), tile=False)
    xpadding 24
    ypadding 20

style tab_group_button_text is gui_button_text:
    color current_theme().colors().INTERFACE.value
    selected_font AS_FONTS_DIR + "Medium.ttf"
    size 16

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")
