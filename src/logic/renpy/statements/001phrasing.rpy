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

    # MARK: Phrase Updates

    def update_phrasing(base="bgm/base.ogg", mood=None, char=None):
        """Update the sequencing of the music playing to match a set of specific conditions.

        The respective files from the conditions will be queued in their respective channels, and
            then Ren'Py will play those files, ensuring the current phrase is finished before
            playing all of the tracks simultaneously.

        Args:
            base (str): The filename of the base track. Defaults to "bgm/base.ogg".
            mood (Optional[str]): The filename of the mood track. Defaults to None
            char (Optional[str]): The filename of the character track. Defaults to None.
        """
        b_queue = [base] if base is not None else []
        s_queue = [mood] if mood is not None else []
        c_queue = [char] if char is not None else []

        renpy.music.queue(c_queue, channel="music_char", loop=True, clear_queue=True)
        renpy.music.queue(s_queue, channel="music_scene", loop=True, clear_queue=True)
        renpy.music.queue(b_queue, channel="music", loop=True, clear_queue=True)

    def parse_phrasing(lex):
        """Parse a phrase statement."""
        base = lex.simple_expression()
        if not base:
            renpy.error("Base track in phrase must be defined.")

        mood = lex.simple_expression()
        if not mood:
            renpy.error("Mood or scene track in phrase must be defined.")

        char = lex.simple_expression()
        if not char:
            renpy.error("Character tack must be defined.")

        return (base, mood, char)

    def execute_phrasing(o):
        """Execute a phrase statement."""
        base, mood, char = o
        try:
            base = eval(base, locals=store.audio.__dict__)
            mood = eval(mood, locals=store.audio.__dict__)
            char = eval(char, locals=store.audio.__dict__)
        except:
            base = mood = char = None
        update_phrasing(base=base, mood=mood, char=char)

    def lint_phrasing(o):
        """Lint a phrase statement."""
        try:
            base, mood, char = o
        except:
            renpy.error("Phrase statement doesn't contain files for base, scene, and character.")

    # MARK: Kill Phrase
    def parse_killphrase(lex):
        """Parse a killphrase statement."""
        return {}

    def lint_killphrase(o):
        """Lint a killphrase statement."""
        pass

    def execute_killphrase(o):
        """Execute a killphrase statement by stopping all music channels."""
        for channel in ["music", "music_scene", "music_char"]:
            renpy.music.stop(channel=channel)

    # Register the phrase statement.
    renpy.register_statement(
        "phrase",
        parse=parse_phrasing,
        execute=execute_phrasing,
        lint=lint_phrasing
    )

    # Register the killphrase statement.
    renpy.register_statement(
        "killphrase",
        parse=parse_killphrase,
        execute=execute_killphrase,
        lint=lint_killphrase
    )
