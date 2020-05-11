#
# styles.css.rpy
# Unscripted Core - Credits (Styles)
#
# Created by Marquis Kurt on 04/14/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 5

style ce_frame is gui_frame:
    margin (0, 0)
    padding (24, 16)
    background "#2b2b2b"
    yfill True

style ce_vbox is vbox:
    yfit True
    spacing 0

style ce_hbox is hbox:
    xfit True
    yspacing 0

style ce_text:
    font "gui/font/JetBrainsMono-Regular.ttf"
    size 16
    color "#A9B7C6"
    slow_cps 15

style ce_identifier_text is ce_text
style ce_symbol_text is ce_text:
    size 18

style ce_comment_text is ce_text:
    font "gui/font/JetBrainsMono-Italic.ttf"
    color "#75715e"

style ce_docstring_text is ce_comment_text

style ce_str_const_text is ce_text:
    color "#A5C25C"

style ce_keyword_text is ce_text:
    font "gui/font/JetBrainsMono-Bold.ttf"
    color "#CB772F"

style ce_num_text is ce_text:
    color "#6897BB"