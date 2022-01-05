import argparse
from functions import  open_load, is_positive_number, transfer_coor

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--inputfile", help = "Název vstupního souboru", type = open_load)
parser.add_argument("-l", "--maxlength", help = "Maximální délka", type = is_positive_number)
parser.add_argument("-o", "--outputfile", help = "Název výstupního souboru")

arguments = parser.parse_args()
'''print(f"Vstupní soubor je {arguments.inputfile}")
print(f"Maximální délka je {arguments.maxlength}")
print(f"Výstupní soubor je {arguments.outputfile}")'''
cyklotrasy = arguments.inputfile

#pokud jsou souřadnice WGS-84 -> transformace souřadnic
for i in cyklotrasy["features"]:
    # x-ová souřadnice WGS-84 bude vždy menší než y-ová
    # v systému S-JTSK je to přesně naopak - tedy x>y
    if i["geometry"]["coordinates"][0][0]< i["geometry"]["coordinates"][0][1]:
        coor=[]
        if isinstance(i["geometry"]["coordinates"],list):
            for j in i["geometry"]["coordinates"]:
                j=transfer_coor(j[0],j[1])
                coor.append(j)
    else:
        break
    i["geometry"]["coordinates"]= coor
print(cyklotrasy)



