# You can place the script of your game in this file.

init:
    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"

    # Declare characters used by this game.
    $ mchar = Character('Mödchen', color="#c8ffc8")
    $ jchar = Character('Junge', color="#c8ffc8")
    
    image regen = Animation("images/regen/1.png", 0.1,
                        "images/regen/2.png", 0.1,
                        "images/regen/3.png", 0.1,
                        "images/regen/4.png", 0.1)
                        
# The game starts here.
label start:

    # Dinge die gemacht werden müssen, bevor das erste Kapitel
    # anfängt, kommen hier rein.
    # Danach Sprung zum ersten Kapitel, zu finden in
    # kapitel_1.rpy
    
    jump kapitel_1
