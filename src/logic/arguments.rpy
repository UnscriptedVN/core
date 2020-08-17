#
# arguments.rpy
# Unscripted Core - Logic (Arguments)
#
# Created by Marquis Kurt on 05/22/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -10

init -100 python:
    import logging
    import toml
    import os

    arguments = {}

    # Load the arguments file if there is one.
    if renpy.loadable("arguments.toml"):
        logging.info("Arguments found. Loading from arguments file.")
        with renpy.file("arguments.toml") as arg_file:
            arguments = toml.load(arg_file)["args"]

    # Add the dreams folder.
    if "init-dreams" in arguments and arguments["init-dreams"]:
        logging.info("Creating dream folder...")
        try:
            os.mkdir("game/dreams/")
        except:
            pass

    # Disable running experiments if any are specified
    if "disable_experiments" in arguments:
        for experiment in arguments["disable_experiments"]:
            logging.info("Disabling experiment '%s'...", experiment)
            if experiment in uconf["labs"]["current"]:
                uconf["labs"]["current"].remove(experiment)

    if "mg-classic-mode" in arguments:
        logging.warn(
            "mg-classic-mode is no longer supported. The game will continue as normal."
        )
