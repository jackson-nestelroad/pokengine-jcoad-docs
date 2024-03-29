.. _battle_properties:

####################
Battle Properties
####################

You can set various properties of a battle when you call it to start, for both wild |Pokemon| battles and also trainer battles. The properties are listed below.

Types of Battle Properties
============================

.. jcoad:battleoption:: norun

    Cannot run from battle. This is default true of trainer battles so you only need to specify for wild battles.

.. jcoad:battleoption:: nocatch

    Cannot catch the opposing |Pokemon|. This is default true of trainer battles so you only need to specify for wild battles.

.. jcoad:battleoption:: nomoney

    No money earned from battle. This is default true of wild battles so you only need to specify for trainer battles.

.. jcoad:battleoption:: noexp

    No |Pokemon| experience gained during the battle. 

.. jcoad:battleoption:: noseen

    Opposing |Pokemon| are not counted as seen in the Pokedex.

.. jcoad:battleoption:: noitems

    Cannot use items from the bag widget during battle, such as Poke Balls or Potions.

.. jcoad:battleoption:: double

    Changes battle format to a double battle.

.. jcoad:battleoption:: triple

    Changes battle format to a triple battle.

.. jcoad:battleoption:: hiddenlevel

    Levels of the opposing |Pokemon| are hidden. Appear as ???.

.. jcoad:battleoption:: fixedlevel
    :suffix: level

    Forces all |Pokemon| in battle to the specified level. Uses their true stats (IVs, EVs) but calculates the actual stat value (attack, etc) based on the new set level. This works identically to fixed level battles such as the Battle Tower in the mainline games.

.. jcoad:battleoption:: scene
    :suffix: id

    Sets the battle scene (background image) to the one specified. Only necessary for wild battles, as trainer battles have a scene property set in advance.

.. jcoad:battleoption:: theme
    :suffix: url

    Sets the music playing during battle. Currently hosting on Dropbox is supported only. The format is :code:`db:` for host, then a modified URL which cuts out the :code:`https://www.dropbox.com/` part.
    :code:`theme db:s/fo7smcp2luvrikc/BattleTowerSWSHRemix.mp3` |emdash| Sets the theme according to this Dropbox shared URL.



Examples
============================

**Example 1:** Wild |Pokemon| Boss
This first example is a boss battle against a wild |Pokemon|. You cannot run or catch it, and the level is hidden. The |Pokemon|'s name is also set to hide its species.

.. code-block::

    msg(Groouuugoooough!!)&!cry=517,3,2&battle=517,3,2;level 80;name ???;scene 51;hiddenlevel;nomoney;nocatch;norun


**Example 2:** Battle Tower
This example is from the HUB Battle Tower. The dialogue in the :jcoad:func:`msg` block and the trainer battle ID are both controlled by a list. The variable :code:`var[noblackout]=1` is set so that the player will not teleport away if they lose the battle.

Similar to the mainline games' Battle Tower, this battle gives no exp or money, but instead I manually give the player BP if they win (not shown). Items are not allowed, and all participating |Pokemon| are set to level 50 for the duration of the battle.

.. code-block::

    msg(%list[trainers][n].speech%)&var[noblackout]=1&mapvar[battle]=3&battle=%list[trainers][n].battleid%;noexp;nomoney;noseen;noitems;fixedlevel 50;theme db:s/fo7smcp2luvrikc/BattleTowerSWSHRemix.mp3
