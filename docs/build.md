# Build Configuration

Unscripted Core uses a build configuration file to handle versioning, channels, and enabling/disabling specific files in the game. This configuration, `build.toml`, should live in the root of the game's files. When Unscripted runs, it will read from this file and store the configuration in a Python dictionary `uconf`.

The following is a document that outlines all of the possible fields and information inside the build configuration file.

> :warning: The build configuration file is still a work-in-progress. Fields and information may change over time.

## Information

The info section controls the versioning information and release channels for the game. There are two primary keys used in the `info` section of the build file:

- `version` - Defines the game's version, such as `1.2.3`. This is exposed here to allow easy manipulation in external processes such as CI deployments.
- `channel` - Defines the release channel. Typically, there are two channels used: `"stable"` and `"beta"`. If the game is started via the Ren'Py SDK, the channel is set to `"canary"`.

```toml
[config.info]
version = "1.2.3"
channel = "stable"
```

## Features

The features section controls what features are enabled in the game by default. The following keys exist in the features section:

- `enable_dreams` - Whether the Dreams modding functionality should be enabled.
- `enable_minigame_adv_mode` - Whether to enable the minigame's advanced mode. This does _not_ turn the feature on, but it allows for the option to exist in the game.

```toml
[config.features]
enable_dreams = false
enable_youtrack_link = true
enable_minigame_adv_mode = true
```

## Labs

The labs section controls experimental features. There currently is a single key, `current`, which contains a list of strings for the experiments that will be enabled in the game.

```toml
[config.labs]
current = [
    "enable-glossary"
]
```

## Analytics

The analytics section controls the features for the bug reports and analytics data.

- `enable_bug_reports` - Whether or not to show the bug report links in the game menu. Replaces `enable_youtrack_link` in features.
- `survey_link` - Defines the survey link at the end of the game. If this key is included, a prompt will appear at the end of the game that encourages players to take a survey about the game.
- `links` - Defines the bug reporting links. This dictionary should contain fields for the stable and beta release channels.

```toml
[config.analytics]
enable_bug_reports = true
survey_link = "https://go-to-my-survey.com"

[config.analytics.links]
stable = "https://github.com/UnscriptedVN/issues/issues/new/choose"
beta = "https://github.com/UnscriptedVN/game/issues/new/choose"
```

## Discord

The Discord section controls the Rich Presence feature in the game. There are two keys present:

- `enable_rpc` - Whether the Rich Presence client should be enabled.
- `client_id` - Defines the Discord Rich Presence client's ID. This client must contain the images necessary for the game.

```toml
[config.discord]
enable_rpc = true
client_id = "000000000000000000"
```

## Demo

The demo section controls different aspects of the demo version of the game.

- `demo` - Whether this build is a demo release.
- `demo_max_count` - Defines the maximum number of chapters that should be accessible in the game.
- `demo_bundle_core` - Whether the game should make an archive containing the source code to the Unscripted Core.

```toml
[config.demo]
demo = false
demo_max_count = 6
demo_bundle_core = false
```
