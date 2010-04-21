# You can place the script of your game in this file.

init:
    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"

    # Declare characters used by this game.
    $ mchar = Character('Mödchen', kind=nvl, color="#c8ffc8")
    $ jchar = Character('Junge', kind=nvl, color="#c8ffc8")
    $ narrator = Character(None, kind=nvl)
    $ q = Character(None, kind=nvl, what_prefix='"',what_suffix='"')


# The game starts here.
label start:

    # Dinge die gemacht werden müssen, bevor das erste Kapitel
    # anfängt, kommen hier rein.
    
    # Danach Sprung zum ersten Kapitel, zu finden in
    # kapitel_1.rpy
    
    jump kapitel_1
