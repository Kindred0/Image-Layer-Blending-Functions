
def Max(a, b) :
    if a > b :
        return a
    elif b > a :
        return b
    else :
        return a


def Min(a, b) :
    if a < b :
        return a   
    elif b < a :
        return b
    return a 


def to_hsv(rgb) :
    red = rgb[0]/255
    green = rgb[1]/255
    blue = rgb[2]/255
    alpha = rgb[3]

    cmax = Max(red, Max(blue, green))
    cmin = Min(red, Min(blue, green))

    """ Value calculation """

    value = cmax

    """ Hue calculation """

    delta = cmax - cmin

    if delta == 0 :
        hue = 0
    elif cmax == red :
        hue = 60 * (((green - blue) / delta) % 6)
    elif cmax == green :
        hue = 60 * (((blue - red) / delta) + 2)
    elif cmax == blue :
        hue = 60 * (((red - green) / delta) + 4)

    """ Saturation calculation """

    if cmax == 0 :
        saturation = 0
    else : 
        saturation = delta / cmax

    color = [hue , saturation, value, alpha]
    return color

def to_rgb(hsv) :
    hue = hsv[0]
    saturation = hsv[1]
    value = hsv[2]
    alpha = hsv[3]

    """Chroma , X, m calculation"""

    chroma = value * saturation

    y = (((hue / 60) % 2) - 1)
    if y < 0 :
        y = y * -1
    x = chroma * ( 1 - y)

    m = value - chroma

    """ Checking for color range """

    if 0 <= hue and hue < 60 :
        rgb = [chroma, x, 0]
    elif 60 <= hue and hue < 120 :
        rgb = [x, chroma, 0]
    elif 120 <= hue and hue < 180 :
        rgb = [0, chroma, x]
    elif 180 <= hue and hue < 240 :
        rgb = [0, x, chroma]
    elif 240 <= hue and hue < 300 :
        rgb = [x, 0, chroma]
    elif 300 <= hue and hue < 360 :
        rgb = [chroma, 0, x]
    else :
        rgb = [0, 0, 0]

    """ Assigning colors """

    red = (rgb[0] + m) * 255
    green = (rgb[1] + m) * 255
    blue = (rgb[2] + m) * 255 

    """ Converting colors to integer values as RGB only supports integers """

    red = int(red)
    green = int(green)
    blue = int(blue)

    color = [red, green, blue, alpha]

    return color
