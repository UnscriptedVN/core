#
# state.rpy
# Unscripted Core - Minigame (State Manager)
#
# Created by Marquis Kurt on 07/24/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 10

init python:
    class MinigameState(renpy.store.object):
        """An object representation of a minigame state.

        A minigame state consists of a player's position, the current number of devices the player
            has turned on, and a list containing all of the checks that the player has passed.
        """
        position = (0, 0)
        count = 0
        checks = [False, False]

        def __init__(self, position, count, checks):
            self.position = position
            self.count = count
            self.checks = checks

        def __str__(self):
            passed = False not in self.checks
            return "%s (%s devices, Passes all checks: %s)" % (self.position, self.count, passed)

    class MinigameStateManager(renpy.store.object):
        """A class representation of a state manager for the minigame.

        The state manager is used to keep track of the current goals and tasks a player has
            committed. The state manager can also be used to manage states for cases where
            artificial intelligence is used.
        """

        _player_position = (0, 0)
        _exit_position = (0, 0)
        _total_item_count = 0
        _current_item_count = 0
        _previous = []

        @property
        def history(self):
            """A list containing all previous states that lead up to the current state."""
            return self._previous

        def __init__(self, player_position, exit_position, starting_count, expected_count):
            """Initialize the state manager.

            Args:
                player_position (tuple): The player's starting position.
                exit_position (tuple): The exit's position.
                starting_count (int): The number of devices the player has already turned on.
                expected_count (int): The number of devices the player needs to turn on.
            """
            self._player_position = player_position
            self._exit_position = exit_position
            self._current_item_count = starting_count
            self._total_item_count = expected_count

        def update_state(self, new_position, new_count):
            """Add the current state and generate a new successor.

            Args:
                new_position (tuple): The player's new position.
                new_count (int): The number of devices the player has now turned on.
            """
            self._previous.append(self.get_state())
            self._player_position = new_position
            self._current_item_count = new_count

        def get_state(self):
            """Get the current state.

            Returns:
                state (MinigameState): The current minigame state.
            """
            checks = [self._arrived(), self._acted()]
            return MinigameState(self._player_position, self._current_item_count, checks)

        def _arrived(self):
            """Returns whether the player's position is at the exit."""
            return self._player_position == self._exit_position

        def _acted(self):
            """Return whether the player has turned on all devices."""
            return self._total_item_count == self._current_item_count
