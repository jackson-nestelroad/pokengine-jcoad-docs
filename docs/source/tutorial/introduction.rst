.. _introduction:

############
Introduction
############

What is |Pokengine|?
====================
|Pokengine|_ is a community focused on the creation of custom content, such as Regions and Dexes. |Pokengine| also provides a browser-based MMO, combining all the created content into one big game (although Regions can be isolated, and turned into a standalone game, if their owners wish to do so).

|Pokengine| is an engine by nature, not an actual game. The game part is created by its users, meaning instead of |Pokengine| being just one game, it's several rolled into one.

The engine offers a collection of online browser-based tools, made for the sole purpose of editing and building the game.

What is Mapbuilder?
===================
**Mapbuilder** is |Pokengine|'s software to program and implement Tilefuser maps into the game engine. Only users granted access to the Mapbuilder may use it to put their maps into the game.

Only users developing a region or who are trusted with the Mapbuilder are granted access to this tool. Not all users may use this tool because it allows players a high degree of control over the game engine.

Mapbuilder works by using your Tilefuser map as a foundation. The Mapbuilder can add objects, NPCs, sprites, animations, or anything your map needs to make it come alive in the game. All map objects are implemented using |Pokengine|'s custom programming language, jCoad, which is the focus of this guide.

Before jumping into the programming, here are a few Mapbuilder tips to get you started with the tool.

Rules of Mapbuilder
-------------------

#. Do not talk about Mapbuilder.
#. Do not talk about Mapbuilder.
#. Only use one Mapbuilder tab at one time.

    - Multiple tabs may corrupt where your objects are saved.

#. When in doubt, compile your route.

    - To compile, press the "save" button in the "Settings" tab.

#. When you rage, refresh the page.

    - Mapbuilder autosaves, but sometimes an object might not save properly. If you find something on your map is not working, refresh the page. You could possible find a previously-invisible object wreaking havoc on your map in the wrong location.

#. If you want to share, put it in there.

    - Mapbuilder maps are exclusive to you unless you specify its region in the "Settings" tab. Then, all regions helpers will be able to view and edit your map as well.

#. Be careful!

    - You, and only you, are responsible for the programming of your region. Be cautious when working with event variables and spawning items and |Pokemon|.
    - In other words, don't spawn level 100 legendaries and Master Balls for everyone!

What is jCoad?
==============
**jCoad** is |Pokengine|'s custom programming language. This language is compiled to JavaScript to run client and server events within the game engine.