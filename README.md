# ukol_4_linestring
## Využití programu
Program slouží pro rozdělení linií (segmentů) an menší linie v souboru lomených čar (linestring).
## Základní popis
Program v poli lomených čar zjišťuje délku linie a porovnává ji se zvolenou maximální vzdáleností, kterou zadává uživatel. Pokud je vzdálenost linie větší než maximální stanovená vzdálenost, daná linie se rozdělí na 2 stejně dlouhé linie. Tyto nové 2 linie jsou opět zkontrolovány, jestli je jejich délka kratší než maximální stanovená vzdálenost.
### Vstupní data
Pro správný běh programu je za potřebí mít data v souboru typu `.geojson`. Takový soubor je tovřen slovníkem.

Příklad struktury souboru .geojson:
`{
	"type" : "FeatureCollection",
	"name" : "DOP_Cyklotrasy_l",
	"crs" : {
		"type" : "name",
		"properties" : {
			"name" : "EPSG:5514"
		}
	},
	"features" : [
		{
			"type" : "Feature",
			"geometry" : {
				"type" : "LineString",
				"coordinates" : [
					[ -729120.2305283286, -1047412.9380170368 ],
					[ -729117.334126506, -1047426.4983255751 ],
					[ -729114.9620250128, -1047445.0871372782 ]
				]
		}}]}`
    
Pro účely tohoto programu se dají data stáhnout z [pražského geoportálu](https://www.geoportalpraha.cz/cs/data/otevrena-data/0AF6DE97-68B3-4CD6-AE5D-76ACEEE50636). 
### Stručný popis chodu programu
Před spuštěním programu je třeba vypsat argumenty `-f, -l a -o`, které se později během chodu programu zpracují. Argument `-f` bude nést název souboru s daty, které chce uživatel procházet (např.: **"*-f input.geojson*"**). Argument `-l` slouží pro stanovení maximální délky linie v m. Je tedy třeba zadat celé kladné číslo. (např.**"*-l 15*"**). Do argumentu `-o` se zadá název výstupního souboru (např.: **"*-o output.geojson*"**). Výstupní soubor bude opět typu `.geojson` a pro každé spuštění programu se vytvoří nový výstupní soubor. Všechny zmíněné argumenty jsou povinné. Musí se tedy zadat všechny. V momentě, kdy uživatel nezadá všechny argumenty, porgram nebude funkční. 

Příklad zadávání argumentů: `-f "highways.geojson", -l 20 a -o "modified_highways.geojson"`

Program projde všechna pole (list) lomených čar a zjišťuje vzdálenost každé linie. Tuto vzdálenost pak porovnává se stanovenou maximální vzdáleností, kterou zadává uživatel jako argument `-l`. Pokud je vzdálenost linie menší než maximální stanovená vzdálenost, pak se nestane nic. Pokud však bude vzdálenost větší, tak se tato linie rozdělí na 2 stejně dlouhé segmenty a ty se opět porovnávají se stanovenou maximální vzdáleností.
Výstupní soubor, jehož jméno uživatel zadává v arguemntu `-o`, se uloží do složky, kde se nachází vstupní soubor s daty.
Poznámka: Program pracuje se souřadnicemi v systému S-JTSK. Jako alternativu umí program převést data ze souřadnicového systému WGS-84 na S-JTSK. Výstupní soubor obsahuje souřadnice v souřadnicovém systému S-JTSK.
### Popis souborů s kódy
Pro funkčnost programu jsou třeba soubory `du4.py`, `functions.py` a `geometry.py`. V souboru `du4.py` se nachází hlavní kód programu, který si bere souboru `geometry.py` třídu Linestring. Pro sprévné fungování hlavního kódu i kódu s definovanými třídami je třeba i soubor `functions.py`, který definuje funkce jež oba soubory využívají. 
Pokud uživatel nechce sám zadávat argumenty, může využít soubor `testing.py`, který zpracovává  geojson soubor se jménem `"cyklo.geojson"`. Musí se tedy ujistit, že se jeho soubor bude jmenovat stejně. Nastavená maximální délka je na 30 m. Výstupní soubor se bude jmenovat `output_file.geojson` a bude uložen do stejné složky, kde se nachází vstupní data.
Soubory `cyklo.geojson` (v souřadnicovém systému S-JTSK) a `cyklo_WGS.geojson` (v souřadnicovém systému WGS-84) slouží jako testovací soubory pro správné fungování programu.
