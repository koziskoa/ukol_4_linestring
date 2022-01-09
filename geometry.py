#from abc import ABC, abstractmethod

class LineString():
    """Vlastní obejkty linestring (-> soubor linií)"""
    def __init__(self, l_string) -> None:
        self.my_list = l_string
    """def out (self, moje):
        return moje"""   #asi to npotřebuju
    def devide_long_segments (self, max_lenght):
        #Jethrem popsaný algoritmus bude aplikovat sama na sebe
        # vezme si ten seznam a řekne na tom řádku kde stojíš
        pass

        
class Segment():
    """Vlastní obejkty čar"""
    def __init__(self, line) -> None:
        self.line = line
    def devide():
        #idk
        pass
class Point ():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def xy (self):
        """Vrátí souřadnice bodu jako dvojici"""
        x_y =(self.x, self.y)
        return(x_y)
