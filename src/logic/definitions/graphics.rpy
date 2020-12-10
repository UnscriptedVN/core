#
# graphics.rpy
# Unscripted
#
# Created by Marquis Kurt on 7/7/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

# MARK: UI Elements
image ctc:
    block:
        get_feather_icon("chevrons-right")
        size (24, 24) xoffset 4
        alpha 0.0
        linear 0.75 alpha 1.0
        linear 0.75 alpha 0.0
        repeat

# MARK: Backgrounds
image bg cafe = "images/bg/cafe/day.jpg"
image bg cafe_morning = "images/bg/cafe/morning.jpg"
image bg cafe_night = "images/bg/cafe/night.jpg"

image bg outdoor main = "images/bg/outdoor/main.jpg"
image bg outdoor secondary = "images/bg/outdoor/secondary.jpg"
image bg outdoor station = "images/bg/outdoor/station.jpg"
image bg outdoor street = "images/bg/outdoor/street.jpg"
image bg outdoor apartment = "images/bg/apartment/lot.jpg"
image bg outdoor apartment_night = "images/bg/apartment/lot_night.jpg"

image bg town arcade = "images/bg/town/arcade.jpg"

image bg nature outlook = "images/bg/nature/outlook.jpg"
image bg nature outlook_morning = "images/bg/nature/outlook_morning.jpg"
image bg nature riverside_apmidi = "images/bg/nature/riverside_afternoon.jpg"

image bg nature beach = "images/bg/nature/beach.jpg"
image bg nature beach_night = "images/bg/nature/beach_night.jpg"

image bg apartment morning = "images/bg/apartment/living_morning.jpg"
image bg apartment day = "images/bg/apartment/living_day.jpg"
image bg apartment night = "images/bg/apartment/living_night.jpg"
image bg apartment room_day = "images/bg/apartment/room_day.jpg"
image bg apartment room_night = "images/bg/apartment/room_night.jpg"

image bg mc_apartment entrance = "images/bg/mc/entrance.jpg"
image bg mc_apartment entrance_morning = "images/bg/mc/entrance_morning.jpg"
image bg mc_apartment entrance_night = "images/bg/mc/entrance_night.jpg"
image bg mc_apartment day = "images/bg/mc/landing.jpg"
image bg mc_apartment morning = "images/bg/mc/landing_morning.jpg"
image bg mc_apartment night = "images/bg/mc/landing_night.jpg"
image bg mc_apartment bedroom = "images/bg/mc/bedroom.jpg"
image bg mc_apartment bedroom_night = "images/bg/mc/bedroom_night.jpg"

# image main_menu = "gui/main_menu.png"

# MARK: CGs

# TV CG
image bg cg1 = "images/cg/cg1/base.png"
image cg cg1_fg1 = "images/cg/cg1/fg1.png"
image cg cg1_fg2 = "images/cg/cg1/fg2.png"
image cg cg1_fg3 = "images/cg/cg1/fg3.png"

# Kanban Board CG
image bg cg2 = "images/cg/cg2/base.png"
image cg cg2_fg1 = "images/cg/cg2/fg1.png"
image cg cg2_fg2 = "images/cg/cg2/fg2.png"
image cg cg2_fg3 = "images/cg/cg2/fg3.png"

# Meredith Reveal CG
image bg cg2b = "images/cg/cg2b/base.png"
image cg cg2b_fg1:
    zoom 0.5
    "images/cg/cg2b/fg1.png"

# Zen'no TV CG
image bg cg3 = "images/cg/cg3/base.png"
image cg cg3_fg1 = "images/cg/cg3/fg1.png"
image cg cg3_fg2 = "images/cg/cg3/fg2.png"

# MARK: Credits
image credits_with_love = "images/bg/special/clove.png"

image bg blueprint = "images/bg/special/blueprint.png"

