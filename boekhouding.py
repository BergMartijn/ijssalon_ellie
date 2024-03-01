from helper import som
from presentatie import presenteer
import csv

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

totaal_inkomsten = presenteer(inkomsten)

print (totaal_inkomsten)

with open('boekhouding.csv', 'w',newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow([key,value])