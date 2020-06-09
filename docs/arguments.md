# Arguments File

Since Unscripted doesn't support command-line arguments presently, players and developers can create an arguments file that will act as command line arguments.

Unscripted will search for an arguments file at the root of the game's files, `arguments.toml`:

```
Unscripted/
    scripts.rpa
    images.rpa
    logic.rpa
    arguments.toml
```

For macOS builds, you may need to right-click on the app and select "Show Package Contents", then navigate to Contents/Resources/game/.

The arguments should contain a single dictionary at the root, `args`. The following are the allowed keys in the arguments file:

- `init_dreams`: Whether to initialize the dreams folder in the game files if Dreams are enabled.
- `disable-minigame`: Whether to disable the minigame and prevent it from running at all.
- `disable_experiments`: Defines the list of experiments to turn off when running the game. Should be a list of strings that matches the experiments defined in the build configuration.

## Example

```toml
[args]
disable_experiments = [
    "enable-glossary"
]
```
