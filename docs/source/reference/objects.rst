.. _object_functions:

################
Object Functions
################

If you are unsure how to use these object functions, check out the :ref:`objects tutorial<objects_tutorial>`.

Any object function ending with :code:`[&triggers]` may have an optional string of game triggers appended to them to execute alongside the function. See :ref:`triggers` for more information.

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
    :prefix: [name.]
    :suffix: ([text])[&triggers]

    Displays a textbox message after interacting with the tile.

    .. param:: name
        :type: string

        If a name is given with a dot separator, this object function operates like a property attached to an entity.

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
        :type: number|string
        :options: heal, cave, safari, fly

        A spawn ID number that is unique to the map. This ID can be used to warp players to this spawn point. Alternatively, one of the following strings can be given to indicate a special type of spawn point.

    .. param:: direction
        :type: direction

        Direction the player faces when spawning here.

    .. param:: move
        :type: 0/1

        Move one tile in the aforementioned direction?

.. jcoad:function:: warp
    :suffix: (map,spawn)[&triggers]

    Warps the player to a spawn point.

    .. param:: map
        :type: number

        Map ID to warp to.

    .. param:: spawn
        :type: number

        Spawn point ID to warp to.

    .. param:: triggers

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

.. jcoad:function:: execute
    :suffix: (triggers)

    Executes game triggers immediately when the map loads. To make the triggers tile specific, use :code:`if ontile` before this code. See :jcoad:cond:`ontile`.

    See the :ref:`Triggers<triggers>` reference list for a list of triggers to use.

    .. param:: triggers
        :type: string

        String of triggers to execute. The first trigger should not start with an ampersand, but all chained triggers should.

.. jcoad:function:: sprite
    :prefix: [name=]
    :suffix: (image[,depth[,x,y,width,height[,unsynced]]])

    Draws a sprite on the tile. This function is able to "crop" a sprite out of the given sprite sheet or tileset by using the four positional parameters parameters. The coordinates of the top-left corner of the sprite you want to draw should be given to the :code:`x` and :code:`y` parameters, and the width and height of the sprite should be given to the :code:`width` and :code:`height` parameters.

    .. param:: name
        :type: string

        Name of the sprite to refer to it elsewhere.

    .. param:: image
        :type: sprite sheet|tileset

        Sprite source, which could be a large tileset or an uploaded sprite sheet.

    .. param:: depth
        :type: depth

        Depth of the sprite.

    .. param:: x
        :type: number

        The x-position of the sprite in the image source.

    .. param:: y
        :type: number

        The y-position of the sprite in the image source.

    .. param:: width
        :type: number

        Width of the sprite in the image source.

    .. param:: height
        :type: number

        Height of the sprite in the image source.

    .. param:: unsynced
        :type: 0/1

        Meaningless.

.. jcoad:function:: animation
    :prefix: [name=]
    :suffix: (image[,depth[,x,y,width,height[,frames[,speed[,loop[,unsynced]]]]]])

    Draws an animated sprite on the tile. Very similar to :jcoad:func:`sprite`, but multiple frames are ripped from the image source to create an animation. All animation frames should be the same size, and they should be stored sequentially and horizontally in their sprite sheet. Each frame has an area of :code:`width x height` pixels, and the overall width of the image source should be at least :code:`width x frames`.

    .. param:: name
        :type: string

        Name of the animation to refer to it elsewhere.

    .. param:: depth
        :type: depth

        Depth of the sprite.

    .. param:: x
        :type: number

        The x-position of the first frame's top-left corner in the image source.

    .. param:: y
        :type: number

        The y-position of the first frame's top-left corner in the image source.

    .. param:: width
        :type: number

        Width of a single frame.

    .. param:: height
        :type: number

        Height of a single frame.

    .. param:: frames
        :type: number

        Number of frames.

    .. param:: speed
        :type: number

        Speed of the animation in frames per second.

    .. param:: loop
        :type: number|"loop"

        Number of times to loop the animation. Use :code:`loop` to loop indefinitely.

    .. param:: unsynced
        :type: 0/1
        :default: 0

        Should the animation be unsynced with other animations of the same type?

.. jcoad:function:: npc
    :prefix: [name=]
    :suffix: (skin[,direction[,path]])

    Spawns an NPC (non-playable character) on the tile.

    .. param:: name
        :type: string

        Name of the NPC to refer to it elsewhere. It is heavily recommended to use :code:`%random%`, rather than your own name, as much as possible.

    .. param:: skin
        :type: skin

        Skin ID number, which is the NPC's overworld sprite.

    .. param:: direction
        :type: direction

        The NPC's starting direction.

    .. param:: path
        :type: area

        The NPC's path boundary.

