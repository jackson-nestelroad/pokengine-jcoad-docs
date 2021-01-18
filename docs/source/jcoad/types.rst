##########
Data Types
##########

jCoad does not really have data types, but putting arguments into the proper format for object functions, properties, and triggers is absolutely necessary for your code to work properly. Use this guide to understand how to enter arguments into your jCoad.

.. jcoad:type:: string

    A string of characters. Some characters may have special meaning for the function or trigger.

.. jcoad:type:: number

    A string of numeric digits, such as :code:`256` or :code:`-3`.

.. jcoad:type:: direction
    :options: up, down, left, right

    A direction the player can face.

.. jcoad:type:: 0/1

    A binary digit, representing a boolean value. 1 represents "on" or "true," while 0 represents "off" or "false."

.. jcoad:type:: sprite sheet
    :examples: 2654/sprites.png
        1995/door.png

    A link to an internal sprite sheet (uploaded to |Pokengine|) that you or another user owns. The format is :code:`user_id/sprite_sheet_name.png`.
