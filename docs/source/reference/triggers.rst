.. _triggers:

########
Triggers
########

If you are unsure how to use these triggers, check out the :ref:`triggers tutorial<triggers_tutorial>`.

Programming
===========

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

Entity Manpulation
==================

.. jcoad:trigger:: freeze

    Freezes the target completely.

.. jcoad:trigger:: unfreeze

    Unfreezes the target.

.. jcoad:trigger:: destroy
    :suffix: [=target]

    Permanently destroys the target.

    .. param:: target
        :type: string
        :default: The current target

        Target to destroy.

.. jcoad:trigger:: jump
    :suffix: [=height]

    Causes the target to jump.

    .. param:: height
        :type: number
        :default: 8

        Number of pixels to jump.

.. jcoad:trigger:: direction
    :suffix: =direction

    Causes the target to face the given direction.

    .. param:: direction
        :type: short direction

        Direction to face.

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

.. jcoad:trigger:: follow
    :suffix: [=target]

    Forces the current target to follow another target.

    .. param:: target
        :type: string
        :default: Unfollows

        Target to follow

.. jcoad:trigger:: behindplayer

    Puts the current target behind the player.

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

    Creates a fading trail behind the target.

    .. param:: type
        :type: string
        :default: No trail

        Type of trail to draw.

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

Sprite Manipulation
===================

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

.. jcoad:trigger:: sprite
    :suffix: [name]=x,y,file,depth,image_x,image_y,image_width,image_height,frames,speed,loop,unsynced

    Adds a new (potentially animated) sprite to the map. See :jcoad:func:`animation`.

Player Events
=============

.. jcoad:trigger:: warp
    :suffix: =map,spawn

    Warps the player to a spawn point on a different map.

    .. param:: map
        :type: number

        Map ID to warp to.

    .. param:: spawn
        :type: number

        Spawn ID to warp to.

.. jcoad:trigger:: textbox
    :suffix: [=text]

    .. param:: text
        :type: string
        :default: Destroys the current textbox

        Text to display.

.. jcoad:trigger:: answers
    :suffix: =answer1[,answer2,...]

    Gives the player one or more answers to select. Answers should be separated by commas.

    .. param:: answer
        :type: string

        A single answer.

.. jcoad:trigger:: battle
    :suffix: =id

    Initiates a battle.

    .. param:: id
        :type: number

        Battle ID to initiate.

.. jcoad:trigger:: noblackout

    Prevents blacking out (losing a battle) from warping the user back to a heal point.

.. jcoad:trigger:: msg
    :suffix: [=target]

    ???

    .. param:: target
        :type: string
        :default: ???

        ???

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

.. jcoad:trigger:: trade
    :suffix: [whom]=for_whom

    Trades one type of |Pokemon| in the player's party for a new |Pokemon|.

    .. param:: whom
        :type: string

        Type of |Pokemon| needed to trade.

    .. param:: for_whom
        :type: pokemon

        |Pokemon| the player receives.

.. jcoad:trigger:: giveaway
    :suffix: =whom

    Gives away one |Pokemon| forever, removing it from the player's party

    .. param:: whom
        :type: string

        Type of |Pokemon| able to be given away.

.. jcoad:trigger:: money
    :suffix: =amount

    Adds money to the player's wallet.

    .. param:: amount
        :type: number

        Amount of money to add. Use a negative number to take money away.

.. jcoad:trigger:: coins
    :suffix: =amount

    Adds coins to the player's coin case.

    .. param:: amount
        :type: number

        Amount of coins to add. Use a negative number to take coins away.

.. jcoad:trigger:: starter
    :suffix: =pokemon

    Gives the |Pokemon| to the player as a starter. Players may only receive one starter per region.

    .. param:: pokemon
        :type: pokemon

        Starter |Pokemon| to give.

.. jcoad:trigger:: heal

    Heals the target's party.

.. jcoad:trigger:: badge
    :suffix: =badge

    Gives the user a gym badge.

    .. param:: badge
        :type: number

        Badge ID to give to the player.

.. jcoad:trigger:: achievement
    :suffix: =id

    Advances the given achievement by 1.

    .. param:: id
        :type: number

        Achievement ID to advance.

.. jcoad:trigger:: travel

    Activates the region travel menu.

.. jcoad:trigger:: pc

    Activates the PC.

