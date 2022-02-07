import argparse
from functions import  new_geojson, open_load, is_positive_number, transfer_coor
from geometry import LineString

parser = argparse.ArgumentParser()

#definování argumentů
parser.add_argument("-f", help = "Název vstupního souboru", required=True)
parser.add_argument("-l", help = "Maximální délka",required=True)
parser.add_argument("-o", help = "Název výstupního souboru", required=True)

arguments = parser.parse_args()

input_file = arguments.f
max_len = is_positive_number(arguments.l)
output_file = arguments.o

#otvírání souboru
cyklotrasy = open_load(input_file)

#pokud jsou souřadnice WGS-84 -> transformace souřadnic do JTSK
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

#hledání ve slovníku
for i in cyklotrasy["features"]:
    # pokud iterátor narazí na pole souřadnic, převede ho na soubor linií - Linestring
    # v definování obejktu Linestring se jednotlivé souřadnice zpracovávají na linie (Segment) a body (Point)
    if isinstance(i["geometry"]["coordinates"],list):
        geo_s = LineString(i["geometry"]["coordinates"])
        geo_s.divide_long_segments(max_len)
        modified_list = geo_s.segment_to_point_list()
        i["geometry"]["coordinates"] = modified_list

#zápis do souboru typu geojson
new_geojson(cyklotrasy, output_file)