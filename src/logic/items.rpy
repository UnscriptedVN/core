#
# items.rpy
# Unscripted
#
# Created by Marquis Kurt on 9/27/19
# Copyright © 2019-2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = -20

# Define a set of inventory items to use in the game.
default inventory_items = {
    "usb_stick": ASInventoryItem(itemId="usb_stick",
                                 name="Project USB",
                                 description="The flash drive with the compiled project. Hopefully this runs alright.",
                                 imageName="gui/items/usb.png",
                                 canBeUsedOnce=False),
    "chess_piece": ASInventoryItem(itemId="chess_piece",
                                   name="Chess Piece",
                                   description="This was the chess piece Christina gave me that one morning when she told me that 'reality is whatever I perceive it to be'.\n\nI'm not sure what to do with it or how long I'm supposed to keep it for, though...",
                                   imageName="gui/items/chess_piece.png",
                                   canBeUsedOnce=False)
}
