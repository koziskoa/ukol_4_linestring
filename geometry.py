from functions import distance

class LineString():
    """Vlastní obejkty linestring (-> soubor linií)"""
    def __init__(self, l_string) -> None:
        self.my_list = l_string
        self.segments = []
        for i in range(len(l_string) - 1): 
            self.segments.append(Segment(Point(l_string[i][0], l_string[i][1]), Point(l_string[i + 1][0], l_string[i + 1][1])))
        
    def divide_long_segments (self, max_lenght):
        new_segments_list = []
        for segment in self.segments:
            #semi_result = segment.divide(max_lenght)
            #print(f"{semi_result.p1.xy} + {semi_result.p2.xy}")
            new_segments_list.extend(segment.divide(max_lenght))
        self.my_list = new_segments_list
    
    def segment_to_point_list (self):
        final_list = []
        for segment in self.my_list:
            final_list.append(segment.p1.xy)
        final_list.append(self.my_list[-1].p2.xy)
        return(final_list)

class Segment():
    """Vlastní obejkty čar"""
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
    def divide(self, max_lenght):
        if distance(self.p1.xy,self.p2.xy) < max_lenght:
            return [self]

        else: 
            x=abs((self.p1.xy[0]-self.p2.xy[0])/2)
            y=abs((self.p1.xy[1]-self.p2.xy[1])/2)
            if self.p1.xy[0]<self.p2.xy[0]:
                if self.p1.xy[1]<self.p2.xy[1]:
                    new_p = Point(self.p1.xy[0]+x,self.p1.xy[1]+y)
                else:
                    new_p = Point(self.p1.xy[0]+x,self.p1.xy[1]-y)
            else:
                if self.p1.xy[1]<self.p2.xy[1]:
                    new_p = Point(self.p1.xy[0]-x,self.p1.xy[1]+y)
                else:
                    new_p = Point(self.p1.xy[0]-x,self.p1.xy[2]-y)
            line1= Segment(self.p1,new_p)
            line2= Segment(new_p,self.p2)
            new_line1 = line1.divide(max_lenght)
            new_line2 = line2.divide(max_lenght)
            return new_line1 + new_line2

class Point ():
    def __init__(self, x, y) -> None:
        self.xy = [x, y]


'''vzor = {
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
					[ -729114.9620250128, -1047445.0871372782 ],
					[ -729113.5667241365, -1047465.0529498458 ],
					[ -729103.7995179854, -1047550.0110033341 ],
					[ -729100.86941614, -1047574.6584188528 ],
					[ -729095.1458125375, -1047612.6914427951 ],
					[ -729092.5928109288, -1047647.5884647667 ]
				]
			},
			"properties" : {
				"OBJECTID" : 1,
				"CISLO_TRAS" : "A440",
				"CT" : 0,
				"REALIZACE" : 1,
				"JEDNOSMERKA" : 0,
				"DOPR_STAV" : 123,
				"Shape_Length" : 236.41044043711238
			}
		}]}
geo_s = []
geo_l = []
geo_p = []
for i in vzor["features"]:
    if isinstance(i["geometry"]["coordinates"],list):
        geo_s.append(i["geometry"]["coordinates"])
print(geo_s)
geo_s=LineString(geo_s)
geo_s.divide_long_segments(10)
print(geo_s)'''
