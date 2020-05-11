# 
# inventory_hud.rpy
# Unscripted
# 
# Created by Marquis Kurt on 12/25/19.
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 

screen InventoryHUD():
    style_prefix "ASInterface"
    zorder 100
    modal True

    key 'e' action Hide("InventoryHUD")

    default items = []

    python:
        items = get_recent_items()

    if items:
        frame:
            xmaximum 900
            ymaximum 216
            xalign 0.5
            yalign 0.5

            hbox:
                yfill True
                for item in items:
                    button action [Function(inventory.useItem, item), Hide("InventoryHUD")]:
                        style "Inventory_button"
                        has vbox:
                            yfill True

                            add item.imageName
                            text "[item.name]" xalign 0.5

                button action [Show("ASInventoryManagerView"), Hide("InventoryHUD")]:
                    style "Inventory_button"
                    has vbox:
                        yfill True

                        add AS_DEFAULT_APP_DIR + "Inventories.aosapp/Resources/OpenMore.png"
                        text "Open Inventories" xalign 0.5
    else:
        on "show" action [Notify("You aren't carrying anything."), Hide("InventoryHUD")]

style Inventory_button:
    hover_background "#00000033"
    ysize 164