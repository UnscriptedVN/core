#
# characters.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/6/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

# Create the character object and assign their names to the dynamic
# variables stored below.
define narrator = Character(image='unknown',
                            ctc='ctc')

define mc = Character('[player.name]',
                      what_prefix='"',
                      what_suffix='"',
                      image='mc',
                      ctc='ctc')

define c = Character('[cname]',
                     image='christina',
                     what_prefix='"',
                     what_suffix='"',
                     ctc='ctc')

define z = Character('[zname]',
                     image='zenno',
                     what_prefix='"',
                     what_suffix='"',
                     ctc='ctc')

define k = Character('[kname]',
                     image='katorin',
                     what_prefix='"',
                     what_suffix='"',
                     ctc='ctc')

define m = Character('[mname]',
                     image='fira',
                     what_prefix='"',
                     what_suffix='"',
                     ctc='ctc')

# Generate default values for the names of the characters if nothing
# is found. This should be overwritten in script.rpy to `???`.
init -1:
    default player.name = "MC"
    default cname = "Christina"
    default zname = "Zen'no"
    default kname = "Katorin"
    default mname = "Meredith"
