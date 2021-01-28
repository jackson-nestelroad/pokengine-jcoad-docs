.. _triggers:

########
Triggers
########

If you are unsure how to use these triggers, check out the :ref:`triggers tutorial<triggers_tutorial>`.

.. jcoad:trigger:: pause
    :suffix: =ms

    Pauses trigger execution for a given amount of time.

    .. param:: ms
        :type: number

        Time in milliseconds to wait before preceding.

.. jcoad:trigger:: with
    :suffix: [=target]

    Targets the following triggers on the given entity.

    .. param:: target
        :type: string
        :default: Re-target the player.

        New target name.

.. jcoad:trigger:: var
    :suffix: [name]=value

    Updates the variable.

    .. param:: name
        :type: string

        **REQUIRED**. Name of the variable.

    .. param:: value
        :type: string

        New value of the variable.

.. jcoad:trigger:: mapvar
    :suffix: [name]=value

    Updates the map variable.

    .. param:: name
        :type: string

        **REQUIRED**. Name of the variable.

    .. param:: value
        :type: string

        New value of the variable.

.. jcoad:trigger:: ev
    :suffix: [name]=value

    Updates the event variable.

    .. param:: name
        :type: string

        **REQUIRED**. Name of the variable.

    .. param:: value
        :type: string

        New value of the variable.

.. jcoad:trigger:: jump
    :suffix: [=height]

    Causes the target to jump.

    .. param:: height
        :type: number
        :default: 8

        Number of pixels to jump.

.. jcoad:trigger:: path
    :suffix: [=path]

    Moves the target along the given path.

    .. param:: path
        :type: path
        :default: Unsets the current path

        Path for the target.

.. jcoad:trigger:: speed
    :suffix: [=percentage]

    Sets the player's speed.

    .. param:: percentage
        :type: percentage
        :default: 100

        Percentage of normal speed. Use :code:`50` for half speed, or use :code:`200` for double speed.

.. jcoad:trigger:: zoom
    :suffix: [=scale]

    Changes the client's game window scale.

    .. param:: zoom
        :type: number
        :default: 2

        Zoom setting. Use :code:`1` for 100%, or use :code:`0.5` for 50%.

