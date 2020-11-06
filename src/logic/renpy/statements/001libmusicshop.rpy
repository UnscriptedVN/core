#
# 001libmusicshop.rpy
# Unscripted Core - Custom Statements
#
# Created by Marquis Kurt on 11/06/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

python early:

    def _push_mus_layer(trackname, layer):
        position = renpy.music.get_pos(channel="music") or 0.0
        bit = "<from %s>%s" % (position, trackname)
        renpy.music.play(bit, channel=layer, fadein=3.0)
        renpy.music.queue(trackname, channel=layer, loop=True, clear_queue=True)

    def _pop_mus_layer(layer):
        renpy.music.stop(channel=layer, fadeout=3.0)

    def _parse_musiclayer_push(lex):
        trackname = lex.simple_expression()
        channel = lex.simple_expression()
        print(trackname, channel)
        return (trackname, channel)

    def _parse_musiclayer_pop(lex):
        channel = lex.rest()
        if not channel:
            renpy.error("Channel must be supplied to pop the layer.")
        return channel

    def _lint_musiclayer_cmd(lex):
        pass

    def _execute_musiclayer_push(o):
        trackname, channel = o
        track = eval(trackname, locals=store.audio.__dict__)
        layer = eval(channel, locals=store.audio.__dict__)
        _push_mus_layer(track, layer=layer)

    def _execute_musiclayer_pop(o):
        channel = o
        _pop_mus_layer(channel)

    renpy.register_statement(
        "musiclayer push",
        parse=_parse_musiclayer_push,
        lint=_lint_musiclayer_cmd,
        execute=_execute_musiclayer_push
    )

    renpy.register_statement(
        "musiclayer pop",
        parse=_parse_musiclayer_pop,
        lint=_lint_musiclayer_cmd,
        execute=_execute_musiclayer_pop
    )
