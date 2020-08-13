<div align="center">
   <img src="core.png" width="176px" alt="Unscripted Core logo"/>

# Unscripted Core

The core module for [Unscripted][uvn], a visual novel about software development.

[![Ren'Py 7.3.5][renpy]](https://renpy.org)
[![MPL][mozilla]](LICENSE.txt)
![CI][ci]

</div>

## What is Unscripted Core?

Unscripted Core contains the source code for most, if not all, of the logic for the game. This logic includes, but is not limited to:

- User interface controls, themes, and splash screens
- Credits sequencing, lexer, and display mechanism
- Definitions for images and audio
- Minigame frontend logic not covered by [Fira][fira]
- Open-sourced assets such as images and audio
- Classes and logic for player data
- Logic for build configurations

## Why is Unscripted Core open-source?

> I anticipate that some players and developers may want to better understand how I do some things in Unscripted or may want to contribute to the project to catch any bugs. I want to make Unscripted a place to go to learn new things and try out what's available with Python and Ren'Py just like how I did when making mods for DDLC, so I've decided that I will be open-sourcing some core utilities and modules inside of the game itself known as the Unscripted Core.

\- [Captain's Devlog: May-June 2020][devlog]

## Getting started

To get started, clone this repository into a Ren'Py project or Unscripted mod in the `core` folder. The files will automatically be compiled with Unscripted.

> :warning: Unscripted Core is still under heavy development and the overall structure/inner workings of the project will change over time.

### Installing dependencies

Unscripted Core (and the game, subsequently) rely on some Python packages to operate properly. The required dependencies are listed in requirements.txt.

To install these dependencies, run the following\*:

```
pip install -r path/to/core/requirements.txt --target game/python-packages
```

> \*Unscripted is currently built with Ren'Py 7.3.5, which requires that these packages be Python 2-compatible. Run the `pip` command in a Python 2 environment, either from your system or the provided Python environment in Ren'Py.

## Documentation

The following links contain documentation on core aspects of the Unscripted Core.

- [Build Configuration](docs/build.md)
- [Arguments File](docs/arguments.md)
- [Themes](docs/themes.md)

## License

The source code and assets in this repository are licensed under the Mozilla Public License v2.0. More information on how this code is licensed can be found in the game's license.

Unscripted Core is made possible with the following open-source software:

- Inter, Lexend, JetBrains Mono (fonts): SIL Open Font License, Apache 2.0 License
- Discord RPC: Mozilla Public License
- AliceOS: BSD-2-Clause License
- Ren'Py: MIT, Lesser GPL License
- Ring UI (Interface design inspiration): Apache 2.0 License
- Feather Icons: MIT License
- Minetest: MIT License
- Ayu color scheme: MIT License

<!--Images and links-->

[renpy]: https://img.shields.io/badge/renpy-7.3.5-orange.svg
[license]: https://img.shields.io/badge/license-MPLv2-green.svg?logo=mozilla
[fira]: https://github.com/UnscriptedVN/fira
[uvn]: https://unscriptedvn.dev
[ci]: https://github.com/UnscriptedVN/core/workflows/CI/badge.svg?event=push
[mozilla]: https://img.shields.io/github/license/UnscriptedVN/core
[devlog]: https://unscriptedvn.dev/posts/2020/06/15/captains-devlog-may-june-2020/
