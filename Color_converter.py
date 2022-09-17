
import Utilities as util
import numpy as np

def RGBtoHSV(rgb) :
    red = rgb[0]/255
    green = rgb[1]/255
    blue = rgb[2]/255
    if rgb.size == 4 :
        alpha = rgb[3]

    

    cmax = util.Max(red, util.Max(blue, green))
    cmin = util.Min(red, util.Min(blue, green))

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
    if rgb.size == 4 :
        color = np.array([hue, saturation, value, alpha])
    else :
        color = np.array([hue, saturation, value])
    return color

def HSVtoRGB(hsv) :
    hue = hsv[0]
    saturation = hsv[1]
    value = hsv[2]
    if hsv.size == 4 :
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
    if hsv.size == 4 :
        color = np.array([red, green, blue, alpha])
    else :
        color = np.array([red, green, blue])

    return color


def RGBtoHSL(rgb) :
    red = rgb[0] / 255
    green = rgb[1] / 255
    blue = rgb[2] / 255
    if rgb.size == 4 :
        alpha = rgb[3]

    cmax = util.Max(red, util.Max(blue, green))
    cmin = util.Min(red, util.Min(blue, green))

    delta = cmax - cmin

    """ Luminosity Calculation """

    luminosity = (cmax + cmin) / 2

    """ Saturation Calculation"""

    y = ((2 * luminosity) - 1)
    if y < 0 :
        y = y * -1

    if delta == 0 :
        saturation = 0
    else : 
        saturation = delta / (1 - y)

    """ Hue Calculation """

    if delta == 0 :
        hue = 0
    elif cmax == red :
        hue = 60 * (((green - blue) / delta) % 6)
    elif cmax == green :
        hue = 60 * (((blue - red) / delta) + 2)
    elif cmax == blue :
        hue = 60 * (((red - green) / delta) + 4)

    if rgb.size == 4 :
        color = np.array([hue , saturation, luminosity, alpha])
    else :
        color = np.array([hue, saturation, luminosity])
    return color

def HSLtoRGB(hsl) :
    hue = hsl[0]
    saturation = hsl[1]
    luminosity = hsl[2]
    if hsl.size == 4 :
        alpha = hsl[3]

    """Chroma , X, m calculation"""

    y = ((2 * luminosity) - 1)
    if y < 0 :
         y = y * -1
    chroma = (1 - y) * saturation

    y = (((hue / 60) % 2) - 1)
    if y < 0 :
        y = y * -1
    x = chroma * ( 1 - y)

    m = luminosity - (chroma / 2)

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

    if hsl.size == 4 :
        color = np.array([red, green, blue, alpha])
    else :
        color = np.array([red, green, blue])

    return color