.. jcoad:trigger:: icon
    :suffix: [=id]
    :examples:
        1 = !               13. haha
        2 = ...             14-18. numbers 1-5
        3 = :)              19. poisoned
        4 = music note      20. o_o
        5 = ,               21. shaking head
        6 = ^_^             22. ?
        7 = <3              23. asleep
        8 = :[              24. sweat drop
        9 = :D              25. skull
        10 = <><            26. big red !
        11 = >:(            27. eye (spectating)
        12. battle icon     28. Dx

    Places an emoticon above the player's head.

    .. param:: id
        :type: number
        :default: Removes any icon

        Icon ID to display.

.. jcoad:trigger:: view
    :suffix: [=wxh]

    Sets the dimensions of the client's game window.

    .. param:: wxh
        :type: area|"normal"
        :default: normal

        Width and height of the game window. Use :code:`normal` to reset.

.. jcoad:trigger:: fadeout
    :suffix: [=color]

    Fades the screen out to a solid color.

    .. param:: color
        :type: hex
        :default: Black

        Solid color to fade out to.

.. jcoad:trigger:: fadein
    :suffix: [=color]

    Fades the screen in, starting from the given color.

    .. param:: color
        :type: hex
        :default: Black

        Solid color to fade in from.

.. jcoad:trigger:: flash
    :suffix: [=color]

    Flashes the screen with a solid color.

    .. param:: color
        :type: hex
        :default: White

        Solid color to flash.

.. jcoad:trigger:: direction
    :suffix: =direction

    Causes the target to face the given direction.

    .. param:: direction
        :type: short direction

        Direction to face.

.. jcoad:trigger:: freeze

    Freezes the target completely.

.. jcoad:trigger:: unfreeze

    Unfreezes the target.

.. jcoad:trigger:: warp
    :suffix: =map,spawn

    Warps the player to a spawn point on a different map.

    .. param:: map
        :type: number

        Map ID to warp to.

    .. param:: spawn
        :type: number

        Spawn ID to warp to.

.. jcoad:trigger:: xy
    :suffix: =x,y

    Instantly warps the target to the specified coordinates on the current map.

    .. param:: x
        :type: number

        X-coordinate to warp to.

    .. param:: y
        :type: number

        Y-coordinate to warp to.

.. jcoad:trigger:: moveto
    :suffix: =x,y[,direction]

    Moves the target to the specified coordinates on the current map by taking the straight-line path.

    .. param:: x
        :type: number

        X-coordinate to move to.

    .. param:: y
        :type: number

        Y-coordinate to move to.

    .. param:: direction
        :default: Current direction

        Direction to face while moving.

.. jcoad:trigger:: outfit
    :suffix: =skin

    Sets the target's skin.

    .. param:: skin
        :type: skin

        Skin ID to change to.

.. jcoad:trigger:: texture
    :suffix: =sprite

    Sets the target's texture.

    .. param:: texture
        :type: sprite sheet

        Texture sprite to change to.

.. jcoad:trigger:: skincolor
    :suffix: [=id]

    Sets the target's skin color.

    .. param:: id
        :type: number
        :default: 0

        Skin color ID to change to.

.. jcoad:trigger:: ally
    :suffix: [=ally1 [ally2 [ally3...]]]

    Sets the target's allies, or following entities.

    .. param:: ally
        :type: skin

        Overworld skin of following ally. For multiple allies, separate with spaces.

.. jcoad:trigger:: battle
    :suffix: =whom

    ???

    .. param:: whom
        :type: ???

        ???

.. jcoad:trigger:: noblackout

    ???

.. jcoad:trigger:: textbox
    :suffix: [=text]

    .. param:: text
        :type: string
        :default: Destroys the current textbox

        Text to display.

.. jcoad:trigger:: destroy
    :suffix: [=target]

    Permanently destroys the target.

    .. param:: target
        :type: string
        :default: The current target

        Target to destroy.

.. jcoad:trigger:: floating
    :suffix: [=height]

    Causes the target to float.

    .. param:: height
        :type: number|"yes"
        :default: Stops floating

        Number of pixels high to float. :code:`yes` defaults to 10 pixels.

.. jcoad:trigger:: spin
    :suffix: [=choice]

    Causes the target to spin.

    .. param:: spin
        :type: yes/no
        :default: no

        Should the target spin?

.. jcoad:trigger:: solid
    :suffix: [=choice]

    Turns the target solid.

    .. param:: choice
        :type: yes/no
        :default: no

        Should the target be solid?

.. jcoad:trigger:: print
    :suffix: [=type]

    ???

    .. param:: type
        :type: ???
        :default: Unsets

        ???

.. jcoad:trigger:: msg
    :suffix: [=target]

    ???

    .. param:: target
        :type: string
        :default: ???

        ???

.. jcoad:trigger:: follow
    :suffix: [=target]

    Forces the current target to follow another target.

    .. param:: target
        :type: string
        :default: Unfollows

        Target to follow

.. jcoad:trigger:: behindplayer

    Puts the current target behind the player.

.. jcoad:trigger:: outline
    :suffix: [=color]

    Draws a colored outline around the target.

    .. param:: color
        :type: rgb
        :default: Removes outline

        Color of outline.

.. jcoad:trigger:: color
    :suffix: [=color]

    Sets the glow color of the target.

    .. param:: color
        :type: rgb
        :default: Removes outline

        Glow color. Three RGB values separated by commas.

.. jcoad:trigger:: glide
    :suffix: [=choice]

    Causes the target to glide, which removes the target's walking animation.

    .. param:: choice
        :type: yes/no
        :default: no

        Should the target glide?

.. jcoad:trigger:: wtw
    :suffix: [=choice]

    Causes the target to walk through walls.

    .. param:: choice
        :type: yes/no
        :default: no

        Should the target walk through walls?

.. jcoad:trigger:: repel
    :suffix: [=choice]

    Causes the target to repel wild |Pokemon| encounters.

    .. param:: choice
        :type: yes/no
        :default: no

        Should the target have repel activated?

.. jcoad:trigger:: depth
    :suffix: [=z]

    Sets the depth of the target.

    .. param:: z
        :type: number
        :default: 0

        Target's new depth.

.. jcoad:trigger:: opacity
    :suffix: [=percentage]

    Sets the target's opacity.

    .. param:: percentage
        :type: percentage
        :default: 100

        Target's opacity.

.. jcoad:trigger:: animate
    :suffix: [=percentage]

    Forces the target to animate.

    .. param:: percentage
        :type: percentage
        :default: 100

        Percentage of the normal speed to animate at.

.. jcoad:trigger:: frame
    :suffix: [=frame]

    Forces the target to pause on the given frame number.

    .. param:: frame
        :type: number
        :default: 0

        Frame number to pause on.

.. jcoad:trigger:: filter
    :suffix: [=type]

    Generates a filter over the game screen.

    .. param:: type
        :type: string:
        :default: Remove any filter
        :options: crt, oldfilm, glitch, shockwave, bloom, ascii, godray, rgbsplitter, pixelate, underwater

        Filter to display.

.. jcoad:trigger:: palette
    :suffix: [=hexhex]

    Changes the game's palette. Used in retro maps.

    .. param:: hexhex
        :type: string
        :default: Unsets

        Two colors, formatted as twelve hexadecimal digits (:code:`[0-F]{12}`) all together. The first six digits represent the primary color, and the second six digits represent the secondary color.

.. jcoad:trigger:: dawn

    Changes the game time to dawn (06:00).

.. jcoad:trigger:: day

    Changes the game time to day (12:00).

.. jcoad:trigger:: dusk

    Changes the game time to dusk (18:00).

.. jcoad:trigger:: night

    Changes the game time to night (20:00).

.. jcoad:trigger:: time
    :suffix: [=h:m]

    Changes the game time.

    .. param:: h:m
        :type: string
        :default: Resets to server time

        Time in 24-hour format.

.. jcoad:trigger:: lighting
    :suffix: [=color]

    Changes the game's overlay lighting.

    .. param:: color
        :type: rgb
        :default: Resets to map or time lighting

        Color of overlay.

.. jcoad:trigger:: sfx
    :suffix: =sound

    Plays a sound file.

    .. param:: sound
        :type: string

        Some name of a :code:`.ogg` file.

.. jcoad:trigger:: track
    :suffix: [=track]

    Plays a sound track.

    .. param:: track
        :type: string
        :default: Stops playing any track

        Track to play. Track can be some name of a :code:`.ogg` file, or it can be a SoundCloud song. Use :code:`sc:username/songname` to play from SoundCloud.

.. jcoad:trigger:: cry
    :suffix: =pokemon

    Plays a |Pokemon| cry.

    .. param:: pokemon
        :type: skin

        Plays a |Pokemon|'s cry.

.. jcoad:trigger:: item
    :suffix: =item[,amount]

    Gives the player a given amount of some item.

    .. param:: item
        :type: string|number

        Name or ID number of the item.

    .. param:: amount
        :type: number
        :default: 1

        Number of items to give. Use a negative number to take items away from the player.

.. jcoad:trigger:: mon
    :suffix: =pokemon

    Gives the player the generated |Pokemon|.

    .. param:: pokemon
        :type: pokémon

        |Pokemon| to give.

.. jcoad:trigger:: show
    :suffix: =pokemon

    Shows the player a |Pokemon|.

    .. param:: pokemon
        :type: ???

        |Pokemon| to show.

.. admonition:: TODO

    More to come.