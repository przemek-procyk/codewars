def check_value(value):
    if value < 0:
        return 0
    elif value > 255:
        return 255
    else:
        return value

def rgb_2(r,g,b):
    return '{:02X}{:02X}{:02X}'.format(check_value(r), check_value(g), check_value(b))



def rgb(r, g, b):
    r_checker = r in range(0, 256)
    if r_checker is True:
        pass
    else:
        if r_checker is False and r < 0:
            r = 0
        else:
            r = 255
    g_checker = g in range(0, 256)
    if g_checker is True:
        pass
    else:
        if g_checker is False and g < 0:
            g = 0
        else:
            g = 255
    b_checker = b in range(0, 256)
    if b_checker is True:
        pass
    else:
        if b_checker is False and b < 0:
            b = 0
        else:
            b = 255
    return '{:02X}{:02X}{:02X}'.format(r, g, b)
