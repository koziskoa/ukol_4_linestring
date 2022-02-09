import argparse
from functions import  new_geojson, open_load, is_positive_int, transfer_coor
from geometry import LineString

parser = argparse.ArgumentParser()

#definování argumentů
parser.add_argument("-f", help = "Název vstupního souboru", required=True)
parser.add_argument("-l", help = "Maximální délka",required=True)
parser.add_argument("-o", help = "Název výstupního souboru", required=True)

arguments = parser.parse_args()

input_file = arguments.f
max_len = is_positive_int(arguments.l)
output_file = arguments.o

#otvírání souboru
linestring = open_load(input_file)

#pokud jsou souřadnice WGS-84 -> transformace souřadnic do JTSK
for feature in linestring["features"]:
    # x-ová souřadnice WGS-84 bude vždy menší než y-ová
    # v systému S-JTSK je to přesně naopak - tedy x>y
    if feature["geometry"]["coordinates"][0][0]< feature["geometry"]["coordinates"][0][1]:
        new_coor=[]
        if isinstance(feature["geometry"]["coordinates"],list):
            for coords in feature["geometry"]["coordinates"]:
                coords=transfer_coor(coords[0],coords[1])
                new_coor.append(coords)
    else:
        break
    feature["geometry"]["coordinates"]= new_coor

#hledání ve slovníku
for feature in linestring["features"]:
    # pokud iterátor narazí na pole souřadnic, převede ho na soubor linií - Linestring
    # v definování obejktu Linestring se jednotlivé souřadnice zpracovávají na linie (Segment) a body (Point)
    if isinstance(feature["geometry"]["coordinates"],list):
        geo_s = LineString(feature["geometry"]["coordinates"])
        geo_s.divide_long_segments(max_len)
        modified_list = geo_s.segment_to_point_list()
        feature["geometry"]["coordinates"] = modified_list

#zápis do souboru typu geojson
new_geojson(linestring, output_file)