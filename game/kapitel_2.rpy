label kapitel_2:

    #Esszimmer
    #scene bg esszimmer
    #with fade
    
    #Sound überleg ich mir noch
    #play ambient "sounds/regen_drinnen.ogg" fadein 1.0
    
    $ renpy.pause(1)
    
    # Kapitel 2 - Los!
    
    $ setMode("nvl")
    
    nvl clear
    
    "Als Liz die Augen öffnete, fand sie sich zu ihrer Überraschung im Esszimmer wieder."
    "Ihre Verwunderung über den ungewohnten Schlafplatz auf dem kleinen Sofa verschwand jedoch schnell, als ihr die Geschehnisse des gestrigen Abends wieder ins Gedächtnis schossen."
    "Nachdem der merkwürdige Junge in ihrem Bett eingeschlafen war, hatte sie sich eine der Ersatzbettdecken geholt, und es sich auf dem Sofa bequem gemacht."
    "Sie hatte kurz überlegt, die Nacht in einem der Gästeschlafzimmer zu verbringen, verwarf den Gedanken jedoch wieder, da sie sich nicht daran erinnern konnte, wann dort zuletzt saubergemacht worden war."
    
    nvl clear
    
    "Sich den Schlaf aus den Augen reibend stand sie auf, faltete die Decke zusammen und legte sie über das Sofa. {w}Wegräumen würde sie sie später."
    "Sie schaute aus dem Fenster und stellte fest, dass es aufgehört hatte zu regnen."
    "Ob der Junge inzwischen wach war?"
    "Liz beschloss, nachschauen zu gehen."
    
    nvl clear
    
    scene bg zimmer
    with fade
    
    "Als Liz das Zimmer betrat, traute sie ihren Augen nicht."
    "Die Bettdecke lag auf dem Fußboden, einige Dinge waren aus ihrem Regal gefallen und vom Jungen fehlte jede Spur."
    q "Was...? {w}Aber..."
    "Sie wusste nicht, was vorgefallen war, aber alles sah danach aus, als wäre er abgehauen."
    q "Das kann doch nicht wahr sein!"
    "Vielleicht versteckte er sich irgendwo?"
    "Sie beschloss, das Haus zu durchsuchen. {w}Mit diesem Zimmer würde sie anfangen."
    
    nvl clear
    
    "Sie schaute in allen Ecken, hinter alles, wohinter man sich hätte verstecken können und unters Bett."
    "Tatsächlich gab es nicht viele Orte, die als Versteck geeignet waren in diesem Zimmer."
    q "Gut, dann bin ich hier wohl fertig. {w}Jetzt noch 12 andere Zimmer."
    
    nvl clear
    
    scene black
    with fade
    
    $ renpy.pause(1)
    
    scene bg zimmer
    with fade
    
    "Eine halbe Stunde später hatte sie beinahe das ganze Haus durchsucht, doch von dem mysteriösen Jungen war nichts zu sehen."
    q "Ah! {w}Ich weiß! {w}Ich werde meinen Onkel fragen."
    
    nvl clear
    
    scene black
    with fade
    
    jump kapitel_2_onkel
    