.. jcoad:trigger:: halloffame
    :suffix: [=dex]

    Activates the Hall of Fame cutscene for the current region.

    .. param:: dex
        :type: 0/1
        :default: 0

        Display Dex progress at the end?

.. jcoad:trigger:: shop
    :suffix: =item[:price],[item[:price],...]

    Creates a shop with the listed items and prices. An infinite list of items can be provided, with each item being separated by a comma.

    .. param:: item
        :type: string|number

        Item name or number to sell.

    .. param:: price
        :type: number
        :default: Default price

        Price for one item. This price cannot be less than the item's sell price.

.. jcoad:trigger:: buy
    :suffix: =item[:price],[item[:price],...]

    Creates a shop with the listed items and prices, similar to :jcoad:trigger:`shop`. However, the player may not sell items here; only the buy option is activated.

    .. param:: item
        :type: string|number

        Item name or number to sell.

    .. param:: price
        :type: number
        :default: Default price

        Price for one item. This price cannot be less than the item's sell price.

.. jcoad:trigger:: sell

    Creates a menu that only allows the player to sell items.

.. jcoad:trigger:: replay
    :suffix: =id

    Replays a previous battle for the player. Basically initiates a battle where the player does nothing.

    .. param:: id
        :type: number

        Replay ID to watch.

.. jcoad:trigger:: rival

    Puts the "/rival" command into the player's chat.

.. jcoad:trigger:: cycle
    :suffix: =choice

    Causes the player to start riding a bicycle.

    .. param:: choice
        :type: yes/no
        :default: no

        Ride a bicycle?

.. jcoad:trigger:: surf
    :suffix: =choice

    Causes the target to start surfing.

    .. param:: choice
        :type: yes/no
        :default: no

        Surf?

.. jcoad:trigger:: safari
    :suffix: [=steps]

    Puts the player in a Safari Zone, where they have a certain number of steps before being warped away.

    .. param:: steps
        :type: number
        :default: Unsets the state

        Number of steps in the Safari Zone.

Game Appearance
===============

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




.. jcoad:trigger:: shake
    :suffix: [=x,y]

    Shakes the screen, as if there was an earthquake.

    .. param:: x
        :type: number
        :default: 0

        Number of pixels to shake horizontally.

    .. param:: y
        :type: number
        :default: 0

        Number of pixels to shake vertically.

.. jcoad:trigger:: lookat
    :suffix: [=x,y]

    Moves the game camera to the given coordinates on the map.

    .. param:: x
        :type: number
        :default: Player

        X-coordinate of target tile.

    .. param:: y
        :type: number
        :default: Player

        Y-coordinate of target tile.

.. jcoad:trigger:: weather
    :suffix: [=type]

    Sets the weather the player sees.

    .. param:: type
        :type: string
        :default: Resets to no weather
        :options: downpour, rain, storm, blizzard, snow, hail, hailstorm, fog, mist, spooky, sandstorm, soot, kyle, cherry, confetti, overcast, harsh sunlight, strong winds

        Type of weather.

Sounds
======

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

Client Properties
=================

.. jcoad:trigger:: zoom
    :suffix: [=scale]

    Changes the client's game window scale.

    .. param:: zoom
        :type: number
        :default: 2

        Zoom setting. Use :code:`1` for 100%, or use :code:`0.5` for 50%.
.. jcoad:trigger:: view
    :suffix: [=wxh]

    Sets the dimensions of the client's game window.

    .. param:: wxh
        :type: area|"normal"
        :default: normal

        Width and height of the game window. Use :code:`normal` to reset.


.. jcoad:trigger:: filter
    :suffix: [=type]

    Generates a filter over the game screen.

    .. param:: type
        :type: string
        :default: Remove any filter
        :options: crt, oldfilm, glitch, shockwave, bloom, ascii, godray, rgbsplitter, pixelate, underwater

        Filter to display.

Other
=====

.. jcoad:trigger:: refresh

    Refreshes the client's game. Equivalent to pressing F5 on desktop.

.. jcoad:trigger:: untile
    :suffix: [=target]

    ???

    .. param:: target
        :type: string
        :default: ???

        ???

.. jcoad:trigger:: unspot
    :suffix: [=target]

    ???

    .. param:: target
        :type: string
        :default: ???

        ???




