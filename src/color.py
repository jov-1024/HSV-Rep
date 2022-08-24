
class hsv:
    def __init__(self, hue, sat, val):
        self._hue = hue
        self._sat = sat #saturation
        self._val = val #value/brightness

    #since tkinter doesnt support hsv, only rgb values
    #TODO
    def to_rgb(self):
        pass 

    #find a complementary high contrast color for text and return another HSV object
    #TODO
    def find_complement(self):
        pass