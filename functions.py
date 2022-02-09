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
            reader_n = coor_control(reader)
        return reader_n
    
    except FileNotFoundError:
        print(f"Soubor {name} se nepodařilo najít.")
        exit()
    except PermissionError:
        print(f"Soubor {name} není programu přístupný.")
        exit()
    except JSONDecodeError:
        print(f"Soubor {name} nelze dekódovat.")
        exit()

def coor_control (geo_file):
   """## Kontrola souřadnic
      pokud souřadnice chybí (jedna, nebo obě), program vypíše chybu a skončí"""
   for feature in geo_file["features"]:
      if isinstance(feature["geometry"]["coordinates"],list):
         try:
            for coords in feature["geometry"]["coordinates"]:
               coords[0] = float(coords[0])
               coords[1] = float(coords[1])
         except IndexError:
            print("Chybí souřadnice, nelze dále pracovat. ")
            exit()
      return (geo_file)

def transfer_coor (x,y):
    """## Převod souřadnicového systému z WGS84 do JTSK
    - vrátí dvojici čísel x a y v souřadnicovém systému JTSK"""
    return wgs2jtsk.transform(x,y)

def is_positive_int (n):
   """Pokusí se převést na číslo, pokud proběhne, zkontroluje, zda je číslo kladné"""
   try:
      number = int(n)
      if number < 0:
         print("V argumentu -l nesmí být číslo záporné")
         exit()
      return(number)
   except ValueError:
      print("Do argumentu -l musí být zadané číslo")
      exit()
   

def new_geojson (var, name):
    """## Vytvoří ze slovníku nový soubor GEOJSON
    """
    try:
     with open(name, "w", encoding="utf-8") as outfile:
      json.dump(var, outfile, indent=5)
    except Exception:
      print("Soubor se nepodařilo zapsat.")

 