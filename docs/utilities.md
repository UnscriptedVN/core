# Common Utilities

The following documentation is a running list of all of the common utilities in Unscripted Core. These utilities are found in `src/logic/utils.rpy`.

## `InventoryMismatchError(Exception)`

The inventory between AliceOS and the player's doesn't match.

## `FeatherAssetError(Exception)`

The Feather icon could not be found.

## `TimeOfDay(Enum)`

An enumeration class for the different times of day (see dynamic backgrounds).

### Cases

- morning
- day
- night

## `acquire_item(item_key)`

Add the item with a specific key to the inventory.

### Args

- item_key (str): The item's key.

## `use_item(item_key, remove=False)`

Use the item with a given key.

### Args

- item_key (str): The item's key.
- remove (bool): Whether to remove the item from the inventory. Defaults to False.

## `restore_inventory()`

Restore the inventory to the state listed in the player's
inventory.

## `grab_recent_items()`

Grab the five most recent items from the inventory.

## `match_inventory_scheme(event, interact=True, **kwargs)`

Compare the current state's inventory and the AliceOS inventory and update AliceOS's inventory if there isn't a match.

This is used in the character say callback to manage the state of the inventory to make sure that AliceOS's Inventories is keeping up with the player at a given point.

### Args

- event: The callback event
- interact (bool): Whether the dialogue causes an interaction

## `update_item_callbacks(item_callbacks)`

Update the use case callbacks in the inventory.

### Args

- item_callbacks (dict): A dictionary containing the callbacks for items.

## `clear_item_callbacks()`

Clear all of the existing callbacks for the inventory.

## `get_feather_icon(name, mode=None)`

Get the path to a Feather icon.

### Args

- name (str): The name of the Feather icon.

## `reset_playername()`

Reset the player to a default player with the name 'MC'.

## `change_playing_state()`

Send an update to the Discord Rich Presence client and update the rich presence state.

## `get_history_name(who)`

Get the history name of the character in question.

### Args

- who (str): The name of the character.

## `finished_talks(a)`

Determine whether the given dictionary of talks has been completed.

The dictionary is checked to see if all values are set to True.

### Args

- a (dict): The dictionary of talks.

## `get_username()`

Get the username of the current computer user.

## `escape_code(who, code="print \"Hello, world!\"")`

Use a character line to speak code.

### Args

- who (Character): The character to deliver the dialogue
- code (str): The corresponding code.

## `current_theme()`

Get the theme object for the currently selected theme.

### Returns

- theme (Theme): The theme object that corresponds to the GUI preference for the theme. If the theme object cannot be loaded, it will attempt to use the Ring theme.

## `gtheme(name)`

Get the theme object for the currently selected theme.

### Returns

- theme (Theme): The theme object that corresponds to the GUI preference for the theme. If the theme object cannot be loaded, it will attempt to use the Ring theme.

## `dynamic_background(image_path, include=[TimeOfDay.day, TimeOfDay.night])`

Get the background based on the time of day, relative to "Catalina City" time.

This utility assumes that Catalina City is occurring during the summer where the day is longer and the night is shorter. The utility reads the current hour on the user's machine and determines the appropriate image to apply.

This utility also only works with JPEG files.

### Args

- image_path (str): The path to the image to use.
- include (list): A list of the different times of day to include in the dynamic background.

### Returns

- path (str): The path to the image according to the time of day.

## `open_directory(path)`

Open the directory with the system's file browser.

### Args

- path (str): The path to open in the system's file browser.
