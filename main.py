health = 10
print(health)


def essen():
    print("hi")

    if health == 5:
        health += 95
        print(health)
        print("Du regeneriertst auf", health, "Gesundheitspunkte...")

    elif health == 10:
        health += 90
        print(health)
        print("Du regeneriertst auf", health, "Gesundheitspunkte...")

def klopfen():
    print("Du klopfst an die Tür du musst einen Moment warten, doch dann öffnet dein guter Freund Peter, er bietet dir an reinzukommen...")
    essen_ja_nein = input("Er bietet dir etwas zu essen an, nimmst du es an??? (ja/nein) ")
    if essen_ja_nein == "ja":
        print("essen wurde angenommen")
        essen()

    elif essen_ja_nein == "nein":   
        essen_ja_nein_sicher = input("Bist du sicher??? Du wirst keine Gesundheitspunkte regenerieren... bist du sicher??? (ja/nein)")
        if essen_ja_nein_sicher == "ja":
            print("")
        
        elif essen_ja_nein_sicher == "nein":
            essen()


    

            

def gucken():
        print("Du gehst um das Haus herum und guckst durch die Fenster...")
        ans = input("Drinnen siehst du deinen guten freund Peter sitzen gehst du klopfen oder gehst du zum Fluss??? (klopfen/Fluss) ").lower()
        if ans == "klopfen":
            klopfen()
        elif ans == "Fluss":
            Fluss()   




def Haus_Fluss():
    Haus_oder_Fluss = input("Du siehst ein Haus und einen Fluss wo gehst du hin??? (Haus/Fluss)").lower()
    if Haus_oder_Fluss == "haus":       
        klopfen_gucken = input("Du kommst am Haus an, gehst du klopfen oder schaust du es dir an??? (klopfen/gucken) ").lower()
        if klopfen_gucken == "klopfen":
            klopfen()
        elif klopfen_gucken == "gucken":
            gucken()
        else:
            Fluss()
    elif Haus_oder_Fluss == "fluss":
        Fluss()

 


                            


def Fluss(): 
   
    durch_zurück = input("Du siehst vor dir einen reißenden gut zehn Meter breiten Fluss, gehst du durch oder zurück??? (durch/zurück)").lower()
    if durch_zurück == "durch":
        print("Du wirst durch die Strömung runtergezogen und ertrinkst...")
        ans = input("Willst du nochmal spielen???" )

    elif durch_zurück == "zurück":
        Haus_Fluss()


print("Willkommen zu meinem ersten Spiel")
name = input("Wie ist dein Name? ")
alter = int(input("Wie alt bist du? "))
print("Du heißt also", name, "und bist", alter, "Jahre alt")

if alter >= 18:
    print("Du bist alt genug um zu spielen!")

    wants_to_play = input("Willst du spielen? ").lower()
    if wants_to_play == "ja":
        print("Lass uns spielen")
        print("Du startest mit", health, "Gesundheitspunkten")
        left_or_right = input("Erste Entscheidung... Links oder Rechts (Links/Rechts) ").lower()
        if left_or_right == "links":
            ans = input("Du folgst dem Weg und triffst auf einen See... schwimmst du durch oder gehst du drumherum??? (schwimmen/gehen) ")
            if ans == "schwimmen":
                print("Du bist geschwommen und konntest die andere seite erreichen, jedoch hast du 5 Lebenspunkte verloren...")
                health -= 5
                Haus_Fluss()

            elif ans == "gehen":
                print("Du bist um den See herumgelaufen und hast die andere Seite erreicht... ")
                
                Haus_Fluss()
                          
            else:
                print("Du hast verloren")
                
            
        else:
            print("Du bist in ein Loch gefallen und gestorben... Versuche es nochmal! ")
    else:
        print("Dann tschüss...")
else:
    print("du bist nicht alt genug um zu spielen... ")
