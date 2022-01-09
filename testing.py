from functions import open_load, transfer_coor, distance
from geometry import LineString, Point, Segment

cyklotrasy = open_load("cyklo.geojson")
zvol_vzd = 18
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
        #print(geo_s.my_list) #-> tiskne celý list souřadnic linestringu
        
    for j in range(len(geo_s.my_list)-1):
        print(j)
        line = geo_s.my_list[j],geo_s.my_list[j+1]
        geo_l = Segment(line)
        print(geo_l.line)
        p1 = Point(geo_s.my_list[j][0],geo_s.my_list[j][1])
        p2 = Point(geo_s.my_list[j+1][0], geo_s.my_list[j+1][1])
        #print(geo_s.my_list[j], geo_s.my_list[j+1])
        #print(f"Bod 1: souřadnice x je {p1.x} a souřadnice y je {p1.y}\nBod 2: souřadnice x je {p2.x} a souřadnice y je {p2.y}")
        vzdalenost = distance(p1.xy(),p2.xy())
        print(f"Vzdálenost bodů: {vzdalenost:.2f} m")
        if vzdalenost > zvol_vzd:
            x=abs((p1.x-p2.x)/2)
            y=abs((p1.y-p2.y)/2) # mezivýpočet x a y
            if p1.x<p2.x:
                if p1.y<p2.y:
                    new_p = Point(p1.x+x,p1.y+y)
                else:
                    new_p = Point(p1.x+x,p1.y-y)
            else:
                if p1.y<p2.y:
                    new_p = Point(p1.x-x,p1.y+y)
                else:
                    new_p = Point(p1.x-x,p1.y-y)
            print(f"Přidávám nový bod: {new_p.xy()}")

            print(vzdalenost)
        

#print(cyklotrasy)
