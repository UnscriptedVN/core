# Custom Statements

Unscripted Core introduces a few custom statements to make managing the game easier. This document is a running list of the statements added and their arguments, respectively.

## `musiclayer push track_name channel`

Push a given track to the specified audio channel, with respect to the music channel. If the music channel is playing, the music layer will determine where the audio position is and play the file from that point. Fades are automatically applied.

- **track_name**: The filepath or audio definition to play in the given channel.
- **channel**: The audio channel to play the track in.

## `musiclayer pop channel`

Pop the current track from the specified audio channel. Fades are automatically applied.

- **channel**: The audio channel to stop playing music from.
