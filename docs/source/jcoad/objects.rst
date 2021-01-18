.. _objects:

########
Objects
########

An **object** is a single 16x16 tile that holds its own special properties to add functionality to the game. The most common objects are simple, such as walls, ledges, or signs, but some objects can be more complex, such as doors, wraps, or stairs.

A lot of objects are pre-built within the Mapbuilder already, making your job as a developer even easier! However, you may want to be familiar with creating your own objects in case you need to.

Code Types
==========

All objects may contain jCoad to specify their behavior. However, there are two ways that code can be added to an object.

**Root code** is global code that is shared across all instances of that object placed on any map. Root code is great for code that must be repeated across multiple ties, such as walls or shorelines. Instead of writing the code in every object you place, you can write it just once and place that object everywhere you need that functionality.

**Instance code**, or just "code," is exclusive code to the single tile the object resides on. This code is written on a single object instance on a single map. Instance code is best for creating a unique event, such as NPC dialogue, that never needs to be repeated.

Objects can have *both* root code and instance code. Think of a sign. All signs are solid, but most signs hold a unique message. Therefore, a sign object would probably have the following jCoad:

.. code-block::
    :caption: Root Code

    solid()

.. code-block::
    :caption: Instance Code

    msg(I am a unique sign. Only I hold this message!)

All the jCoad in this guide can be used in both root code and instance code.

Object Functions
================

.. jcoad:function:: xy
    :suffix: (x,y)

    Offsets the display position of the object.

    .. param:: x
        :type: number

        Horizontal offset in pixels.

    .. param:: y
        :type: number

        Vertical offset in pixels.

.. jcoad:function:: solid
    :suffix: ([type])

    Makes the tile solid. Give a specific direction to customize which edge of the tile is solid.

    .. param:: type
        :type: direction
        :options: up, down, left, right, all, race, 0
        :default: all

.. jcoad:function:: msg
    :suffix: ([text])[&triggers]

    Displays a textbox message after interacting with the tile.

    .. param:: text
        :type: string
        :default: Empty textbox

.. jcoad:function:: answer
    :prefix: Answer=
    :suffix: ([text])[&triggers]
    :examples:
        msg(Take the fruit?)&answers=Yes,No
        Yes=answer(You took the fruit.)
        No=answer(You left the fruit.)

    Defines the response to specified answers. Use this code after specifying answer options with the :jcoad:trigger:`answers` trigger.

    .. param:: Answer
        :type: string

        Answer given by the player, such as "Yes" or "No."

    .. param:: text
        :type: string
        :default: No textbox

        Textbox response to the player's answer.

.. jcoad:function:: prints
    :suffix: (sprite[,frames[,speed[,fade[,directional]]]])

    Draws footprints when the player walks offtile.

    .. param:: sprite
        :type: sprite sheet

        Footprint sprite sheet.

    .. param:: frames
        :type: number

        Number of frames in the sprite sheet.

    .. param:: speed
        :type: number

        Speed of the animation.

    .. param:: fade
        :type: number

        Time to fade in milliseconds.

    .. param:: directional
        :type: 0/1

        Based on direction?

.. jcoad:function:: ledge
    :suffix: (direction[,jump_height[,distance]])

    Creates a ledge that can be hopped over in one direction.

    .. param:: direction
        :type: direction

        Direction to jump.

    .. param:: jump_height
        :type: number

        Height to jump in pixels.

    .. param:: distance
        :type: number

        Distance to jump in pixels. Should be in increments of 16.

.. jcoad:function:: spawn
    :suffix: (id,direction[,move])

    Creates a spawn point. Use on entrances, exits, or other spawn points.

    .. param:: id
        :type: number|"heal"

        A spawn ID number that is unique to the map. This ID can be used to warp players to this spawn point. If the user heals here, give :code:`heal` as the ID.

    .. param:: direction
        :type: direction

        Direction the player faces when spawning here.

    .. param:: move
        :type: 0/1

        Move one tile in the aforementioned direction?

.. jcoad:function:: warp
    :suffix: (map,spawn)

    Warps the player to a spawn point.

    .. param:: map
        :type: number

        Map ID to warp to.

    .. param:: spawn
        :type: number

        Spawn point ID to warp to.

.. jcoad:function:: door
    :suffix: (sprite,map,spawn)[&triggers]

    Creates a door object that animates when the user walks through it.

    .. param:: sprite
        :type: sprite sheet:

        Door sprite sheet.

    .. param:: map
        :type: number

        Map ID to warp to.

    .. param:: spawn
        :type: number

        Spawn point ID to warp to.

.. jcoad:function:: glow
    :suffix: (radius,color,[,flicker])

    Creates a circular glow effect around the tile.

    .. param:: radius
        :type: number

        Radius of the glow in pixels.

    .. param:: color
        :type: rgba

        Color of the glow.

    .. param:: flicker
        :type: unit interval

        Strength of the flicker, where 1 is full flicker and 0 is no flicker.

.. jcoad:function:: slide
    :suffix: ([direction])

    Causes the player to slide in the direction indicated until they hit a solid wall or warp.

    .. param:: direction
        :type: direction
        :default: Player will slide in the direction they were facing

        Direction to slide the player in. If omitted, the player will slide in the direction they are currently facing.

.. jcoad:function:: spin
    :suffix: ([direction])

    Causes the player to spin in the direction indicated until they hit a solid wall or warp.

    .. param:: direction
        :type: direction
        :default: Player will spin in the direction they were facing

        Direction to spin the player in.

.. jcoad:function:: cut
    :suffix: ([sprite])&triggers

    Creates a tree that can be cut down with the move "Cut."

    .. param:: sprite
        :type: sprite sheet
        :default: Region sprite

        Sprite that displays as the object to be cut.

.. jcoad:function:: strength
    :suffix: ([sprite])

    Creates a heavy object that can be pushed with the move "Strength."

    .. param:: sprite
        :type: sprite sheet
        :default: Region sprite

        Sprite that displays as the object to be pushed.

.. jcoad:function:: surf
    :suffix: ([direction])

    Allows the player to begin surfing here with the move "Surf."

    .. param:: direction
        :type: direction
        :default: Surf from any direction

        Direction to begin surfing in.

.. jcoad:function:: item
    :suffix: (id[,qty[,sprite]])

    Spawns an overworld item or |Pokemon|. If a |Pokemon| is spawned, it will be given to the player, not battled.

    .. param:: id
        :type: number|string|pokémon

        ID of the object to spawn. This can be an item ID number, an item name, or a :ref:`Pokémon Generation String<pokemon_generation>`.

    .. param:: qty
        :type: number

        Number of items to give.

    .. param:: sprite
        :type: sprite sheet
        :default: Region sprite

        Item sprite sheet.

.. admonition:: TO DO

    More to come!