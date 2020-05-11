#
# logic.rpy
# Unscripted Core - Credits (Logic)
#
# Created by Marquis Kurt on 04/14/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 7

init python:
    def transform_tokens(tokens):
        new_tokens = []
        current_row = []

        for kind, name in tokens:
            t = name.replace("{", "{{")
            current_row.append((kind, t))

            if kind == "tab":
                continue

            if kind == "newline":
                if len(current_row) > 1:
                    new_tokens.append(current_row)
                current_row = []

        return new_tokens