.. jcoad:function:: glow
    :prefix: [name=]
    :suffix: (radius,color[,flicker])

    Creates a circular glow effect around the tile.

    .. param:: name
        :type: string

        Name of the glow to refer to it elsewhere.

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
        :type: direction|"stop"
        :default: Player will slide in the direction they were facing

        Direction to slide the player in. Use :code:`stop` to use this tile to stop a player if they are sliding.

.. jcoad:function:: spin
    :suffix: ([direction])

    Causes the player to spin in the direction indicated until they hit a solid wall or warp.

    .. param:: direction
        :type: direction|"stop"
        :default: Player will spin in the direction they were facing

        Direction to spin the player in. Use :code:`stop` to use this tile to stop a player if they are sliding.

.. jcoad:function:: item
    :suffix: (id[,amount[,sprite]])

    Spawns an overworld item or |Pokemon|. If a |Pokemon| is spawned, it will be given to the player, not battled.

    .. param:: id
        :type: number|string|pokémon

        ID of the object to spawn. This can be an item ID number, an item name, or a :ref:`Pokémon Generation String<pokemon_generation>`.

    .. param:: amount
        :type: number

        Number of items to give.

    .. param:: sprite
        :type: sprite sheet|"hidden"
        :default: Region sprite

        Item sprite sheet. Use :code:`hidden` to make this item invisible.

.. jcoad:function:: encounter
    :suffix: (type)

    .. param:: type
        :type: string

        Allows encounters of the given type to pop up on this tile. Encounters are created and named for each map.

.. jcoad:function:: surf
    :suffix: ([direction])

    Allows the player to begin surfing here with the move "Surf."

    .. param:: direction
        :type: direction
        :default: Surf from any direction

        Direction to begin surfing in.

.. jcoad:function:: cut
    :suffix: ([encounter_list[,sprite]])[&triggers]

    Creates a tree that can be cut down with the move "Cut."

    .. param:: encounter_list
        :type: string

        Encounter list to use when player cuts down the object.

    .. param:: sprite
        :type: sprite sheet
        :default: Region sprite

        Sprite that displays as the object to be cut.

.. jcoad:function:: strength
    :suffix: ([sprite][,slide])[&triggers]

    Creates a heavy object that can be pushed with the move "Strength."

    .. param:: sprite
        :type: sprite sheet
        :default: Region sprite

        Sprite that displays as the object to be pushed.

    .. param:: slide
        :type: 0/1
        :default: 0

        Slide in one direction on touch?

.. jcoad:function:: rocksmash
    :suffix: ([encounter_list[,sprite]])[&triggers]

    Creates an object that may be destroyed with the move "Rock Smash."

    .. param:: encounter_list
        :type: string

        Encounter list to use when player smashes the object.

    .. param:: sprite
        :type: sprite sheet
        :default: Region sprite

        Sprite that displays as the object to be smashed.

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

.. jcoad:function:: moveto
    :suffix: (x,y[,direction])

    Moves the player to the given coordinates by taking the straight-line path.

    .. param:: x
        :type: number

        X-coordinate of the tile to move to.

    .. param:: y
        :type: number

        Y-coordinate of the tile to move to.

    .. param:: direction
        :type: direction
        :default: The direction the player entered the tile facing

        The direction the player should face while moving.

.. jcoad:function:: grass
    :suffix: (image,frames,speed[,overlay_sprite[,loop]])[&triggers]

    Creates an animation and overlay over the player while they are on the tile.

    .. param:: image
        :type: sprite sheet

        Sprite sheet with overlay animation. Frames should be evenly spaced horizontally.

    .. param:: frames
        :type: number

        Number of frames in the animation sprite sheet.

    .. param:: speed
        :type: number

        Speed of the animation in frames per second.

    .. param:: overlay_sprite
        :type: sprite sheet

        Single static sprite to overlay over player.

    .. param:: loop
        :type: "loop"

        Use :code:`loop` to loop the animation indefinitely.

.. jcoad:function:: ripple
    :suffix: (animation,frames,speed[,loop])

    Creates an animation over the player while they are on the tile.

    .. param:: image
        :type: sprite sheet

        Sprite sheet with overlay animation. Frames should be evenly spaced horizontally.

    .. param:: frames
        :type: number

        Number of frames in the animation sprite sheet.

    .. param:: speed
        :type: number

        Speed of the animation in frames per second.

    .. param:: loop
        :type: "loop"

        Use :code:`loop` to loop the animation indefinitely.