# MARK: Christina
layeredimage christina:

    group base:
        attribute standard default:
            "christina/base.png"
        attribute alt:
            "christina/base_alt.png"

    group brows:
        attribute b1:
            "christina/eyebrows1.png"
        attribute b2:
            "christina/eyebrows2.png"
        attribute b3:
            "christina/eyebrows3.png"

    group eyes:
        attribute e1:
            "christina/eyes1.png"
        attribute e2:
            "christina/eyes2.png"

    group mouths:
        attribute mf1:
            "christina/mouthfrown1.png"
        attribute mf2:
            "christina/mouthfrown2.png"

        attribute mo1:
            "christina/mouthopen1.png"
        attribute mo2:
            "christina/mouthopen2.png"

        attribute ms1:
            "christina/mouthsmile1.png"
        attribute ms2:
            "christina/mouthsmile2.png"
        attribute ms3:
            "christina/mouthsmile3.png"
        attribute ms4:
            "christina/mouthsmile4.png"
        attribute ms5:
            "christina/mouthsmile5.png"

    group extras:
        attribute blush:
            "christina/blush.png"

# MARK: Zen'no
layeredimage zenno:

    group base:
        attribute standard default:
            "zenno/base.png"

    group brows:
        attribute b1:
            "zenno/eyebrow1.png"
        attribute b2:
            "zenno/eyebrow2.png"
        attribute b3:
            "zenno/eyebrow3.png"

    group eyes:
        attribute e1:
            "zenno/eye_open.png"
        attribute e2:
            "zenno/eye_open2.png"
        attribute e3:
            "zenno/eye_midopen.png"
        attribute e4:
            "zenno/eye_closed.png"

    group mouths:
        attribute mf:
            "zenno/mouth_frown.png"

        attribute mmo:
            "zenno/mouth_midopen.png"

        attribute mo1:
            "zenno/mouth_open1.png"
        attribute mo2:
            "zenno/mouth_open2.png"
        attribute mo3:
            "zenno/mouth_open3.png"

        attribute msmile:
            "zenno/mouth_smile.png"

        attribute ms:
            "zenno/mouth_straight.png"

    group extras:
        attribute blush:
            "zenno/blush.png"

# MARK: Katorin
layeredimage katorin:

    group base:
        attribute standard default:
            "katorin/base.png"

    group brows:
        attribute b1:
            "katorin/eyebrows1.png"
        attribute b2:
            "katorin/eyebrows2.png"
        attribute b3:
            "katorin/eyebrows3.png"

    group eyes:
        attribute e1:
            "katorin/eyes.png"
        attribute e2:
            "katorin/eyesmidopen.png"

    group mouths:
        attribute mf1:
            "katorin/mouthfrown.png"
        attribute mf2:
            "katorin/mouthfrown2.png"

        attribute mc:
            "katorin/mouthcurvy.png"

        attribute mo1:
            "katorin/mouthopen1.png"
        attribute mo2:
            "katorin/mouthopen2.png"

        attribute ms1:
            "katorin/mouthsmile1.png"
        attribute ms2:
            "katorin/mouthsmile2.png"

    group extras:
        attribute blush:
            "katorin/blush.png"


layeredimage fira:

    group base:
        attribute standard default:
            "fira/base.png"

        # Variant where the hood is on.
        attribute hooded:
            "fira/base_hood.png"

    group brows:
        attribute b1:
            "fira/eyebrows_1.png"
        attribute b2:
            "fira/eyebrows_2.png"
        attribute b3:
            "fira/eyebrows_3.png"
        attribute b4:
            "fira/eyebrows_4.png"
        attribute b5:
            "fira/eyebrows_5.png"

    group eyes:
        attribute e1:
            "fira/eyes_1.png"
        attribute e2:
            "fira/eyes_2.png"
        attribute e3:
            "fira/eyes_3.png"
        attribute e4:
            "fira/eyes_4.png"

    group mouths:
        attribute mf1:
            "fira/m_frown1.png"
        attribute mf2:
            "fira/m_frown2.png"
        attribute mf3:
            "fira/m_frown3.png"
        attribute mf4:
            "fira/m_frown4.png"

        attribute mo1:
            "fira/m_O1.png"
        attribute mo2:
            "fira/m_O2.png"
        attribute mo3:
            "fira/m_O3.png"

        attribute ms1:
            "fira/m_smile1.png"
        attribute ms2:
            "fira/m_smile2.png"
        attribute ms3:
            "fira/m_smile3.png"
        attribute ms4:
            "fira/m_smile4.png"

    group effects:
        attribute blush:
            "fira/blush.png"

    # Add the hood shadow if using the hooded base.
    always if_any "hooded":
        "fira/effect_hood.png"

    # Add the glasses automatically if using the regular base.
    always if_any "standard":
        "fira/glasses.png"
