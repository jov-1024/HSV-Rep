import maths

class hsv:
    def __init__(self, hue, sat, val):
        self._hue = hue
        self._sat = sat #saturation
        self._val = val #value/brightness

    #since tkinter doesnt support hsv, only rgb values
    #TODO
    def to_rgb(self):
        c = self._val*self._sat #chroma
        h = self._hue/60
        x = c*(1-abs((h%2)-1))
        #bad code help
        temp = []
        if 0 <= h and h < 1:
            temp = [c, x, 0]
        elif 1 <= h and h < 2:
            temp = [x, c, 0]
        elif 2 <= h and h < 3:
            temp = [0, c, x]
        elif 3 <= h and h < 4:
            temp = [0, x, c]
        elif 4 <= h and h < 5:
            temp = [x, 0, c]
        elif 5 <= h and h < 6:
            temp = [c, 0, x]
        m = self._val - c
        temp = list(map(lambda x: x + m, temp))
        temp = list(map(lambda x: maths.to_hex(maths.to_bin(int(maths.map(x, 0.0, 1.0, 0.0, 255.0)))), temp))
        for i in range(len(temp)):
            if len(temp[i]) == 1:
                temp[i] = "0" + temp[i]
        
        return '#' + temp[0] + temp[1] + temp[2]

    #find a complementary high contrast color for text and return another HSV object
    #TODO
    def find_complement(self):
        return hsv((180 + self._hue)%360, self._sat, 1 - self._val)