#
# storymap.rpy
# Unscripted Core - Story Map
#
# Created by Marquis Kurt on 05/11/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init -10 python:
    class StoryMap(renpy.store.object):
        """The class representation of a story map.

        The story map contains all of the information the player sets in a given playthrough. This
            usually includes the type of game being made, the language that game is written in,
            the current route of the game, etc.

        Attributes:
            game_type (str): The type of game being created. This is a read-only value to ensure
                backwards compatibility with older versions of the game that require this field.
            language (str): The language the game will be written in
            route (str): The route the player is currently on
            choices (dict): The different choices made in a given route
            emails (dict): The emails sent in a given run and whether the player has checked them
        """

        language = "Python"
        route = ""
        choices = { }
        emails = { }

        @property
        def game_type(self):
            return "puzzle"

        def update_email(self, email_number, checked=False):
            """Record whether or not the player has checked an email with a give number.

            Arguments:
                email_number (int): The number corresponding to the email.
                checked (bool): Whether the player has checked the email.
            """
            self.emails[email_number] = checked

        def __eq__(self, other):
            """Determine whether two StoryMap objects are equal."""
            return isinstance(other, StoryMap) and self.__dict__ == other.__dict__

        def __ne__(self, other):
            """Determine whether two StoryMap objects are not equal."""
            return not self.__eq__(other)

        def __init__(self):
            """Construct an empty StoryMap."""
            self.language = "Python"
            self.route = ""
            self.emails = { }
            self.choices = { }
            pass
