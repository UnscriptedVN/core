#
# quick.rpy
# Unscripted
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -1

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
            textbutton _("Glossary") action ShowTransient("GlossaryAppUIView")
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
    background Frame(current_theme().buttons(), gui.quick_button_borders, tile=gui.button_tile)

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    hover_color current_theme().colors().INTERFACE_HIGHLIGHT.value
    font AS_FONTS_DIR + "Regular.ttf"
