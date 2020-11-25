#
# styles.rpy
# Unscripted Core - Settings UI
#
# Created by Marquis Kurt on 11/25/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

style pref_tab_group is hbox
style pref_tab_group_button is gui_button
style pref_tab_group_button_text is gui_text

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_text is gui_text
style pref_access_preview is gui_text
style pref_vbox is vbox
style pref_hbox is hbox

style pref_navigation_button is gui_button
style pref_navigation_button_text is gui_button_text

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

style link_vbox is pref_vbox
style link_label is pref_label
style link_label_text is pref_label_text
style link_button is gui_button
style link_button_text is gui_button_text

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

style pref_navigation_button_text:
    font AS_FONTS_DIR + "Medium.ttf"
    idle_color current_theme().colors().INTERFACE.value
    size 20

style pref_font_mwthr is radio_button
style pref_font_mwthr_text is radio_button_text:
    font "core/assets/fonts/merriweather/Merriweather-Regular.ttf"

style pref_font_mono is radio_button
style pref_font_mono_text is radio_button_text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"

style pref_font_opendys is radio_button
style pref_font_opendys_text is radio_button_text:
    font "core/assets/fonts/opendys/OpenDyslexic-Regular.otf"

style pref_font_deca is radio_button
style pref_font_deca_text is radio_button_text:
    font "core/assets/fonts/lexend/Deca-Regular.ttf"

style pref_font_exa is radio_button
style pref_font_exa_text is radio_button_text:
    font "core/assets/fonts/lexend/Exa-Regular.ttf"

style pref_font_giga is radio_button
style pref_font_giga_text is radio_button_text:
    font "core/assets/fonts/lexend/Giga-Regular.ttf"

style pref_font_mega is radio_button
style pref_font_mega_text is radio_button_text:
    font "core/assets/fonts/lexend/Mega-Regular.ttf"

style pref_font_peta is radio_button
style pref_font_peta_text is radio_button_text:
    font "core/assets/fonts/lexend/Peta-Regular.ttf"

style pref_font_tera is radio_button
style pref_font_tera_text is radio_button_text:
    font "core/assets/fonts/lexend/Tera-Regular.ttf"

style pref_font_zetta is radio_button
style pref_font_zetta_text is radio_button_text:
    font "core/assets/fonts/lexend/Zetta-Regular.ttf"

style check_vbox:
    spacing gui.pref_button_spacing

style slider_vbox:
    xsize 450

style pref_text:
    size 14
    color current_theme().colors().INTERFACE_SECONDARY.value

style standard_vbox:
    spacing gui.pref_button_spacing

style link_button:
    ymargin 0
    ypadding 0

style link_button_text:
    idle_color current_theme().colors().INTERFACE_ACTIVE.value
    font AS_FONTS_DIR + "Medium.ttf"
    size 16

style pref_access_preview is gui_text:
    font gui.preference("text_font")

style pref_tab_group_button is tab_group_button
style pref_tab_group_button_text is tab_group_button_text
