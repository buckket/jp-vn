# You can place the script of your game in this file.

init:

    # Charaktere

    $ m = Character('Liz',color="#c8ffc8") # Mödchen für Dialogszenen
    $ j = Character('Junge',color="#c8ffc8") # Junge für Dialogszenen
    $ narrator = Character(None, kind=nvl) # Erzähler für Dialog und NVL
    $ q = Character(None, kind=nvl, what_prefix='"',what_suffix='"') # Wörtliche Rede für NVL
    
    # Bilder, die nicht automatisch geladen werden
    
    image black = Solid((0,0,0,255)) # Schwarzer Hintergrund
    
    image regen = Animation("images/regen/1.png", 0.1, # Regenanimation
                        "images/regen/2.png", 0.1,
                        "images/regen/3.png", 0.1,
                        "images/regen/4.png", 0.1)


    image bg zimmer_nacht: # Zimmer bei Nacht, Animation
        "images/bg/zimmer_nacht_2.png" with Dissolve(5.0)
        pause 5.0
        "images/bg/zimmer_nacht.png" with Dissolve(5.0)
        pause 5.0
        repeat

    # Übergänge

    $ slow_fade = Fade(2.0,0.0,1.0)
    $ trans_diagonal = ImageDissolve("images/effects/trans_diagonal.png", 0.2, 8, reverse=True) # Diagonal

    # Sonstiges

    $ renpy.music.register_channel("ambient", "music", True)

    # Spezielle Funktionen

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
