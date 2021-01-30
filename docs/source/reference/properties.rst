.. _properties:

#################
Entity Properties
#################

If you are unsure how to use these object functions, check out the :ref:`entity properties tutorial<properties_tutorial>`.

Any entity property ending with :code:`[&triggers]` may have an optional string of game triggers appended to them to execute alongside the function. See :ref:`triggers` for more information.

.. jcoad:property:: path
    :suffix: (path)

    Defines a path for the entity to follow.

    .. param:: path
        :type: path
        :default: None

        Entity's path.

.. jcoad:property:: speed
    :suffix: (speed)

    Defines the entity's walking speed.

    .. param:: speed
        :type: number
        :default: 100

        Percentage of normal speed. Use :code:`50` for half speed, or use :code:`200` for double speed.

.. jcoad:property:: shadow
    :suffix: ([state])

    Sets whether the entity has a shadow or not.

    .. param:: state
        :type: 0/1
        :default: 0 for sprites, 1 for NPCs

        Should the entity have a shadow?

.. jcoad:property:: solid
    :suffix: ([state])

    Sets where the entity is solid or not.

    .. param:: state
        :type: 0/1
        :default: 0 for sprites, 1 for NPCs

        Should the entity be solid?

.. jcoad:property:: ignore
    :suffix: ()

    Sets whether the entity should ignore the player, by not changing direction, when the player interacts with it.

.. jcoad:property:: float
    :suffix: ([height])

    Sets the entity's floating height.

    .. param:: height
        :type: number
        :default: 0

        Floating height in pixels.

.. jcoad:property:: color
    :suffix: ([color])

    Sets the entity's color.

    .. param:: color
        :type: rgb
        :default: Entity completely ignores lighting effects

        The color to mask the entity with.

.. jcoad:property:: nametag
    :suffix: ()

    Gives the entity a nametag.

.. jcoad:property:: print
    :suffix: (type)

    Creates a fading trail behind the target.

    .. param:: type
        :type: string
        :default: No trail

        Type of trail to draw.

.. jcoad:property:: outline
    :suffix: ([color])

    Draws a colored outline around the target.

    .. param:: color
        :type: rgb
        :default: Removes outline

        Color of outline.

.. jcoad:property:: ally
    :suffix: [=ally1 [ally2 [ally3...]]]

    Sets the target's allies, or following entities.

    .. param:: ally
        :type: skin

        Overworld skin of following ally. For multiple allies, separate with spaces.

.. jcoad:property:: skincolor
    :suffix: [=id]

    Sets the target's skin color.

    .. param:: id
        :type: number
        :default: 0

        Skin color ID to change to.

.. jcoad:property:: persistent
    :suffix: ()

    By default, entities are destroyed when the player leaves the map or reloads the map. Persistent entities will persist.

.. jcoad:property:: spot
    :suffix: (tiles[,change_path[,spot_through_walls[,move_to_spotted]]])

    Allows the entity to spot the player and initiate an interaction.

    .. param:: tiles
        :type: number

        Radius, in all directions, the player must be in to be spotted.

    .. param:: change_path
        :type: 0/1
        :default: 1

        Should the NPC stop their path after spotting the player? If not, the entity will keep moving after spotting the player.

    .. param:: spot_through_walls
        :type: 0/1
        :default: 0

        Can the entity spot the player through walls?

    .. param:: move_to_spotted
        :type: 0/1
        :default: 1

        Should the entity move to the player after spotting?

.. jcoad:property:: opacity
    :suffix: (opacity)

    Sets the entity's opacity.

    .. param:: opacity
        :type: percentage

        The opacity as a percentage. Use :code:`100` for 100%, or use :code:`50` for 50%.

.. jcoad:property:: xy
    :suffix: (x,y)

    Offsets the display position of the object.

    .. param:: x
        :type: number

        Horizontal offset in pixels.

    .. param:: y
        :type: number

        Vertical offset in pixels.

.. jcoad:property:: depth
    :suffix: (depth)

    Sets the relative depth of the entity.

    .. param:: depth
        :type: number|depth

        Depth of the sprite. If a number is given, it works like :code:`depth+n`.

.. jcoad:property:: spin
    :suffix: ()

    Causes the object to spin.