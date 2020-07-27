#
# options.rpy
# Unscripted
#
# Created by Marquis Kurt on 07/01/19.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

# Load the Unscripted build configuration defined in build.toml.
init -2000 python:
    import toml
    import logging

    log_filename = "uvn.log" if not renpy.macintosh else config.savedir \
        + "/../../Logs/net.marquiskurt.unscripted.log"

    logging.basicConfig(format='%(asctime)s - [%(levelname)s] %(message)s',
                        level=logging.INFO,
                        filename=log_filename)

    class UnscriptedCoreConfigError(Exception):
        """Could not load the build configuration."""

    # Call the default build config from the core if the build.toml file at top doesn't exist.
    uconf_path = "build.toml"
    if not renpy.loadable(uconf_path):
        logging.warn("Build configuration is missing. Loading the default settings.")
        uconf_path = "core/build.toml"

    # If the default build configuration is missing, raise an exception.
    if not renpy.loadable(uconf_path):
        logging.critical("Build configuration at %s not found or not loadable." % (uconf_path))
        raise UnscriptedCoreConfigError("The build configuration for Unscripted is not loadable.")

    # If the config field is missing from the build.toml file, raise an exception.
    with renpy.file(uconf_path) as uconf_file:
        toml_load = toml.load(uconf_file)
        if "config" not in toml_load:
            logging.error("Build configuration is either empty or corrupt.")
            raise UnscriptedCoreConfigError("The build configuration is missing the 'config' key.")

        # Store the Unscripted configuration as uconf, which is referenced in other places.
        uconf = toml_load["config"]
        uconf["info"]["build_channel"] = uconf["info"]["channel"]
        logging.info("Loaded build configuration at " + uconf_path + ".")

init -100 python:
    # If Unscripted was started in developer mode (either from the Ren'Py launcher or from the)
    # SDK, change the channel to "Canary".
    if config.developer:
        uconf["info"]["channel"] = "canary"
        logging.info(
            "Channel set to 'canary' because the client is running in developer mode."
        )

    logging.info("New session started.")

    # Update the window icon to the match the channel.
    wicon_add = "_" + uconf["info"]["channel"].replace("stable", "")
    wicon = "core/assets/iconset/window_icon%s.png"\
        % wicon_add if uconf["info"]["channel"] != "stable" else ""

# Basic configuration info such as the product name, version, and save directory.
define config.name = _("Unscripted")
define config.version = uconf["info"]["version"] or "1.0.0"
define build.name = "Unscripted"
define config.save_directory = "net.marquiskurt.unscripted"

# GUI Information
define gui.show_name = True
define gui.about = _("")
define config.window_icon = wicon or "core/core.png"

# Volume configurations
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.default_music_volume = 0.5

# Default settings for the "Emphasize ambience/sound effects" setting in Settings > Sound.
define config.emphasize_audio_channels = ['sound', 'ambient']
define config.emphasize_audio_volume = 0.5
define config.emphasize_audio_time = 0.5

# Theme music cinfiguration
define config.main_menu_music = audio.theme

# Transition configurations
define config.enter_transition = Dissolve(0.1)
define config.exit_transition = Dissolve(0.1)
define config.after_load_transition = fade
define config.end_game_transition = None
define config.end_splash_transition = Dissolve(0.1)
define config.game_main_transition = Dissolve(0.1)

# Say window configurations
define config.window = "auto"
define config.window_show_transition = Dissolve(.25)
define config.window_hide_transition = Dissolve(.25)

# General text speed and auto-play settings. These can be controlled
# in Settings > General.
default preferences.text_cps = 60
default preferences.afm_time = 15

# Save configurations
define config.has_quicksave = False
define config.has_autosave = False
define config.save_json_callbacks = [save_player, save_chaptername]

# Say callbacks. These run whenever dialogue is presented.
define config.all_character_callbacks = [match_inventory_scheme]

# Image and layering information.
define config.search_prefixes = ["", "System/", "assets/", "assets/images/" , "gui/"]
define config.layers = ['background', 'master', 'effects', 'transient', 'screens', 'overlay']
init:
    $ config.tag_layer['effect'] = 'effects'
    $ config.tag_layer['bg'] = 'background'

