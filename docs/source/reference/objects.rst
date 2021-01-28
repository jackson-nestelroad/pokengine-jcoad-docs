.. _object_functions:

################
Object Functions
################

If you are unsure how to use these object functions, check out the :ref:`objects tutorial<objects_tutorial>`.

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
        :type: sprite sheet

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
    :suffix: ([sprite][,slide])

    Creates a heavy object that can be pushed with the move "Strength."

    .. param:: sprite
        :type: sprite sheet
        :default: Region sprite

        Sprite that displays as the object to be pushed.

    .. param:: slide
        :type: 0/1
        :default: 0

        Slide in one direction on touch?

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

.. jcoad:function:: heal
    :suffix: (sprite,ball_width,ball_height[,ball_offset_x,ball_offset_y[,ball_margin_x,ball_margin_y]])

    Heals the player's party and creates a healing animation like the one used in a |Pokemon| Center.

    .. param:: sprite
        :type: sprite sheet

        Healing sprite sheet. |Poke| Balls must be in the lower left-hand corner. Machine must be in the upper left-hand corner.

    .. param:: ball_width
        :type: number

        Width of the individual ball sprite in pixels.

    .. param:: ball_height
        :type: number

        Height of the individual ball sprite in pixels.

    .. param:: ball_offset_x
        :type: number
        :default: 0

        Number of pixels to displace the drawing of the |Poke| Ball sprites in the x-direction.

    .. param:: ball_offset_y
        :type: number
        :default: 0

        Number of pixels to displace the drawing of the |Poke| Ball sprites in the y-direction.

    .. param:: ball_margin_x
        :type: number
        :default: 0 (touching)

        The number of pixels to draw between the |Poke| Balls in the x-direction.

    .. param:: ball_margin_y
        :type: number
        :default: 0 (touching)

        The number of pixels to draw between the |Poke| Balls in the y-direction.

.. jcoad:function:: shop
    :suffix: (item[:price],[item[:price],...])

    Creates a shop with the listed items and prices. An infinite list of items can be provided, with each item being separated by a comma.

    .. param:: item
        :type: string|number

        Item name or number to sell.

    .. param:: price
        :type: number
        :default: Default price

        Price for one item. This price cannot be less than the item's sell price.

.. jcoad:function:: height
    :suffix: (height)

    Creates an invisible wall with the specified height. If short enough, the wall can be jumped over.

    .. param:: height
        :type: number

        Height in pixels the player must jump to cross the tile.

.. jcoad:function:: execute
    :suffix: (triggers)

    Executes game triggers immediately when the map loads. To make the triggers tile specific, use :code:`if ontile` before this code. See :jcoad:var:`ontile`.

    See the :ref:`Game Triggers<game_triggers>` guide for a list of triggers to use.

    .. param:: triggers
        :type: string

        String of triggers to execute. The first trigger should not start with an ampersand, but all chained triggers should.