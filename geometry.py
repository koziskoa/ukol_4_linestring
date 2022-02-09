from math import sqrt

class LineString():
    """Vlastní obejkty linestring (-> soubor linií)
    do proměnné my_list se načte celé pole souřadnic
    do proměnné semgments se ukládají souřadnice linií (Segment) tvořené jednotlivými body (Point)"""
    def __init__(self, l_string) -> None:
        self.segments = []
        for i in range(len(l_string) - 1): 
            self.segments.append(Segment(Point(l_string[i][0], l_string[i][1]), Point(l_string[i + 1][0], l_string[i + 1][1])))
        
    def divide_long_segments (self, max_length):
        """prochází pole liní (segments) a uplatňuje na každý segment metodu divide(max_lenght)"""
        new_segments_list = []
        for segment in self.segments:
            new_segments_list.extend(segment.divide(max_length))
        self.segments = new_segments_list
    
    def segment_to_point_list (self):
        """Tato metoda prochází pole linií (my_list) a vrací nové pole bodů"""
        final_list = []
        for segment in self.segments:
            final_list.append([segment.p1.x, segment.p1.y])
        final_list.append([self.segments[-1].p2.x, self.segments[-1].p2.y])
        return(final_list)

class Segment():
    """Vlastní obejkty linií, proměnné p1 a p2 jsou body, které tvoří jednu linii"""
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
    def distance (self):
        return sqrt((self.p1.x-self.p2.x)**2+(self.p1.y-self.p2.y)**2)
    def divide(self, max_length):
        """Kontroluje, zdali je délka segmentu kratší než stanová vzdálenost (max_length).
            - pokud je vzdálenost segmentu kratší než stanovená vzdálenost: - vrátí stejný segment zpět.
            - pokud je vzdálenost segmentu větší než stanovená vzdálenost: - vrátí 2 segmenty s vytvořeným novým bodem"""
        if self.distance() < max_length:
            return [self]

        else: 
            x=(self.p1.x+self.p2.x)/2 # mezivýpočet pro souřadnici x
            y=(self.p1.y+self.p2.y)/2 # mezivýpočet pro souřadnici y
            new_p = Point(x, y)
            line1= Segment(self.p1,new_p)
            line2= Segment(new_p,self.p2)
            new_line1 = line1.divide(max_length)
            new_line2 = line2.divide(max_length)
            return new_line1 + new_line2

class Point ():
    """Vlatní objekty bodů, proměnné x a y jsou souřadnice bodu"""
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
