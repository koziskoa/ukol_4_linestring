import json
import argparse
from json.decoder import JSONDecodeError
def open_load (name):
    """# Otevírá soubor typu json 
    - do parametru se zadá název souboru včetně uvozovek např. "soubor.json"
    - vrací obsah souboru"""
    try:
        with open(name, encoding="utf-8") as geojsonfile:
            reader = json.load(geojsonfile)
        return reader
    
    except FileNotFoundError:
        print(f"Soubor {name} se nepodařilo najít.")
        exit()
    except PermissionError:
        print(f"Soubor {name} není programu přístupný.")
        exit()
    except JSONDecodeError:
        print(f"Soubor {name} je prázdný.")
        exit()

def is_number (n):
   try:
      number = int(n)
   except ValueError:
      print("Musí být zadané číslo")
      exit()
   