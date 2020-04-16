#
# player.rpy
# Unscripted
#
# Created by Marquis Kurt on 01/06/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init -10 python:

    class StoryMap(renpy.store.object):
        """
            The base object for a story map. The story map
            contains information about a player's intentions
            and choices.
        """

        game_type = "platformer"
        language = "Python"
        route = ""
        choices = { }
        emails = { }

        def update_email(self, email_number, checked=False):
            """
                Record whether or not the player has checked an email
                with a give number.

                Args:
                    email_number: The number corresponding to the email.
                    checked: Whether the player has checked the email.
            """
            self.emails[email_number] = checked

        def __eq__(self, other):
            """
                Determine whether two StoryMap objects are
                equal.
            """
            return isinstance(other, StoryMap) and self.__dict__ == other.__dict__

        def __ne__(self, other):
            """
                Determine whether two StoryMap objects are
                not equal.
            """
            return not self.__eq__(other)

        def __init__(self):
            """
                Construct an empty StoryMap.
            """
            self.game_type = "platformer"
            self.language = "Python"
            self.route = ""
            self.emails = { }
            self.choices = { }
            pass

    class Player(renpy.store.object):
        """
            The base object for a player. The Player object contains
            information regarding the character's experience and
            information.
        """

        name = "MC"
        current_inventory = []
        current_inbox = []
        pronouns = {
            "subject": "he",
            "object": "him",
            "possessive": "his"
        }

        def serialize(self):
            """Get a serializable version of this class.

            This may be useful in cases where the Player object cannot
            be inherently serialized due to the StoryMap instance.
            """
            self_dict = self.__dict__.copy()
            story_map_dict = self.story_map.__dict__.copy()
            self_dict["story_map"] = story_map_dict
            return self_dict

        def update_language(self, lang="Python"):
            """Set the programming language for the story.

            Args:
                lang: The language to update to.
            """
            player.story_map.language = lang

        def update_pronouns(self, identify_as="male"):
            """Update the player's pronouns.

            Args:
                identify_as: The pronoun type to identify as (male, female, they)
            """
            if identify_as not in ["male", "female", "they"]:
                raise KeyError("Could not find pronoun set for %s" % (identify_as))

            pronouns = {
                "male": ("he", "him", "his"),
                "female": ("she", "her", "hers"),
                "they": ("they", "them", "their")
            }

            sub, obj, poss = pronouns.get(identify_as)
            self.pronouns['subject'] = sub
            self.pronouns['object'] = obj
            self.pronouns['possessive'] = poss

        def __init__(self, name):
            """
                Construct the Player object.

                Args:
                    name: The name of the Player.
            """

            self.name = name
            self.current_inventory = []
            self.current_inbox = []
            self.story_map = StoryMap()
            self.pronouns = {
                "subject": "",
                "object": "",
                "possessive": ""
            }

        def __eq__(self, other):
            """
                Determine whether a Player object is the same
                as another.
            """
            return isinstance(other, Player) and self.__dict__ == other.__dict__

        def __ne__(self, other):
            """
                Determine whether a Player object is different
                from another.
            """
            return not self.__eq__(other)