# Build instructions for Ren'Py.
init python:

    # Create a package type called "patches" where patched files can go. This contains only the
    # archives needed.
    build.package("patches", "zip", "patches", "Patch Files")

    # Create the archives that will be compiled with the game. Scripts will contain the story code,
    # logic contains all of the Unscripted Core logic, and assets contains all of the required
    # images, audio files, etc.
    build.archive("scripts", "patches all")
    build.archive("assets", "patches all")
    build.archive("logic", "patches all")

    # To maintain compatibility with the license, a new archive is added to bundle the source code
    # to Unscripted Core. This archive will not appear in the demo version of the game as this code
    # shouldn't be accessible or licensed in a demo state, unless the demo_bundle_core flag in the
    # build settings is enabled. The source code is also available on GitHub at the following link:
    # https://github.com/UnscriptedVN/core.
    if uconf["demo"]["demo_bundle_core"] or not uconf["demo"]["demo"]:
        build.archive("source", "patches all")

    # Target any of the AliceOS-specific files first. The compiled targets and assets will be added
    # to the logic archive, while the source code will be added to the source archive.
    if uconf["demo"]["demo_bundle_core"] or not uconf["demo"]["demo"]:
        build.classify('game/System/**.aoscservice/**.rpy', "source")
        build.classify('game/System/**.aosapp/**.rpy', "source")
        build.classify('game/core/core.png', "source")
    else:
        build.classify('game/core/core.png', None)

    build.classify('game/System/**.rpy', None)
    build.classify('game/System/**.aoscservice/**', 'logic')
    build.classify('game/Applications/**.rpy', None)
    build.classify('game/Applications/**.aosapp/**', 'logic')
    build.classify('game/System/**', 'logic')

    # Separate all of the logic-specific files before the scripts. This should make the modding
    # process easier since all of the story scripts will be contained in scripts.rpa.
    build.classify("game/core/**.rpyc", 'logic')

    # Bundle the Kotlin scripts in the credits folder since they are required for the credits
    # scenes.
    build.classify("game/core/src/credits/kt/**.kts", 'logic')

    # Bundle the theme files together.
    build.classify("game/core/themes/**", 'logic')

    # Bundle all of the assets together into a single package
    build.classify('game/assets/**', "assets")
    build.classify('game/core/assets/**', 'assets source')

    # Bundle TOML files
    build.classify('game/story/**.toml', "scripts")
    build.classify("game/core/**.toml", 'logic source')

    # If this is the complete game, bundle all the compiled story files together.
    if not uconf["demo"]["demo"]:
        build.classify('game/story/**.rpyc', "scripts")

    # Otherwise, omit the files that don't pertain to the full game. The demo only goes up to the
    # amount of days specified in the build configuration (config.demo.demo_max_count).
    else:
        # Grab all the labels with 'script_ch' first.
        story_labels = filter(lambda a: a.startswith("script_ch"),
                              renpy.get_all_labels())

        # Iterate over every label in order.
        for slabel in sorted(story_labels):

            # Parse the chapter number from the second part of the name.
            chapter_number = int(slabel.split("_")[1][-1:])

            # Get the path of the script file.
            file_location = 'game/story/script-ch%s.rpyc' % (chapter_number)

            # Exclude it if that script is not part of the demo and go to
            # the next file.
            if chapter_number > uconf["demo"]["demo_max_count"]:
                build.classify(file_location, None)
                continue

            # Include the compiled file in the scripts package.
            build.classify(file_location, 'scripts')

    # Grab any other compiled file and toss it into the script package.
    build.classify("game/**.rpyc", 'scripts')
    build.classify("game/build.toml", 'scripts source')

    # Target and bundle all of the Unscripted Core source files together in a convenient place.
    if uconf["demo"]["demo_bundle_core"] or not uconf["demo"]["demo"]:
        build.classify("game/core/**.rpy", "source")
        build.classify("game/core/**.txt", "source")
        build.classify("game/core/**.md", "source")

    # Remove caches, thumbnail databases, and Ren'Py script source files that aren't part of the
    # Unscripted Core.
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)

    # Pack entitlements.plist and other macOS-specific file to the macOS build
    build.classify("entitlements.plist", "mac")

    # Remove unnecessary developer files that come with the project.
    build.classify('docs/**', None)
    build.classify('repo_assets/**.**', None)
    build.classify('unscripted.iconset/**.**', None)
    build.classify('unscripted/**', None)
    build.classify('poetry.lock', None)
    build.classify('pyproject.toml', None)
    build.classify('README.md', None)
    build.classify('.vscode/**.**', None)
    build.classify('.git/**.**', None)
    build.classify('**/cache/**', None)
    build.classify("**/arguments.toml", None)
    build.classify("**/**.vdf", None)
    build.classify("doc_templates/**", None)
    build.classify("iconsets/**", None)
    build.classify(".github/**", None)
    build.classify(".governance/**", None)

    # Remove Ren'Py-generated log files
    build.classify("game/log.txt", None)
    build.classify("game/errors.txt", None)
    build.classify("game/traceback.txt", None)

    # Filter out the DEVCHANGES file in stable builds.
    if uconf["info"]["build_channel"] == "stable":
        build.classify("**/DEVCHANGES.txt", None)

    # Mark as documentation. If this build is the demo, exclude the
    # source code license.
    if uconf["demo"]["demo"]:
        build.classify('**/MPL.txt', None)

    build.documentation('*.html')
    build.documentation('*.txt')

# Used for itch.io uploads in Ren'Py Launcher. Unnecessary if
# using the distribute tool from Poetry (poetry run distribute).
define build.itch_project = "marquiskurt/unscripted"
