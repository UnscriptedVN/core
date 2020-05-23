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

    arguments = {}

    if renpy.loadable("arguments.toml"):
        logging.info("Arguments found. Loading from arguments file.")
        with renpy.file("arguments.toml") as arg_file:
            arguments = toml.load(arg_file)["args"]

    if "disable_experiments" in arguments:
        for experiment in arguments["disable_experiments"]:
            expr_name = experiment.replace("_", "-")
            logging.info("Disabling experiment '%s'...", expr_name)
            if expr_name in uconf["labs"]["current"]:
                uconf["labs"]["current"].remove(expr_name)
