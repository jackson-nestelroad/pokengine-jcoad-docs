.. _understanding_definitions:

#########################
Understanding Definitions
#########################

This guide will focus on several definitions for using jCoad functions, properties, and triggers.

Anything in parenthesis is a **parameter**. Parameters are separated by commas with **no spaces between them**.

Any parameter than is enclosed in brackets (*[,example]*) is an **optional parameter**. These are not required and may not be needed when you are using the object code.

Any set of brackets may be removed and your jCoad will still work properly, but you must be careful to remove the correct set of brackets and optional parameters.

Take the following jCoad as an example on how to identify which optional parameters can be taken out at once.

.. raw:: html

    <div class="highlight-none notranslate"><div class="highlight">
    <pre><span></span>animation(image<span class="purple">[,depth<span class="blue">[,x,y,width,height<span class="green">[,frames<span class="orange">[,speed<span class="red">[,loop]</span>]</span>]</span>]</span>]</span>)</pre>
    </div></div>

This piece of jCoad can be used in any of the following ways depending on what you may or may not need to include.

.. raw:: html

    <div class="highlight-none notranslate"><div class="highlight">
        <pre><span></span><span>animation(image)</span>
    <span>animation(image<span class="purple">[,depth]</span>)</span>
    <span>animation(image<span class="purple">[,depth<span class="blue">[,x,y,width,height]</span>]</span>)</span>
    <span>animation(image<span class="purple">[,depth<span class="blue">[,x,y,width,height<span class="green">[,frames]</span>]</span>]</span>)</span>
    <span>animation(image<span class="purple">[,depth<span class="blue">[,x,y,width,height<span class="green">[,frames<span class="orange">[,speed]</span>]</span>]</span>]</span>)</span>
    <span>animation(image<span class="purple">[,depth<span class="blue">[,x,y,width,height<span class="green">[,frames<span class="orange">[,speed<span class="red">[,loop]</span>]</span>]</span>]</span>]</span>)</span></pre>
    </div></div>

Now, we only need to **remove the brackets** to show what we would type into Mapbuilder.

.. raw:: html

    <div class="highlight-none notranslate"><div class="highlight">
        <pre><span></span><span>animation(image)</span>
    <span>animation(image<span class="purple">,depth</span>)</span>
    <span>animation(image<span class="purple">,depth<span class="blue">,x,y,width,height</span></span>)</span>
    <span>animation(image<span class="purple">,depth<span class="blue">,x,y,width,height<span class="green">,frames</span></span></span>)</span>
    <span>animation(image<span class="purple">,depth<span class="blue">,x,y,width,height<span class="green">,frames<span class="orange">,speed</span></span></span></span>)</span>
    <span>animation(image<span class="purple">,depth<span class="blue">,x,y,width,height<span class="green">,frames<span class="orange">,speed<span class="red">,loop</span></span></span></span></span>)</span></pre>
    </div></div>

Obviously, the parameter names are only used for documentation. These names will be replaced with **arguments** that you pass in. Arguments may be a string of characters, a number, a boolean value, or some other format. All data types are documented alongside the parameter lists later in this guide.