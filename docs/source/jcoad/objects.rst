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
