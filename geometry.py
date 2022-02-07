from functions import distance

class LineString():
    """Vlastní obejkty linestring (-> soubor linií)
    do proměnné my_list se načte celé pole souřadnic
    do proměnné semgments se ukládají souřadnice linií (Segment) tvořené jednotlivými body (Point)"""
    def __init__(self, l_string) -> None:
        self.my_list = l_string
        self.segments = []
        for i in range(len(l_string) - 1): 
            self.segments.append(Segment(Point(l_string[i][0], l_string[i][1]), Point(l_string[i + 1][0], l_string[i + 1][1])))
        
    def divide_long_segments (self, max_lenght):
        """prochází pole liní (segments) a uplatňuje na každý segment metodu divide(max_lenght)"""
        new_segments_list = []
        for segment in self.segments:
            new_segments_list.extend(segment.divide(max_lenght))
        self.my_list = new_segments_list
    
    def segment_to_point_list (self):
        """Tato metoda prochází pole linií (my_list) a vrací nové pole bodů"""
        final_list = []
        for segment in self.my_list:
            final_list.append(segment.p1.xy)
        final_list.append(self.my_list[-1].p2.xy)
        return(final_list)

class Segment():
    """Vlastní obejkty linií, proměnné p1 a p2 jsou body, které tvoří jednu linii"""
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
    def divide(self, max_lenght):
        """Kontroluje, zdali je délka segmentu kratší než stanová vzdálenost (max_lenght).
            - pokud je vzdálenost segmentu kratší než stanovená vzdálenost: - vrátí stejný segment zpět.
            - pokud je vzdálenost segmentu větší než stanovená vzdálenost: - vrátí 2 segmenty s vytvořeným novým bodem"""
        if distance(self.p1.xy,self.p2.xy) < max_lenght:
            return [self]

        else: 
            x=abs((self.p1.xy[0]-self.p2.xy[0])/2) # mezivýpočet pro souřadnici x
            y=abs((self.p1.xy[1]-self.p2.xy[1])/2) # mezivýpočet pro souřadnici y
            # 4 možnosti správného určení nového bodu
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
    """Vlatní objekty bodů, proměnné x a y jsou souřadnice bodu"""
    def __init__(self, x, y) -> None:
        self.xy = [x, y]
