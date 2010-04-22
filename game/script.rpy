# You can place the script of your game in this file.

init:
    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"

    # Declare characters used by this game.
    $ mchar = Character('Mödchen', color="#c8ffc8")
    $ jchar = Character('Junge', color="#c8ffc8")
    
    image menubar_sp = Animation("images/ui/menu/1.png", 0.10,
                                 "images/ui/menu/2.png", 0.10,
                                 "images/ui/menu/3.png", 0.10,
                                 "images/ui/menu/4.png", 0.10,
                                 "images/ui/menu/5.png", 0.10)


# The game starts here.
label start:

    # Dinge die gemacht werden müssen, bevor das erste Kapitel
    # anfängt, kommen hier rein.
    
    scene bg zimmer
    with fade
    
    "Dies ist nun ein Test, um zu überprüfen, inwiefern mein neuer Versuch eines Menüs auch gut aussieht usw. :3"
    
    menu:
        "Sieht gut aus!":
            "Yay!"
        "Sieht mies aus...":
            "Nein, du! >_<"
    
    # Danach Sprung zum ersten Kapitel, zu finden in
    # kapitel_1.rpy
    
    jump kapitel_1
