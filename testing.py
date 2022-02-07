from functions import open_load, transfer_coor, new_geojson
from geometry import LineString

cyklotrasy = open_load("cyklo.geojson")
zvol_vzd = 30
#transformace souřadnic do S-JTSK pokud jsou ve WGS-84
for i in cyklotrasy["features"]:
    if i["geometry"]["coordinates"][0][0]< i["geometry"]["coordinates"][0][1]:
        coor=[]
        if isinstance(i["geometry"]["coordinates"],list):
            for p in i["geometry"]["coordinates"]:
                p=transfer_coor(p[0],p[1])
                coor.append(p)
    else:
        break
    i["geometry"]["coordinates"]= coor

for i in cyklotrasy["features"]:
    if isinstance(i["geometry"]["coordinates"],list):
        geo_s = LineString(i["geometry"]["coordinates"])
        geo_s.divide_long_segments(zvol_vzd)
        modified_list = geo_s.segment_to_point_list()
        #for point in modified_list:
            #print(point)
        i["geometry"]["coordinates"] = modified_list
new_geojson(cyklotrasy, "output_file.geojson")


