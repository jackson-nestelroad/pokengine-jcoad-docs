.. _types:

##########
Data Types
##########

jCoad does not really have data types, but putting arguments into the proper format for object functions, properties, and triggers is absolutely necessary for your code to work properly. Use this guide to understand how to enter arguments into your jCoad.

.. jcoad:type:: 0/1

    A binary digit, representing a boolean value. 1 represents "yes," "on," or "true," while 0 represents "no," "off," or "false."

.. jcoad:type:: direction
    :options: up, down, left, right

    A direction the player can face.


.. jcoad:type:: number

    A string of numeric digits, such as :code:`256` or :code:`-3`.

.. jcoad:type:: pokémon

    A :ref:`Pokémon Generation String<pokemon_generation>`.

.. jcoad:type:: rgba
    :examples:
        [255,0,0,1] => Red, 100% opacity
        [255,0,0,0.5] => Red, 50% opacity

    A color given in RGBA (red-green-blue-alpha) format. The format is :code:`[0-255,0-255,0-255,0-1]`. Only the final number can be a floating-point value.

.. jcoad:type:: sprite sheet
    :examples:
        2654/sprites.png
        1995/door.png

    A link to an internal sprite sheet (uploaded to |Pokengine|) that you or another user owns. The format is :code:`user_id/sprite_sheet_name.png`.

.. jcoad:type:: string

    A string of characters. Some characters may have special meaning for the function or trigger.


.. jcoad:type:: unit interval

    A floating-point number between 0 and 1 (inclusive), such as :code:`0`, :code:`0.125`, :code:`0.783`, or :code:`1`. Usually used for representing percentages.
