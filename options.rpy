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
init -1000 python:
    import toml

    class UnscriptedCoreConfigError(Exception):
        """Could not load the build configuration."""

    # Call the default build config from the core if the build.toml file at top doesn't exist.
    uconf_path = "build.toml"
    if not renpy.loadable(uconf_path):
        print("[WARN] Build configuration is missing. Loading the default settings...")
        uconf_path = "core/build.toml"

    # If the default build configuration is missing, raise an exception.
    if not renpy.loadable(uconf_path):
        raise UnscriptedCoreConfigError("The build configuration for Unscripted is not loadable.")

    # If the config field is missing from the build.toml file, raise an exception.
    with renpy.file(uconf_path) as uconf_file:
        toml_load = toml.load(uconf_file)
        if "config" not in toml_load:
            raise UnscriptedCoreConfigError("The build configuration is missing the 'config' key.")

        # Store the Unscripted configuration as uconf, which is referenced in other places.
        uconf = toml_load["config"]

# Basic configuration info such as the product name, version, and save directory.
define config.name = _("Unscripted")
define config.version = "1.2.0"
define build.name = "Unscripted"
define config.save_directory = "net.marquiskurt.unscripted"

# GUI Information
define gui.show_name = True
define gui.about = _("")
define config.window_icon = "gui/window_icon.png"

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

    # Create the archives that will be compiled with the game. Scripts will contain the story code,
    # logic contains all of the Unscripted Core logic, and assets contains all of the required
    # images, audio files, etc.
    build.archive("scripts", "all")
    build.archive("assets", "all")
    build.archive("logic", "all")

    # To maintain compatibility with the license, a new archive is added to bundle the source code
    # to Unscripted Core. This archive will not appear in the demo version of the game as this code
    # shouldn't be accessible or licensed in a demo state, unless the demo_bundle_core flag in the
    # build settings is enabled. The source code is also available on GitHub at the following link:
    # https://github.com/UnscriptedVN/core.
    if not uconf["demo"]["demo"] or uconf["demo"]["demo_bundle_core"]:
        build.archive("source", "all")

    # Target any of the AliceOS-specific files first. The compiled targets and assets will be added
    # to the logic archive, while the source code will be added to the source archive.
    if (not uconf["demo"]["demo"]) or uconf["demo"]["demo_bundle_core"]:
        build.classify('game/System/**.aoscservice/**.rpy', "source")
        build.classify('game/System/**.aosapp/**.rpy', "source")

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
    build.classify("game/core/credits/**.kts", 'logic')

    # Bundle all of the assets together into a single package
    build.classify('game/assets/**', "assets")

    # Bundle TOML files
    build.classify('game/story/**.toml', "scripts")
    build.classify("game/core/**.toml", 'logic')

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
    build.classify("game/build.toml", 'scripts')

    # Target and bundle all of the Unscripted Core source files together in a convenient place.
    if not uconf["demo"]["demo"]:
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

    # Remove unnecessary developer files that come with the project.
    build.classify('docs/**', None)
    build.classify('doc_templates/**', None)
    build.classify('repo_assets/**.**', None)
    build.classify('unscripted.iconset/**.**', None)
    build.classify('nikola_src/**', None)
    build.classify('unscripted/**', None)
    build.classify('poetry.lock', None)
    build.classify('pyproject.toml', None)
    build.classify('README.md', None)
    build.classify('.vscode/**.**', None)
    build.classify('.git/**.**', None)
    build.classify('distribute/**', None)
    build.classify('**/cache/**', None)

    # Remove Ren'Py-generated log files
    build.classify("game/log.txt", None)
    build.classify("game/errors.txt", None)
    build.classify("game/traceback.txt", None)

    # Mark as documentation. If this build is the demo, exclude the
    # source code license.
    if uconf["demo"]["demo"]:
        build.classify('**/MPL.txt', None)

    build.documentation('*.html')
    build.documentation('*.txt')

# Used for itch.io uploads in Ren'Py Launcher. Unnecessary if
# using the distribute tool from Poetry (poetry run distribute).
define build.itch_project = "marquiskurt/unscripted"