label kapitel_2_onkel:
    
    $ setMode("normal")
    
    scene bg arbeitszimmer
    with fade
    
    "Als Liz das Arbeitszimmer ihres Onkels betrat, drang ihr ein stechender Geruch in die Nase und sie musste husten."
    m "Was stinkt denn hier so?"
    o "Ah, Liz! {w}Komm doch runter!"
    "Liz befand sich auf der zweiten Etage der ehemaligen Bibliothek, die nun zu einem Arbeitszimmer umfunktioniert wurde, und ihr Onkel sah zu ihr herauf und winkte."
    m "Was ist das für ein Geruch? {w}Wieder irgendein Experiment?"
    "Sie schaute angewidert nach der Quelle des Gestanks, während sie die kleine Wendeltreppe hinunterstieg, die zur unteren Ebene führte."
    o "Das weißt du doch ganz genau, junges Fräulein!"
    o "Tu mal nicht so unschuldig!"
    "Liz ignorierte die merkwürdigen Bemerkungen ihres Onkels und konzentrierte ihren Blick auf den zerbrochenen Glasbecher der unter dem Tisch lag, und aus dem sich eine schwarze Substanz über den Boden ergoss, die die Quelle des Gestanks zu sein schien."
    m "Was auch immer."
    "Sie war nicht hier um sich jetzt mit ihrem verwirrten Onkel zu beschäftigen."
    "Sie musste den Jungen finden."
    o "Wenn du schon mal wieder hier bist, kannst du die Sauerei auch aufwischen. {w}Da in der Ecke sind Putzeimer und Lappen!"
    "Liz schnappte sich den Putzeimer, und fing an, die Glasscherben aus der schwarzen, klebrigen Masse zu ziehen."
    m "Du, Onkel?"
    o "Was ist denn?"
    m "Hast du hier vielleicht einen Jungen gesehen?"
    "Sie nahm den Lappen, tauchte ihn in den Eimer und fing vorsichtig an, die stinkende Flüssigkeit aufzuwischen."
    o "Einen Jungen... {w}einen Jungen...?"
    m "Vergiss es einfach wieder."
    "Ihr Onkel hatte ihn offensichtlich nicht gesehen."
    o "Jetzt wo du es sagst... {w}hier war ein Junge."
    m "Was? {w}Ehrlich?"
    "Hatte er ihn doch gesehen?"
    o "Ja, ziemlich sicher."
    o "Er schaute kurz zur Tür rein, entschuldigte sich schnell und ging dann wieder."
    m "..."
    m "Und du hast dir nichts dabei gedacht?"
    o "Nein, wieso?"
    "Das war typisch für ihren Onkel."
    "Ein fremder Junge lief in seinem Haus herum, und er kümmerte sich nicht darum, oder hielt es für normal."
    m "Und wo ist er dann hin?"
    "Liz hob den Putzlappen an, in den der schwarze Schleim inzwischen ein großes Loch gefressen hatte, und warf ihn in den Eimer."
    o "Ich glaube er ist richtung Ausgang gegangen."
    m "Also in Richtung Stadt?"
    o "Ja, ich denke schon."
    "Liz' Augen fingen an zu funkeln."
    "Sie hatte eine Spur."
    "Schnell stellte sie den Putzeimer in die Ecke und rannte die Treppe hinauf."
    m "Ich geh mal runter in die Stadt! {w}Bis später!"
    o "Aber du sollst doch nicht raus, wenn es regnet."
    "Liz blieb stehen und drehte sich um."
    m "Schau mal öfter aus dem Fenster, Onkelchen!"
    "Mit diesen Worten ließ sie ihren Onkel zurück und machte sich auf in die Stadt."
    
    scene black
    with fade
    
    jump kapitel_2_stadt
    
label kapitel_2_stadt:

    $ setMode("nvl")
    
    # Hintergrund Stadt, evtl. eine Art Marktplatz mit Häusern drumherum und
    # einem Brunnen in der Mitte, der über eine große Pumpe läuft.
    # Vielleicht auch dampfbetriebene Autos bzw. Kutschen oder ähnliches.
    
    # ^ Scheiß auf das. Ich mach nur den Brunnen, das geht schneller. 9_9
    
    "Nach ungefähr zwanzig Minuten war Liz auf dem Marktplatz angekommen. {w}Hier, hatte sie sich entschieden, würde sie ihre Suche beginnen."
    "Doch wie stellte man sowas an?"
    "Bisher war sie nie wirklich auf der Suche nach etwas oder jemandem bestimmten gewesen, sondern ist einfach nur ziellos durch die Stadt gelaufen."
    "Irgendwie schien es ihr, als würde das nicht funktionieren, wenn man einen Jungen sucht."
    "Aber was dann?"
    "Die Stadt systematisch zu durchkämmen kam überhaupt nicht in Frage. {w}Das würde viel zu lange dauern und würde auch nicht garantieren, dass sie den Jungen findet."
    "Sie brauchte also einen Anhaltspunkt. {w}Einen Ort, an dem sie anfangen könnte zu suchen."
    
    nvl clear
    
    menu:
        "Ich frage jemanden.":
            jump kapitel_2_stadt_mann
        "Ich sehe mich um.":
            jump kapitel_2_stadt_suchen

label kapitel_2_stadt_mann:    
    q "Ich habs, ich frage einfach jemanden, ob der ihn gesehen hat!"
    "Ein fremder Junge wird ja wohl recht auffällig sein, für die Leute, die jeden Tag hier unterwegs waren, also wird ihn schon jemand gesehen haben."
    "Liz sah sich nach Leuten um, die sie fragen könnte, als ihr ein älterer, gut gekleideter Herr auffiel."
    q "Den werde ich fragen!"
    
    nvl clear
    
    $ setMode("normal")
    
    #bild von liz und typ
    
    m "Entschuldigen Sie..."
    "Mann" "Hm...? {w}Oh!"
    "Mann" "Was kann ich für dich tun, junge Dame?"
    "Sie erinnerte sich daran, ihn schon einmal gesehen zu haben, war sich aber nicht sicher wo und unter welchen Umständen."
    "Sie wurde ein wenig nervös als sie daran dachte, dass ein Großteil der Stadtbewohner sie wegen ihrer Streifzüge auf fremden Grundstücken nicht besonders mochten."
    "Anscheinend hatte dieser Herr jedoch noch nicht ihre Bekanntschaft gemacht, und war sehr freundlich."
    m "Ich hätte da eine Frage..."
    "Mann" "Und zwar?"
    m "Haben Sie vielleicht einen Jungen hier vorbeikommen sehen, der ungefähr in meinem Alter war?"
    "Mann" "Einen Jungen...?"
    "Der Mann legte die Stirn in Falten und dachte angestrengt nach."
    "Mann" "Also ich war den ganzen Morgen hier, weil ich auf einen Bekannten aus <Name der Nachbarstadt> warte, aber einen Jungen habe ich nicht gesehen."
    "Mann" "Ich glaube nicht, dass hier einer vorbeigekommen ist."
    m "Oh... verstehe."
    "Enttäuscht wandte sie sich ab."
    m "Trotzdem vielen Dank."
    #weg mit dem typen
    jump kapitel_2_stadt_zum_hafen

