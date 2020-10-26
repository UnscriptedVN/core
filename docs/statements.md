# Custom Statements

Unscripted Core comes with a few custom-defined statements to make handling some tasks easier, such as managing the dynamic/adaptive music system.

## `phrase base mood char`

Updates the current music phrase with the specified parameters. These tracks will be queued into their respective channels and will player after the current phrase is finished.

### Parameters

- `base`: The filename or audio definition for the base track to use, or None for no track.
- `mood`: The filename or audio definition for the mood/scene track to use, or None for no track.
- `char`: The filename or audio definition for the character melody track to use, or None for no track.

## `killphrase`

Stop the music in all of the respective music channels immediately.
