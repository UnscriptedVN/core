#
# changes.rpy
# Unscripted Core - What's New Screen
#
# Created by Marquis Kurt on 08/08/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

screen changelog(version):
    zorder 100
    modal True
    tag changelog
    style_prefix "changelog"

    on "show":
        action [
                Function(SetThumbnailFull),
                FileTakeScreenshot(),
                Function(SetThumbnailOriginal)
                ]

    add FileCurrentScreenshot():
        blur CABlurType["default"]
    add "#000000CC"

    frame at ASDynamicBlurTransition:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 8


            if wicon:
                add wicon:
                    size (76, 76)
                    xalign 0.5

            $ _ver, _notes = version
            label "What's New in [_ver]":
                xalign 0.5
            viewport id "changelog_vp":
                scrollbars "vertical"
                mousewheel True
                style "changelog_viewport"

                vbox:
                    spacing 8
                    for note in _notes:
                        text "• [note]"
            textbutton "Got it" action [Function(did_view_changelog), Hide("changelog")]:
                xalign 0.5

style changelog_frame is gui_frame:
    xalign 0.5
    yalign 0.5
    xmaximum 625
    ymaximum 625
    padding (20, 20)

style changelog_label is gui_label
style changelog_label_text is gui_label_text:
    font AS_FONTS_DIR + "Bold.ttf"

style changelog_text is gui_text:
    size 16

style changelog_button is standard_button

style changelog_button_text is standard_button_text:
    font AS_FONTS_DIR + "Medium.ttf"
    size 14

style changelog_viewport is gui_viewport:
    yfill False
    yfit False
    ymaximum 400

style changelog_scrollbar is scrollbar:
    unscrollable "hide"
