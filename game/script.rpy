# You can place the script of your game in this file.

init:

    $ m = Character('Liz',color="#c8ffc8")
    $ j = Character('Junge',color="#c8ffc8")
    $ narrator = Character(None, kind=nvl)
    $ q = Character(None, kind=nvl, what_prefix='"',what_suffix='"')
    
    image regen = Animation("images/regen/1.png", 0.1,
                        "images/regen/2.png", 0.1,
                        "images/regen/3.png", 0.1,
                        "images/regen/4.png", 0.1)

    python:
        #Diese Funktion wechselt den Erzählmodus.
        #Gültige Modi sind:
        # nvl    - NVL-Modus. Großes Textfenster füllt das ganze Bild.
        #          Wörtliche Rede wird vom Charakter "q" gesprochen.
        # normal - Normaler Modus. Kleines Textfenster am unteren Bildrand.
        #          Wörtliche Rede wird durch die Charaktere selbst gesprochen.
        def setMode(mode = "nvl"):
            global narrator
            if mode == "nvl":
                narrator = Character(None, kind=nvl) #Ändere den Erzähler
            elif mode == "normal":
                nvl_clear() #Lösche den NVL-Buffer
                narrator = Character(None) #Ändere den Erzähler
        
                        
# The game starts here.
label start:

    # Dinge die gemacht werden müssen, bevor das erste Kapitel
    # anfängt, kommen hier rein.
    # Danach Sprung zum ersten Kapitel, zu finden in
    # kapitel_1.rpy
    
    jump kapitel_1
