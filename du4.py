import argparse
from functions import is_number, open_load, is_number

parser = argparse.ArgumentParser(exit_on_error=False)

parser.add_argument("-f", "--inputfile", help = "Název vstupního souboru", type = str)
parser.add_argument("-l", "--maxlength", help = "Maximální délka", type = is_number)
parser.add_argument("-o", "--outputfile", help = "Název výstupního souboru")

arguments = parser.parse_args()
'''print(f"Vstupní soubor je {arguments.inputfile}")
print(f"Maximální délka je {arguments.maxlength}")
print(f"Výstupní soubor je {arguments.outputfile}")'''

cyklotrasy = open_load(f"{arguments.inputfile}")
print(cyklotrasy)


