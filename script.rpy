#
# script.rpy
# Unscripted
#
# Created by Marquis Kurt on 07/01/19.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

label start:
    python:
        import logging

        # Reset the names to question marks.
        cname = zname = mname = kname = mname = "???"

        # Disable the quick menu.
        quick_menu = False

        # Get the player's name, pronouns, and language and create a new Player object.
        player_name, player_pronouns, player_language = renpy.call_screen("ProfileNameView")
        player = Player(player_name)
        logging.info("Created player %s." % (player_name))

        # Update the player's personal pronouns and the player's programming language.
        player.update_pronouns(player_pronouns)
        player.update_language(player_language)
        logging.info("Pronouns and language for player %s updated." % (player_name))

        # Grab the personal pronouns that the player has selected.
        pronoun_subj = player.pronouns['subject']
        pronoun_obj = player.pronouns['object']
        pronoun_poss = player.pronouns['possessive']

        # Create conjugations for pronouns for state of being (they're/she's) and state of being
        # in the past (they've/he's [been]).
        conj_being = pronoun_subj + ("'re" if pronoun_subj == "they" else "'s")
        conj_being_past = pronoun_subj + ("'ve" if pronoun_subj == "they" else "'s")

        # Create conjugations for possessive pronouns if used in an "alternate" way from what is
        # listed in the setup screen (hers -> her).
        conj_pos_alt = pronoun_poss[:-1] if pronoun_poss == "hers" else pronoun_poss

        # Clear the AliceOS inventory.
        for item in inventory.export():
            inventory.removeItem(item)

        # Request for the notification permissions to receive in-game emails.
        if "opt-in-quickmail" not in uconf["labs"]["current"]:
            emails.requestPermission(forPermission=AS_REQUIRES_NOTIFICATIONKIT)

        # Update the email location to point to the emails folder.
        emails.email_location = "story/emails/"

        # Finally, update the playing state.
        change_playing_state()

    # Display the splash and fade into the story
    scene splash
    stop music fadeout 1.5
    show black with fade
    $ quick_menu = True

    # Run the story script bootstrapper. This bootstrapper points to the story scripts and will
    # execute the story. As this code is not open-source, we call the bootstrapper instead of
    # directly calling it here.
    #
    # Mods can write their own verson of story_bootstrap and override the story to the mod's story.
    call story_bootstrap

    # Finally, call the credits at the end of the script.
    call credits

    # If the survey link key in the build configuration is set, prompt the user to fill out the
    # form.
    python:
        import webbrowser

        if "survey_link" in uconf["analytics"]:
            dismiss_callback = [Function(webbrowser.open, uconf["analytics"]["survey_link"]),
                    Return('didDismissAlert')]
            renpy.call_screen("ASNotificationAlert",
                              "Feedback Requested",
                              "The developer has requested that you fill out a feedback survey."\
                              + " Clicking 'OK' will open the survey in your browser.",
                              onDismissCallback=dismiss_callback)
    return