label kapitel_2_stadt_suchen:
    q "Ich sollte mich mal lieber gut umsehen."
    "Liz schaute sich auf dem Platz um, doch vom Jungen fehlte natürlich jede Spur."
    "Es wäre auch zu schön gewesen, würde er grade jetzt einfach vor ihr über den Platz laufen."
    "Sie seufzte und setzte sich auf den Rand des Brunnens."
    "Was jetzt?"
    "Sollte sie vielleicht einfach aufgeben?"
    "Es war ja nicht so, dass sie den Jungen unbedingt finden musste."
    "Warum war sie eigentlich nochmal hinter ihm her?"
    
    nvl clear
    
    "Alles was sie dazu gebracht hatte, ihm zu folgen, war dieses Gefühl in ihrem Hinterkopf, dass irgendetwas nicht stimmt."
    "Dieses Gefühl, dass sie unbedingt wissen musste, was los war."
    "Eine unbeschreibliche Neugierde."
    "Etwas war faul hier, und sie würde dahinterkommen, egal was."
    "Denn wenn sie es nicht tat, wer dann?"
    "Sie konnte nicht weiter hier herumsitzen!"
    "Fest entschlossen ballte sie ihre Faust mit aller kraft."
    q "Ich finde ihn."
    q "Ganz sicher."
    
    nvl clear
    
    "Und dann sah sie ihn."
    "Es war nur ein kurzer Moment, aber sie war sich sicher, dass er es war."
    "Sie erkannte es nicht an seiner Kleidung oder seinem Gang."
    "Schon gar nicht an seinem Gesicht, denn sie sah ihn nur von hinten."
    "Es war vielmehr eine Art Intuition. {w}Eine Stimme in ihrem Kopf, die ihr befahl loszurennen."
    "Vielleicht ihre letzte Chance."
    "Sie sprang auf und rannte in Richtung der Straße, in die der Junge verschwunden war."
    
    #wusch! Bild von der Straße
    
    nvl clear
    
    "Weg."
    "Er war weg."
    "Dabei war sie sich so sicher."
    "Sie hatte gehofft, dass sie ihn wenigstens hinter der nächsten Ecke verschwinden sehen würde, aber er war wie vom Erdboden verschluckt."
    "War ihre letzte Chance damit verschwunden?"
    "Oder gab es sie überhaupt nicht?"
    "Sie hatte sich sicher nur eingebildet, ihn gesehen zu haben."
    "Zumindest zog sie das in Betracht, und es erschien ihr immer wahrscheinlicher, je mehr sie darüber nachdachte."
    "Vielleicht sollte sie einfach nach Hause zurückgehen und den Jungen vergessen."
    "Sie kannte ihn ja nicht einmal richtig."
    
    #hier gehts später weiter, und zwar so dass sie zurückgeht zum brunnen, überlegt
    #dann feststelt, dass die straße ja doch nur eine richtung hatte, sofort hinrennt
    #und über ihre eigene dummheit gesichtspalmiert
    #dort wird sie dann von ihrem zukunfts-ich zum hafen geschickt und so...
    # v das da unten muss ich dann noch irgendwie fixen...
    
    jump kapitel_2_stadt_zum_hafen
    
label kapitel_2_stadt_zum_hafen:

    $ setMode("nvl")

    "Sie war wieder da, wo sie angefangen hatte und keinen Schritt weiter."
    "Oder war sie in Wirklichkeit sogar noch weiter von ihrem Ziel entfernt als vorher?"
    "Sie wusste ja gar nicht, ob der Junge wirklich in die Stadt gelaufen war."
    "Ihr Onkel war zwar sehr intelligent, aber auch oft verwirrt und abgelenkt."
    "Konnte sie sich auf seine Aussage verlassen oder war sie auf dem völlig falschen Weg?"
    "Ob sie den Jungen überhaupt finden würde...?"
    
    #with fade