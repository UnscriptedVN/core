#
# funcs.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/13/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init -10 python:
    import os
    import logging
    import collections
    from subprocess import check_call

    class InventoryMismatchError(Exception):
        pass

    class FeatherAssetError(Exception):
        pass

    # MARK: Inventory
    def acquire_item(item_key):
        """Add the item with a specific key to the inventory.

        Args:
            item_key: The item's key.
        """
        item = inventory_items[item_key]
        if item_key not in store.player.current_inventory:
            store.player.current_inventory.append(item_key)

        current_inventory = inventory.export(filter=lambda a: a.itemId)
        if item_key not in current_inventory:
            inventory.addItem(item, silent=True)
            renpy.notify("You just received the '%s' item." % (item.name))

    def use_item(item_key, remove=False):
        """Use the item with a given key.

        Args:
            item_key: The item's key.
            remove: Whether to remove the item from the inventory.
            Defaults to False.
        """

        item = inventory_items[item_key]
        inventory.useItem(item)

        if remove:
            inventory.removeItem(item)
            store.player.current_inventory.remove(item_key)

    def restore_inventory():
        """Restore the inventory to the state listed in the player's
        inventory.
        """
        current_inventory = inventory.export(filter=lambda a: a.itemId)
        for item_key in store.player.current_inventory:
            if item_key not in current_inventory:
                inventory.addItem(inventory_items[item_key], silent=True)

    def get_recent_items():
        """Grab the five most recent items from the inventory.
        """
        return inventory.export()[:5]

    def match_inventory_scheme(event, interact=True, **kwargs):
        """Compare the current state's inventory and the AliceOS inventory
        and update AliceOS's inventory if there isn't a match.

        This is used in the character say callback to manage the state of
        the inventory to make sure that AliceOS's Inventories is keeping
        up with the player at a given point.

        Args:
            event: The callback event
            interact: Whether the dialogue causes an interaction
        """
        pinv = store.player.current_inventory
        ainv = inventory.export(filter=lambda i: i.itemId)

        # Run only at the start of the callback.
        if event == "begin":
            # If the player inventory item is not in the AliceOS inventory,
            # add it.
            for pitem in pinv:
                if pitem not in ainv:
                    inventory.addItem(inventory_items[pitem])

            # If the AliceOS inventory item is not in the player's inventory,
            # remove it.
            for aitem in ainv:
                if aitem not in pinv:
                    inventory.removeItem(inventory.getItemById(aitem))

            # Ensure that the checks worked correctly.
            ainv = inventory.export(filter=lambda i: i.itemId)
            if collections.Counter(pinv) != collections.Counter(ainv):
                logging.error("Inventories don't match: %s vs. %s",
                              pinv,
                              ainv)
                raise InventoryMismatchError("The inventory state manager failed to update.")

    def update_item_callbacks(item_callbacks):
        """Update the use case callbacks in the inventory.

        Args:
            item_callbacks (dict): A dictionary containing the callbacks for items.
        """
        for item in item_callbacks:
            callback = item_callbacks[item]
            if item in inventory_items:
                inventory_items[item].runSpecialUseCase = callback

    def clear_item_callbacks():
        """Clear all of the existing callbacks for the inventory."""
        for item in inventory_items:
            inventory_items[item].runSpecialUseCase = None

    # MARK: Feather
    def get_feather_icon(name):
        """Get the path to a Feather icon.

        Args:
            name: The name of the Feather icon.
        """
        if not renpy.loadable("core/assets/feather/%s.png" % (name)):
            logging.error("Icon %s cannot be found or doesn't exist." % (name))
            raise FeatherAssetError("Icon %s cannot be found or doesn't exist." % (name))
        return "core/assets/feather/%s.png" % (name)

    # MARK: Player name utilities
    def reset_playername():
        """Reset the player to a default player with the name 'MC'.
        """
        store.player = Player("MC")

    def change_playing_state():
        """Send an update to the Discord Rich Presence client and update
        the rich presence state.
        """
        rt = store.player.story_map.route or ""
        ch_text = "Starting a new game"
        ch_img = "chnull_1024"
        if "chapter_count" in store.__dict__:
            ch_text = "Chapter %s | %s" % (store.chapter_count + 1, store.chapter_name)
            ch_img = "ch%s_1024" % (store.chapter_count)
        discord.update_presence(title="with " + rt + " (Ch. %s)" % (store.chapter_count + 1)
                                    if rt else ch_text,
                                detail="as %s" % (store.player.name),
                                image=ch_img,
                                large_text=ch_text)
        if "chapter_count" in store.__dict__:
            logging.info("Updated presence for Chapter %s." % (store.chapter_count + 1))
        else:
            logging.warn("Chapter count is unknown, but presence updated anyway.")

    # MARK: History
    def get_history_name(who):
        """Get the history name of the character in question.

        Args:
            who: The name of the character.
        """
        if who == "???":
            return "unknown"
        elif who == store.player.name:
            return "player"
        else:
            return who.lower()[0]

    # MARK: Conversations
    def finished_talks(a):
        """Determine whether the given dictionary of talks
        has been completed.

        The dictionary is checked to see if all values are
        set to True.

        Args:
            a: The dictionary of talks.
        """
        return False not in a.values()

    # MARK: Spooky stuff
    def get_username():
        """Get the username of the current computer user.
        """
        return os.environ["USERNAME" if renpy.windows else "USER"]

    def escape_code(who, code="print \"Hello, world!\""):
        """Use a character line to speak code.

        Args:
            who: The character to deliver the dialogue
            code: The corresponding code.
        """
        style.say_dialogue = style.python
        who(code)
        style.say_dialogue = style.normal

    def current_theme():
        """Get the theme object for the currently selected theme.

        Returns:
            theme (Theme): The theme object that corresponds to the GUI preference for the theme.
                If the theme object cannot be loaded, it will attempt to use the Ring theme.
        """
        theme = Theme(filepath=os.path.join("core", "themes", "ring", "theme.toml"))
        try:
            theme = Theme(filepath=os.path.join("core", "themes",
                                           gui.preference("theme", "ring"), "theme.toml"))
        except:
            pass
        return theme

init -500 python:
    def open_directory(path):
        # Source: https://stackoverflow.com/a/16204023
        """Open the directory with the system's file browser.

        Arguments:
            path (str): The path to open in the system's file browser.
        """
        try:
            if renpy.windows:
                os.startfile(path.replace("/", "\\"))
                logging.info("Opened %s in Explorer." % (path))
            elif renpy.macintosh:
                check_call(["open", path])
                logging.info("Opened %s in Finder." % (path))
            else:
                check_call(["xdg-open", path])
                logging.info("Opened %s in file manager." % (path))
        except Exception as e:
            renpy.notify("Couldn't open folder.")
            logging.error("Couldn't open %s\nError message: %s" % (path, e.message))
