#
# 01phrasing.rpy
# Unscripted
#
# Created by Marquis Kurt on 10/26/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

python early hide:
    def update_phrasing(**kwargs):
        """Update the sequencing of the music playing to match a set of specific conditions.

        The respective files from the conditions will be queued in their respective channels, and
            then Ren'Py will play those files, ensuring the current phrase is finished before
            playing all of the tracks simultaneously.

        Kwargs:
            base (str): The filename of the base track. Defaults to "bgm/base.ogg".
            mood (str): The filename of the mood track. Defaults to None
            char (str): The filename of the character track. Defaults to None.
        """
        b_queue = [kwargs["base"]] if "base" in kwargs and kwargs["base"] is not None else []
        s_queue = [kwargs["mood"]] if "mood" in kwargs and kwargs["mood"] is not None else []
        c_queue = [kwargs["char"]] if "char" in kwargs and kwargs["char"] is not None else []

        if "char" in kwargs:
            renpy.music.queue(c_queue, channel="music_char", loop=True, clear_queue=True)
        if "mood" in kwargs:
            renpy.music.queue(s_queue, channel="music_scene", loop=True, clear_queue=True)
        if "base" in kwargs:
            renpy.music.queue(b_queue, channel="music", loop=True, clear_queue=True)

    def parse_start_loop(lex):
        basename = lex.simple_expression()
        if not basename:
            renpy.error("Base track must be supplied.")
        return basename

    def execute_start_loop(o):
        basename = eval(o, locals=store.audio.__dict__)
        update_phrasing(base=basename)

    def parse_update_loop(lex):
        channel = lex.simple_expression()
        track = lex.simple_expression()
        return (channel, track)

    def execute_update_loop(o):
        channel, ut = o
        print(o)
        track = eval(ut, locals=store.audio.__dict__)
        kwargs = {}
        kwargs[channel] = track
        update_phrasing(**kwargs)

    def execute_end_loop(o):
        update_phrasing(base=None, mood=None, char=None)

    def execute_kill_loop(o):
        for channel in ["music", "music_scene", "music_char"]:
             renpy.music.stop(channel=channel)

    def empty_parse(lex):
        pass

    def empty_lint(o):
        pass

    renpy.register_statement(
        "musicloop start",
        parse=parse_start_loop,
        execute=execute_start_loop,
        lint=empty_lint
    )

    renpy.register_statement(
        "musicloop update",
        parse=parse_update_loop,
        execute=execute_update_loop,
        lint=empty_lint
    )

    renpy.register_statement(
        "musicloop end",
        parse=empty_parse,
        execute=execute_end_loop,
        lint=empty_lint
    )

    renpy.register_statement(
        "musicloop kill",
        parse=empty_parse,
        execute=execute_kill_loop,
        lint=empty_lint
    )
