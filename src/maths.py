#for math-heavy functions

#maps value from a specified range to another
def map(val, from_beg, to_beg, from_end, to_end):
    """
           value                  map
    ------------------- = -------------------
    beg interval height   end interval height
    """
    return val*(to_end-from_end)/(to_beg-from_beg)

def to_bin(num):
    int(num)
    bin = ""
    while (num != 0):
        rem = num%2
        bin += str(rem)
        num = num//2
    return bin[::-1]

def to_hex(bin):
    hex = ""
    l = list(bin)[::-1]
    while len(l)%4 != 0:
        l.append('0')
    l = l[::-1]
    for i in range(0, len(l), 4):
        temp = l[i] + l[i+1] + l[i+2] + l[i+3]
        temp = temp[::-1]
        val = 0
        for i in range(4):
            val += int(temp[i])*(2**i)
        if val >= 10:
            match val:
                case 10:
                    hex += "A"
                case 11:
                    hex += "B"
                case 12:
                    hex += "C"
                case 13:
                    hex += "D"
                case 14:
                    hex += "E"
                case 15:
                    hex += "F"
        else:
            hex += str(val)
    return hex
