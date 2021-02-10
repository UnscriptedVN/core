#
# keymap.rpy
# Unscripted Core - Keymap
#
# Created by Marquis Kurt on 05/09/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#


init -10 python:
    # Remove the mouse scroll rollback function in the game when not in developer mode (or if the)
    if not config.developer and uconf["info"]["channel"] == "stable":
        config.keymap["rollback"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK']
    config.keymap["director"] = []                  # Disables the interactive director
    config.keymap["screenshot"].append("K_F12")     # Makes F12 an option screenshot key
    config.keymap["open_bug_reports"] = ['B']
    config.keymap["open_glossary"] = ["g"]
    config.keymap["open_log"] = ['l', 'L']
    config.keymap["open_desktop"] = ['d']
    if not config.developer:
        config.keymap["open_desktop"].append("D")


init -130 python:
    import webbrowser
    import logging

    def open_uvn_log():
        """Open the logs for Unscripted."""
        open_directory(log_filename)
        renpy.notify("The log file has been opened or selected in your file browser.")

    def open_desktop():
        """Open the AliceOS desktop shell."""
        if not in_splash:
            caberto.launch(transient=True)

    def open_issues_url():
        """Open the issue tracker to file a bug report."""
        url_key = "stable" if uconf["info"]["channel"] == "stable" else "beta"
        webbrowser.open(uconf["analytics"]["links"][url_key])
        renpy.notify("The bug reporter has been opened in your browser.")

    def buy_me_a_coffee():
        """Buys me a coffee."""
        webbrowser.open("https://ko-fi.com/marquiskurt")
        renpy.notify("The link has been opened in your browser.")

    def open_glossary_menu():
        """Open the Help menu to the glossary page."""
        try:
            renpy.run(
                ShowTransient(
                    "GlossaryAppUIView",
                    glossary=glossary_app.load_glossary(filepath="glossary.json")
                )
            )
        except:
            pass

    def open_api_docs():
        """Open the API documentation for Advanced Mode of the minigame."""
        url = "file://" + config.basedir + "/game/docs/index.html"
        webbrowser.open(url)
        renpy.notify("The API documentation has been opened in your browser.")

    # Create a custom keymap with the respective functions and details.
    _uvn_keymap = renpy.Keymap(
        open_log = open_uvn_log,
        open_desktop = open_desktop,
        open_bug_reports = open_issues_url,
        open_glossary = open_glossary_menu
    )

    # Append the keymap to the existing keymap.
    config.underlay.append(_uvn_keymap)
