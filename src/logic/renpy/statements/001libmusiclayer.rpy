#
# 001libmusiclayer.rpy
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

    def _music_eligible(channel_name):
        """Returns if the channel is eligible to be added to the music channels list."""
        return renpy.audio.is_playing(channel_name) and type(channel_name) is str

    def _music_channels(without_layer=None):
        """Returns a list of channels with audio being played, excluding a supplied layer.

        Args:
            without_layer (str): The channel to exclude from the list or None.

        Returns:
            A list of channels with audio being played, excluding a supplied layer.
        """
        channels = [c for c in renpy.audio.audio.channels.keys() if _music_eligible(c)]
        if with_layer in channels:
            channels.remove(with_layer)
        return channels

    def _push_mus_layer(trackname, layer):
        """Push a given track to the specified layer.

        The channel will attempt to play the track from where other music channels are currently
            playing, then queue the full track into that channel.

        Args:
            trackname (str): The track to play.
            layer (str): The music channel to push the track to.
        """
        accepted = _music_channels(without_layer=layer)
        reference_channel = "music"
        if not renpy.music.is_playing("music"):
            reference_channel = accepted[0]

        position = renpy.music.get_pos(channel=accepted) or 0.0
        bit = "<from %s>%s" % (position, trackname)

        if renpy.music.is_playing(layer):
            _pop_mus_layer(layer)

        renpy.music.play(bit, channel=layer, fadein=3.0)
        renpy.music.queue(trackname, channel=layer, loop=True, clear_queue=True)

    def _pop_mus_layer(layer):
        """Pop the current track from the specified layer."""
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
