import json
from json.decoder import JSONDecodeError
from pyproj import Transformer
from math import sqrt

wgs2jtsk = Transformer.from_crs(4326,5514, always_xy=True)

def open_load (name):
    """# Otevírá soubor typu json 
    - do parametru se zadá název souboru včetně uvozovek např. "soubor.json"
    - vrací obsah souboru"""
    try:
        with open(name, encoding="utf-8") as geojsonfile:
            reader = json.load(geojsonfile)
            reader_n = v_to_number(reader)
        return reader_n
    
    except FileNotFoundError:
        print(f"Soubor {name} se nepodařilo najít.")
        exit()
    except PermissionError:
        print(f"Soubor {name} není programu přístupný.")
        exit()
    except JSONDecodeError:
        print(f"Soubor {name} je prázdný.")
        exit()

def v_to_number (geo_file):
   """## Kontrola souřadnic
      pokud souřadnice chybí (jedna, nebo obě), program vypíše chybu a skončí"""
   for i in geo_file["features"]:
      if isinstance(i["geometry"]["coordinates"],list):
         try:
            for j in i["geometry"]["coordinates"]:
               j[0] = float(j[0])
               j[1] = float(j[1])
         except IndexError:
            print("Chybí souřadnice, nelze dále pracovat. ")
            exit()
      return (geo_file)

def transfer_coor (x,y):
    """## Převod souřadnicového systému z WGS84 do JTSK
    - vrátí dvojici čísel x a y v souřadnicovém systému JTSK"""
    return wgs2jtsk.transform(x,y)

def is_positive_number (n):
   """Pokusí se převést na číslo, pokud proběhne, zkontroluje, zda je číslo kladné"""
   try:
      number = float(n)
   except ValueError:
      print("Musí být zadané číslo")
      exit()
   if number < 0:
      print("Číslo nesmí být záporné")
      exit()

def distance (point0, point1):
    """## Výpočet vzdálenosti mezi 2 body
    -do parametru vstupují proměnné jakožto dvojice čísel"""
    dist = sqrt((point0[0]-point1[0])**2+(point0[1]-point1[1])**2)
    return dist

 