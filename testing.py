from functions import open_load, transfer_coor, new_geojson
from geometry import LineString

linestring = open_load("cyklo.geojson")
zvol_vzd = 30
#transformace souřadnic do S-JTSK pokud jsou ve WGS-84
for feature in linestring["features"]:
    if feature["geometry"]["coordinates"][0][0]< feature["geometry"]["coordinates"][0][1]:
        new_coor=[]
        if isinstance(feature["geometry"]["coordinates"],list):
            for coords in feature["geometry"]["coordinates"]:
                coords=transfer_coor(coords[0],coords[1])
                new_coor.append(coords)
    else:
        break
    feature["geometry"]["coordinates"]= new_coor

for feature in linestring["features"]:
    if isinstance(feature["geometry"]["coordinates"],list):
        geo_s = LineString(feature["geometry"]["coordinates"])
        geo_s.divide_long_segments(zvol_vzd)
        modified_list = geo_s.segment_to_point_list()
        #for point in modified_list:
            #print(point)
        feature["geometry"]["coordinates"] = modified_list
new_geojson(linestring, "output_file.geojson")


