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
    from subprocess import check_call
    from datetime import datetime
    from enum import Enum

    class InventoryMismatchError(Exception):
        """The inventory between AliceOS and the player's doesn't match."""
        pass

    class FeatherAssetError(Exception):
        """The Feather ifcon could not be found."""
        pass

    class TimeOfDay(Enum):
        """An enumeration class for the different times of day (see dynamic backgrounds)."""
        morning = "morning"
        day = "day"
        night = "night"

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

        if not inventory.getItemById(item.itemId):
            logging.warn("Item %s is not in the inventory, so it cannot be removed."
                         + " Are you rolling back?",
                         item_key)
            return

        inventory.useItem(item)

        if remove:
            inventory.removeItem(item)
            store.player.current_inventory.remove(item_key)

    def clear_inventory():
        """Clear the AliceOS inventory."""
        current_inv = inventory.export(filter=lambda a: a.itemId)
        for item_key in current_inv:
            inventory.removeItem(inventory.getItemById(item_key))

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
        if not "player" not in store.__dict__ or "current_inventory" not in store.player.__dict__:
            return

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
            if sorted(pinv) != sorted(ainv):
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
    def get_feather_icon(name, mode=None):
        """Get the path to a Feather icon.

        Args:
            name (str): The name of the Feather icon.
            mode (Optional[str]): The mode to register the icon as ("light" or "dark"). Defaults to
                None.
        """
        use_light = (mode == "light") if mode else (current_theme().type == ThemeType.LIGHT)
        fname = ("%s.png" if use_light else "%s-dark.png") % (name)
        if not renpy.loadable("core/assets/feather/" + fname):
            logging.error(
                "Icon %s cannot be found or doesn't exist. (Path: %s)" % (
                    name,
                    "core/assets/feather/" + fname
                )
            )
            raise FeatherAssetError("Icon %s cannot be found or doesn't exist." % (name))
        return "core/assets/feather/" + fname

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
        specials = {
            "???": "unknown",
            store.player.name: "player",
            "Fira": "m"
        }
        return specials.get(who, who.lower()[0])

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
        theme = Theme(filepath="core/themes/ruby-light/theme.toml")
        path = "core/themes/%s/theme.toml" % (gui.preference("theme", "ruby-light"))
        try:
            theme = Theme(filepath=path)
        except:
            pass
        return theme

    def gtheme(name):
        """Get the theme object for the currently selected theme.

        Returns:
            theme (Theme): The theme object that corresponds to the GUI preference for the theme.
                If the theme object cannot be loaded, it will attempt to use the Ring theme.
        """
        theme = Theme(filepath="core/themes/" + name + "/theme.toml")
        return theme

    def dynamic_background(image_path, include=[TimeOfDay.day, TimeOfDay.night]):
        """Get the background based on the time of day, relative to \"Catalina City\" time.

        This utility assumes that Catalina City is occurring during the summer where the day is
            longer and the night is shorter. The utility reads the current hour on the user's
            machine and determines the appropriate image to apply.

        This utility also only works with JPEG files.

        Args:
            image_path (str): The path to the image to use.
            include (list): A list of the different times of day to include in the dynamic
                background.

        Returns:
            path (str): The path to the image according to the time of day.
        """
        img = image_path.replace(".jpg", "")
        current_hour = datetime.now().hour
        if TimeOfDay.night in include and current_hour in [0, 1, 2, 3, 4, 21, 21, 23, 24]:
            return img + "_night.jpg"
        elif TimeOfDay.morning in include and current_hour in [5, 6, 7, 18, 19, 20]:
            return img + "_morning.jpg"
        else:
            return img + ".jpg"

    def restore_quick_menu(event, interact=True, **kwargs):
        quick_menu = True

    def restore_vn_state():
        """Restore the VN state."""
        # First, restore the quick menu.
        store.quick_menu = True

        # Restore the skipping functionality if it got disabled.
        if not config.allow_skipping:
            config.allow_skipping = True

init -500 python:

    def is_snap():
        """Dummy function to return false."""
        return renpy.loadable("snapcraft.rpy")

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
