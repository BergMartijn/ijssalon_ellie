from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    a = prijs * korting
    eindprijs = prijs - a
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {eindprijs} euro"
    return uitvoer

print (aanbieding_1("aardbei", 4, 0.1))



def inkomsten_totaal(ma,di,wo,do,vr,za,zo):
    return  ma + di + wo + do + vr + za + zo
inkomsten = inkomsten_totaal(220, 430, 125, 160, 205, 90, 345)
btw = 0.09 * inkomsten
uitvoer = f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden."

print (uitvoer)



def laag_en_hoog(ma,di,wo,do,vr,za,zo):
    return ma,di,wo,do,vr,za,zo
mijn_lijst = max(220, 430, 125, 160, 205, 90, 345), min(220, 430, 125, 160, 205, 90, 345)

print (mijn_lijst)



def gemiddelde(ma,di,wo,do,vr,za,zo):
    return ma + di + wo + do + vr + za + zo
mijn_lijst = gemiddelde(220, 430, 125, 160, 205, 90, 345) / 7
uitvoer = f"De gemiddelde inkomsten deze week zijn {mijn_lijst} euro."

print (uitvoer)



def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer