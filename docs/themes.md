# Theming

Unscripted supports the creation and usage of themes which manage the overall look of the game and its interface. Themes are defined as a directory with a manifest and subdirectories of image files that contain the interface elements.

![Ayu Dark Blue theme](https://user-images.githubusercontent.com/13445064/83585115-fe262e00-a516-11ea-90d8-7c80eaad378a.png)

## Default themes

There are four themes that ship with Unscripted:

- Ayu Light Blue (`ruby-light`)
- Ayu Mirage Blue (`ruby-mirage`)
- Ayu Dark Blue (`ruby-dark`)
- Ring (`ring`)

All Ayu themes are variants of the [Ayu color scheme](https://github.com/ayu-theme/ayu-colors) with the accent color changed to the Unscripted blue color. Ring is the original Unscripted theme before the theme overhaul.

The game will try to set `ring` as the default interface theme if no theme is present. In the game's settings under **Appearance**, the game will allow players to select from any of the Ayu themes.

## Creating a theme

A theme can be created by creating a directory of the theme's name and then adding a manifest file in the theme's directory called `theme.toml`.

### Theme manifest

The theme manifest contains a single dictionary key, `theme`. The following is a list of all of the respective keys and values for the manifest:

- `theme` - The root theme object
  - `name` - The name of the theme. This should match the directory's name.
  - `type` - The theme's color scheme type. Should either be `"light"` or `"dark"`
  - `resources-dir` - The path to the theme's folder
  - `colors` - The theme's text and interface colors
    - `background` - The color to use for a background when an image isn't provided.
    - `interface` - The color of the theme's foreground text
    - `interface_active` - The theme's accent color
    - `interface_highlight` - The theme's highlight color
    - `interface_secondary` - The theme's "muted" or "disabled" color
    - `syntax` - The theme's syntax colors
      - `source_text` - The color for standard source text
      - `symbols` - The color for code symbols
      - `comments` - The color for code comments
      - `docstrings` - The color for code documentation
      - `strings` - The color for strings
      - `keywords` - The color for keywords
      - `numbers` - The color for constants such as numbers

This is the manifest for `ruby-light` as an example:

```toml
[theme]
name = "ruby-light"
type = "light"
resources-dir = "core/themes/ruby-light"

[theme.colors]
background = "#FAFAFA"
interface = "#959DA6"
interface_active = "#55B4D4"
interface_highlight = "#77A8D9"
interface_secondary = "#6C7680"
interface_button_idle = "#FFCC66"

[theme.colors.syntax]
source_text = "#6C7680"
symbols = "#6C7680"
comments = "#ABB0B6"
docstrings = "#ABB0B6"
strings = "#86B300"
keywords = "#FA8D3E"
numbers = "#A37ACC"
```

### Theme resources

Interface elements such as frames, buttons, and checkboxes are drawn with image files, which are located in the `resources` directory of the theme's folder. The theme should contain files for the following elements:

- Bars
- Buttons
- Checkboxes
- Frames
- Overlays
- Radios
- Scrollers
- Sliders
- Tabs

Most interact-able elements like checkboxes and buttons will have multiple states: `idle`, `hover`, `selected_idle`, `selected_hover`, and/or `insensitive`. Consult any of the default themes for the exact structure and kinds of files needed.

## Theme object

The `Theme` object holds the data necessary to create and render a theme. The following is the Python documentation for this class.

### Constructor

Construct a theme object.

#### Args

- \*\*kwargs: Arbitrary keyword arguments

#### Kwargs

- filepath (str): The path to a valid theme configuration.
- name (str): The name of the theme.
- path (str): The path to the file's theme resources.

### `colors()`

Get the theme's colors.

#### Returns

- ui_colors (ThemeColor): The theme's UI colors.

### `syntaxes()`

Get the theme's colors for syntax highlighting.

#### Returns

- syntax_colors (ThemeSyntaxColor): The theme's syntax colors.

### `checkboxes()`

Get the paths for the theme's checkbox styles.

#### Returns

- checks (ThemeCheckbox): The theme's checkbox enumeration.

### `radios()`

Get the paths for the theme's radio styles.

#### Returns

- checks (ThemeRadio): The theme's radio enumeration.

### `buttons()`

Get the path for the theme's button styles.

#### Returns

- buttons (str): The path to the button images.

### `tabs()`

Get the path for the theme's tab group styles.

#### Returns

- tabs (str): The path to the tab group images.

### `bars()`

Get the paths for the theme's bar styles.

#### Returns

- bars (ThemeBars): The theme's bars enumeration.

### `scrollbars()`

Get the paths for the theme's scrollbar styles.

#### Returns

- scrollbars (ThemeScrollbars): The theme's scrollbars enumeration.

### `sliders()`

Get the paths for the theme's slider styles.

#### Returns

- sliders (ThemeSliders): The theme's scrollbars enumeration.

### `frames()`

Get the paths for the theme's frame styles.

#### Returns

- frames (ThemeFrame): The theme's frame enumeration.

### `overlays()`

Get the paths for the theme's overlay styles.

#### Returns

- overlays (overlay): The theme's overlay enumeration.
