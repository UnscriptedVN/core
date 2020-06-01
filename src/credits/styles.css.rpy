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
    background current_theme().colors().BACKGROUND.value
    yfill True

style ce_vbox is vbox:
    yfit True
    spacing -8

style ce_hbox is hbox:
    xfit True
    yspacing 0

style ce_text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Regular.ttf"
    size 16
    color current_theme().syntaxes().SOURCE_TEXT.value
    slow_cps 15

style ce_identifier_text is ce_text
style ce_symbol_text is ce_text:
    size 18

style ce_comment_text is ce_text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Italic.ttf"
    color current_theme().syntaxes().COMMENTS.value

style ce_docstring_text is ce_comment_text

style ce_str_const_text is ce_text:
    color current_theme().syntaxes().STRINGS.value

style ce_keyword_text is ce_text:
    font "core/assets/fonts/jb_mono/JetBrainsMono-Bold.ttf"
    color current_theme().syntaxes().KEYWORDS.value

style ce_num_text is ce_text:
    color current_theme().syntaxes().NUMBERS.value
