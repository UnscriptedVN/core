#
# changes.rpy
# Unscripted Core - Changes
#
# Created by Marquis Kurt on 08/08/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -10

init python:
    from simplechanges import SimpleChangesParser
    import logging

    _changelog_obj = SimpleChangesParser(
        "CHANGELOG.changes" if uconf["info"]["channel"] == "stable" else "DEVCHANGES.changes"
    )
    _changelog_obj.parse()
    changelog_notes = _changelog_obj.latest

    if changelog_notes[0] not in uconf["info"]["version"]:
        persistent._viewed_release_notes = False
        logging.info("Ready to display release notes.")

    def did_view_changelog():
        persistent._viewed_release_notes = True
