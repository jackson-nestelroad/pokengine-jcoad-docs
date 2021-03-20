.. _types:

##########
Data Types
##########

jCoad does not really have data types, but putting arguments into the proper format for object functions, properties, and triggers is absolutely necessary for your code to work properly. Use this guide to understand how to enter arguments into your jCoad.

.. jcoad:type:: 0/1

    A binary digit, representing a boolean value. 1 represents "yes," "on," or "true," while 0 represents "no," "off," or "false."

.. jcoad:type:: area

    An area, represented by two integers separated by an "x." Use the format :code:`mxn`, where :code:`m` and :code:`n` are integers.

.. jcoad:type:: depth
    :examples:
        map+16
        void+5
        fore-5
        bottom+293
        fore
        back

    A depth string that indicates the depth of a sprite or animation drawn in the game. Depth strings consist of a base position and an optional offset.

    - :code:`map`/:code:`map+n`/:code:`map-n` --- Depth offset is relative to the base position on the map. :code:`n` is the number of pixels in front of the object the player needs to be to appear in front of it.
    - :code:`void`/:code:`void+n`/:code:`void-n` --- Depth offset is relative to the void, or the map background.
    - :code:`fore`/:code:`fore+n`/:code:`fore-n` --- Depth offset is relative to just above the foreground, or always above the player.
    - :code:`back`/:code:`back+n`/:code:`back-n` --- Depth offset is relative to just above the background, or always behind the player.
    - :code:`bottom`/:code:`bottom+n`/:code:`bottom-n` --- Depth offset is relative to above the map, but behind the shadows.

    The pixel offsets (:code:`+n` or :code:`-n`), especially when working with a depth other than :code:`map`, are primarily used to place objects relative to one other.

.. jcoad:type:: direction
    :options: up, down, left, right

    A direction the player can face.

.. jcoad:type:: hex
    :examples:
        #000000 => black
        #FFFFFF => white
        #F75D5D
        #13A10E


    A hexadecimal color in the format :code:`#[0-F]{6}`.

.. jcoad:type:: number

    A string of numeric digits, such as :code:`256` or :code:`-3`.

.. jcoad:type:: path
    :examples:
        1u,3l,3d,2r => 1 up, 3 left, 3 down, 2 right
        3u,3d* => 3 up, 3 down, repeat forever
        circle => 1r,1d,1l,1u*
        spin => 0r,0d,0l,0u*
        twirl => spin once, ending on the direction currently facing

    A path string that represents a string of tile movements. In their simplest form, path strings specify the number of tiles to move followed by the direction to move in (represented as a single character). For example, :code:`3d` represents moving 3 tiles down. Multiple moves can be strung together by separating them with commas. Add an asterisk on the end of the string to signify the path should repeat indefinitely. There are also a few special keywords that can be used as shortcuts for some common paths.

.. jcoad:type:: percentage
    :examples:
        0 => 0%
        50 => 50%
        75 => 75%
        100 => 100%
        200 => 200%

    An integer representing a percentage.

.. jcoad:type:: pokémon

    A :ref:`Pokémon Generation String<pokemon_generation>`.

.. jcoad:type:: rgb
    :examples:
        255,0,0 => Red
        232,66,255 => Pink

    A color given in RGB (red-green-blue) format. Three RGB values separated by commas.

.. jcoad:type:: rgba
    :examples:
        [255,0,0,1] => Red, 100% opacity
        [255,0,0,0.5] => Red, 50% opacity

    A color given in RGBA (red-green-blue-alpha) format. The format is :code:`[0-255,0-255,0-255,0-1]`. Only the final number can be a floating-point value.

.. jcoad:type:: short direction
    :options: u, d, l, r

    Exactly like :jcoad:type:`direction`, but only using the first character.

.. jcoad:type:: skin
    :examples:
        youngster => Sinnoh Youngster, ID = 29
        257 => Unova Youngster
        pikachu => Pikachu (Nintendo)
        diagla;shiny => Shiny Dialga (Nintendo)
        -100327 => Spinda (Nintendo)
        -460119.001 => Mareep, Aristos form (Aristos)

    A special type of parameter used to identify overworld skins. For simple cases, skin names or |Pokemon| names work, but integer IDs can be more precise. Use negative numbers for and Dex IDs for |Pokemon|.

.. jcoad:type:: sprite sheet
    :examples:
        2654/sprites.png
        1995/door.png

    A link to an internal sprite sheet (uploaded to |Pokengine|) that you or another user owns. The format is :code:`user_id/sprite_sheet_name.png`.

.. jcoad:type:: string

    A string of characters. Some characters may have special meaning for the function or trigger.

.. jcoad:type:: tileset

    A tileset identification string, which takes the format of :code:`!n`, where :code:`n` is the tileset ID. Basically just a number with an exclamation point in front of it.

.. jcoad:type:: unit interval

    A floating-point number between 0 and 1 (inclusive), such as :code:`0`, :code:`0.125`, :code:`0.783`, or :code:`1`. Usually used for representing percentages.

.. jcoad:type:: yes/no

    Two options representing a boolean choice: :code:`yes` or :code:`no`!
