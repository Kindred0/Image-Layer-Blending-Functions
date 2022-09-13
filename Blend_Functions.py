
import Color_converter as cc
import Layer
import Utilities as util

""" All Binary Blending Functions takes two layers , Base layer and Upper layer, the Base layer always 
    underneath the Upper layer. The resultant layer takes the dimension of the Base layer """



















""" The Addition Blending Funcion takes the RGB channels of the images/layers and adds them together. 
    The overall effect of Addition Blend is that it will have a brightning effect. """


def addition(Upper, Base, lock) :    


    # Checks if the given layers are emty or not

    # If the Upper layer is empty and Base layer contains image, Base layer is returned and vice versa

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    # If both of them are empty then an empty layer is returned 

    if Base == None and Upper == None :

        return None

    #Finding the smallest of the two layers

    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    #The resultant layer takes the dimension of the Base layer and inital matrix

    resultant = Base
 

    #Checks if the Base layer is alpha locked 
    
    if lock == 0 :
        

        #The actual addition blending Function

        for i in range(0, length) :
            for k in range(0, height) :

                #Resultant layer takes the largest alpha channel of the two layers

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    #If yes, the alpha value is replaced by the greater alpha value

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]
                    


                alphaB = Base.Alpha[i][k] / 255
                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                #The RGB channels of the resultant layer is replaced with the sum of the RGB channels of the two layers

                for m in range(0, 3) :

                    colorB = Base.rgb[i][k][m]
                    colorU = Upper.rgb[i][k][m]

                    """ R = (Bx + Uy) / z , z = x if x > y else z = y
                        where 
                        R = resultant layer
                        B = Base layer
                        U = Upper layer
                        x = Base alpha channel
                        y = Upper alpha channel
                        z = resultant alpha channel """

                    colorR = Rinverse * ((colorB * alphaB) + (colorU * alphaU))
                    colorR = int(colorR)

                    if colorR > 255 :
                        colorR = 255

                    resultant.rgb[i][k][m] = colorR


    # If the alpha lock is true
    elif lock == 1 :
        
        for i in Base.sparce :

            resultant.rgb[i[0]][i[1]] = Base.rgb[i[0]][i[1]]

            # Checks if the length and height goes past the limit

            if i[0] > length or i[1] > height:

                continue

            alphaB = Base.Alpha[i[0]][i[1]] / 255
            alphaU = Upper.Alpha[i[0]][i[1]] / 255
            if resultant.rgb[i[0]][i[1]][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i[0]][i[1]][3]


            for m in range(0, 3) :

                    colorB = Base.rgb[i[0]][i[1]][m]
                    colorU = Upper.rgb[i[0]][i[1]][m]


                    colorR = Rinverse * ((colorB * alphaB) + (colorU * alphaU))
                    colorR = int(colorR)

                    if colorR > 255 :
                        colorR = 255

                    resultant.rgb[i[0]][i[1]][m] = colorR

    resultant.Update_image()

    return resultant



















""" The Subtraction Blend takes the RGB channels of the two layers. RGB channels of the Upper Layer is subtracted from 
    the RGB channels of the Base layer. The overall effect is that it will take a darkening effect."""    


def subtraction(Upper, Base, lock = 0) :

    # Checks if the given layers are emty or not

    # If the Upper layer is empty and Base layer contains image, Base layer is returned and vice versa

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    # If both of them are empty then an empty layer is returned 

    if Base == None and Upper == None :

        return None

    #Finding the smallest of the two layers

    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    #The resultant layer takes the dimension of the Base layer and inital matrix

    resultant = Base
 

    #Checks if the Base layer is alpha locked 
    
    if lock == 0 :
        

        #The actual addition blending Function

        for i in range(0, length) :
            for k in range(0, height) :

                #Resultant layer takes the largest alpha channel of the two layers

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    #If yes, the alpha value is replaced by the greater alpha value

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]
                    


                alphaB = Base.Alpha[i][k] / 255
                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                #The RGB channels of the resultant layer is replaced with the sum of the RGB channels of the two layers

                for m in range(0, 3) :

                    colorB = Base.rgb[i][k][m]
                    colorU = Upper.rgb[i][k][m]

                    """ R = (Bx - Uy) / z , z = x if x > y else z = y
                        where 
                        R = resultant layer
                        B = Base layer
                        U = Upper layer
                        x = Base alpha channel
                        y = Upper alpha channel
                        z = resultant alpha channel """

                    colorR = Rinverse * ((colorB * alphaB) - (colorU * alphaU))
                    colorR = int(colorR)

                    if colorR < 0 :
                        colorR = 0

                    resultant.rgb[i][k][m] = colorR


    # If the alpha lock is true
    elif lock == 1 :
        
        for i in Base.sparce :

            resultant.rgb[i[0]][i[1]] = Base.rgb[i[0]][i[1]]

            # Checks if the length and height goes past the limit

            if i[0] > length or i[1] > height:

                continue

            alphaB = Base.Alpha[i[0]][i[1]] / 255
            alphaU = Upper.Alpha[i[0]][i[1]] / 255
            if resultant.rgb[i[0]][i[1]][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i[0]][i[1]][3]


            for m in range(0, 3) :

                    colorB = Base.rgb[i[0]][i[1]][m]
                    colorU = Upper.rgb[i[0]][i[1]][m]


                    colorR = Rinverse * ((colorB * alphaB) - (colorU * alphaU))
                    colorR = int(colorR)

                    if colorR < 0 :
                        colorR = 0

                    resultant.rgb[i[0]][i[1]][m] = colorR

    resultant.Update_image()

    return resultant























""" The Normal Blend takes the RGBHSLV channels of the Upper Layer  and replaces it with RGBHSLV channels of the Base layer
    under normal condition. Normal Condition being the alpha transparency of the Upper layer being 100%. While not 
    under normal condition the Normal Blend takes the the RGBHSLV channels of both layers and combines them according 
    to the equation. Under Normal Condition Normal Blend will look exactly like the Upper layer. """


def normal(Upper, Base, lock = 0) :


    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None






    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base

    #The Normal blending Function
    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                for m in range (0, 3) :

                    colorB = Base.rgb[i][k][m] * alphaB
                    colorU = Upper.rgb[i][k][m]

                    """ B' = Bx / 255
                        R  = (B'(1 - y) + Uy) / 255"""


                    colorR = ((colorB * (1 - alphaU)) + (colorU * alphaU)) * Rinverse

                    colorR = int(colorR)

                    if colorR > 255 :
                        colorR = 255
                    elif colorR < 0 :
                        colorR = 0

                    resultant.rgb[i][k][m] = colorR



    elif lock == 1 :
        
        for i in Base.sparce :

            resultant.rgb[i[0]][i[1]] = Base.rgb[i[0]][i[1]]


            if i[0] > length or i[1] > height:

                continue

            alphaB = Base.Alpha[i[0]][i[1]] / 255
            alphaU = Upper.Alpha[i[0]][i[1]] / 255
            if resultant.rgb[i[0]][i[1]][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i[0]][i[1]][3]

            for m in range(0, 3) :

                    colorB = Base.rgb[i[0]][i[1]][m] * alphaB
                    colorU = Upper.rgb[i[0]][i[1]][m]


                    colorR = ((colorB * (1 - alphaU)) + (colorU * alphaU)) * Rinverse
                    colorR = int(colorR)

                    if colorR > 255 :
                        colorR = 255
                    elif colorR < 0 :
                        colorR = 0

                    resultant.rgb[i[0]][i[1]][m] = colorR


    resultant.Update_image()


    return resultant
























""" The Multiply Blend takes the HS channels of Base Layer and replaces it with HS channels of the Upper Layer.
    This Blend will also take the L channel of both the Base layer and Upper layer and multiplies them. The Resultant 
    Layer will take Upper Layer but with Luminosity of the Combination of both Layers. This Blend also has a darkening 
    effect. But the same multiply operation can be done in RGB channels as well. """

def multiply(Upper, Base, lock = 0) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None


    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base


    resultant = Base

    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                hsvB = cc.RGBtoHSL(Base.rgb[i][k])
                hsvU = cc.RGBtoHSL(Upper.rgb[i][k])
                hsvB[1] = hsvB[1] * alphaB
                hsvU[1] = hsvU[1] * alphaU
                
                colorR = hsvU
                colorR[2] = hsvU[2] * hsvB[2]

                if colorR[2] > 100 :
                    colorR[2] = 100
                elif colorR[2] < 0 :
                    colorR[2] = 0

                colorR = cc.HSLtoRGB(colorR)
                colorR[3] = resultant.rgb[i][k][3]

                resultant.rgb[i][k] = colorR


    elif lock == 1 :

        for v in Base.sparce :


            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k] / 255
            alphaU = Upper.Alpha[i][k] / 255
            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]


            hsvB = cc.RGBtoHSL(Base.rgb[i][k])
            hsvU = cc.RGBtoHSL(Upper.rgb[i][k])
            hsvB[1] = hsvB[1] * alphaB
            hsvU[1] = hsvU[1] * alphaU


            colorR = hsvU
            colorR[2] = hsvU[2] * hsvB[2]


            if colorR[2] > 100 :
                colorR[2] = 100
            elif colorR[2] < 0 :
                colorR[2] = 0


            colorR = cc.HSLtoRGB(colorR)
            colorR[3] = resultant.rgb[i][k][3]

            resultant.rgb[i][k] = colorR



    resultant.Update_image()

    return resultant




























""" The Devide Blend takes the L channel of both the layers. The colors of the upper layer are inverted and its 
    L channel is multiplied with that of the L channel of Base Layer. The resultant layer takes the hues of 
    Upper layer."""


def devide(Upper, Base, lock = 1) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None


    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base


    resultant = Base

    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                hsvB = cc.RGBtoHSL(Base.rgb[i][k])
                hsvU = cc.RGBtoHSL(Upper.rgb[i][k])
                hsvB[1] = hsvB[1] * alphaB
                hsvU[1] = hsvU[1] * alphaU

                hsvU[0] = (hsvU[0] + 180 ) % 360
                
                colorR = hsvU
                colorR[2] = hsvU[2] * hsvB[2]

                if colorR[2] > 100 :
                    colorR[2] = 100
                elif colorR[2] < 0 :
                    colorR[2] = 0

                colorR = cc.HSLtoRGB(colorR)
                colorR[3] = resultant.rgb[i][k][3]

                resultant.rgb[i][k] = colorR


    elif lock == 1 :

        for v in Base.sparce :


            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k] / 255
            alphaU = Upper.Alpha[i][k] / 255
            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]


            hsvB = cc.RGBtoHSL(Base.rgb[i][k])
            hsvU = cc.RGBtoHSL(Upper.rgb[i][k])
            hsvB[1] = hsvB[1] * alphaB
            hsvU[1] = hsvU[1] * alphaU

            hsvU[0] = (hsvU[0] + 180 ) % 360

            colorR = hsvU
            colorR[2] = hsvU[2] * hsvB[2]


            if colorR[2] > 100 :
                colorR[2] = 100
            elif colorR[2] < 0 :
                colorR[2] = 0


            colorR = cc.HSLtoRGB(colorR)
            colorR[3] = resultant.rgb[i][k][3]

            resultant.rgb[i][k] = colorR



    resultant.Update_image()

    return resultant























""" The darken mode takes the RGB channels of both the layers and keeps whichever is smaller. The overall effect is that it 
    will remove all the colors brighter than a certain limit and thus remove contrast."""

def darken(Upper, Base, lock = 0) :


    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None






    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base


    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                for m in range (0, 3) :

                    colorB = Base.rgb[i][k][m] * alphaB
                    colorU = Upper.rgb[i][k][m] * alphaU

                    colorR = util.Min(colorB, colorU)

                    resultant.rgb[i][k][m] = colorR * Rinverse



    elif lock == 1 :
        
        for v in Base.sparce :

            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k] / 255
            alphaU = Upper.Alpha[i][k] / 255
            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]

            for m in range (0, 3) :

                    colorB = Base.rgb[i][k][m] * alphaB
                    colorU = Upper.rgb[i][k][m] * alphaU

                    colorR = util.Min(colorB, colorU)

                    resultant.rgb[i][k][m] = colorR * Rinverse



    resultant.Update_image()


    return resultant



























""" Lighten Blend takes the RGB channels of the two layers and keeps the largest of the two layers. The overall effect is 
    that it will remove all the layers dimmer than a certain limit and thus remove contrast. """



def lighten(Upper, Base, lock) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None






    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base


    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                for m in range (0, 3) :

                    colorB = Base.rgb[i][k][m] * alphaB
                    colorU = Upper.rgb[i][k][m] * alphaU

                    colorR = util.Max(colorB, colorU)

                    resultant.rgb[i][k][m] = colorR * Rinverse



    elif lock == 1 :
        
        for v in Base.sparce :

            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k] / 255
            alphaU = Upper.Alpha[i][k] / 255
            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]

            for m in range (0, 3) :

                    colorB = Base.rgb[i][k][m] * alphaB
                    colorU = Upper.rgb[i][k][m] * alphaU

                    colorR = util.Max(colorB, colorU)

                    resultant.rgb[i][k][m] = colorR * Rinverse



    resultant.Update_image()


    return resultant





























""" Erase Blend Erases the Base Layer according to the Upper layer. The alpha channel of the Upper layer is subtracted from 
    alpha channel of the base layer. The resultant layer will be transparent image."""

def Erase(Upper, Base, lock = 0) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None






    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base


    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                
                alphaB = Base.Alpha[i][k]
                alphaU = Upper.Alpha[i][k]

                alphaR = alphaB - alphaU
                if alphaR < 0 :
                    alphaR = 0

                resultant.rgb[i][k][3] = alphaR
                resultant.Alpha[i][k] = alphaR

                if resultant.rgb[i][k][3] == 0:
                    resultant.rgb[i][k][0] = 0
                    resultant.rgb[i][k][1] = 0
                    resultant.rgb[i][k][2] = 0



    elif lock == 1 :
        
        for v in Base.sparce :

            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k]
            alphaU = Upper.Alpha[i][k]
            alphaR = alphaB - alphaU
            if alphaR < 0 :
                alphaR = 0
            resultant.rgb[i][k][3] = alphaR
            resultant.Alpha[i][k] = alphaR
            if resultant.rgb[i][k][3] == 0:
                resultant.rgb[i][k][0] = 0
                resultant.rgb[i][k][1] = 0
                resultant.rgb[i][k][2] = 0



    resultant.Construct_sparce()
    resultant.Update_image()


    return resultant























""" The Hue Blend replaces the Hue channel of the Upper layer with that of the Base layer."""

def hue(Upper, Base, lock = 0) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None



    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base


    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                hslB = cc.RGBtoHSL(Base.rgb[i][k])
                hslU = cc.RGBtoHSL(Upper.rgb[i][k])

                colorR = [0, 0, 0, 0]
                colorR[0] = hslU[0]
                colorR[1] = hslB[1] * alphaB
                colorR[2] = hslB[2]
                colorR[3] = resultant.rgb[i][k][3]
                colorR = cc.HSLtoRGB(colorR)

                resultant.rgb[i][k] = colorR


    elif lock == 1 :
        
        for v in Base.sparce :

            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k] / 255

            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]

            hslB = cc.RGBtoHSL(Base.rgb[i][k])
            hslU = cc.RGBtoHSL(Upper.rgb[i][k])
            colorR = hslU

            colorR = [0, 0, 0, 0]
            colorR[0] = hslU[0]
            colorR[1] = hslB[1] * alphaB
            colorR[2] = hslB[2]
            colorR[3] = resultant.rgb[i][k][3]
            colorR = cc.HSLtoRGB(colorR)

            resultant.rgb[i][k] = colorR



    resultant.Update_image()

    return resultant






















def saturation(Upper, Base, lock = 0) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None



    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base


    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                hslB = cc.RGBtoHSL(Base.rgb[i][k])
                hslU = cc.RGBtoHSL(Upper.rgb[i][k])

                colorR = [0, 0, 0, 0]
                colorR[0] = hslB[0]
                colorR[1] = hslU[1] * alphaU
                colorR[2] = hslB[2]
                colorR[3] = resultant.rgb[i][k][3]
                colorR = cc.HSLtoRGB(colorR)

                resultant.rgb[i][k][0] = colorR[0] * Rinverse
                resultant.rgb[i][k][1] = colorR[1] * Rinverse
                resultant.rgb[i][k][2] = colorR[2] * Rinverse


    elif lock == 1 :
        
        for v in Base.sparce :

            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaU = Upper.Alpha[i][k] / 255
            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]

            hslB = cc.RGBtoHSL(Base.rgb[i][k])
            hslU = cc.RGBtoHSL(Upper.rgb[i][k])

            colorR = [0, 0, 0, 0]
            colorR[0] = hslB[0]
            colorR[1] = hslU[1] * alphaU
            colorR[2] = hslB[2]
            colorR[3] = resultant.rgb[i][k][3]
            colorR = cc.HSLtoRGB(colorR)
            
            resultant.rgb[i][k][0] = colorR[0] * Rinverse
            resultant.rgb[i][k][1] = colorR[1] * Rinverse
            resultant.rgb[i][k][2] = colorR[2] * Rinverse



    resultant.Update_image()

    return resultant
























def luminosity(Upper, Base, lock = 0) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None



    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base


    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                hslB = cc.RGBtoHSL(Base.rgb[i][k])
                hslU = cc.RGBtoHSL(Upper.rgb[i][k])

                colorR = [0, 0, 0, 0]
                colorR[0] = hslB[0]
                colorR[1] = hslB[1] * alphaB
                colorR[2] = hslU[2]
                colorR[3] = resultant.rgb[i][k][3]
                colorR = cc.HSLtoRGB(colorR)

                resultant.rgb[i][k][0] = colorR[0] * Rinverse
                resultant.rgb[i][k][1] = colorR[1] * Rinverse
                resultant.rgb[i][k][2] = colorR[2] * Rinverse


    elif lock == 1 :
        
        for v in Base.sparce :

            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k] / 255
            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]

            hslB = cc.RGBtoHSL(Base.rgb[i][k])
            hslU = cc.RGBtoHSL(Upper.rgb[i][k])

            colorR = [0, 0, 0, 0]
            colorR[0] = hslB[0]
            colorR[1] = hslB[1] * alphaB
            colorR[2] = hslU[2]
            colorR[3] = resultant.rgb[i][k][3]
            colorR = cc.HSLtoRGB(colorR)
            
            resultant.rgb[i][k][0] = colorR[0] * Rinverse
            resultant.rgb[i][k][1] = colorR[1] * Rinverse
            resultant.rgb[i][k][2] = colorR[2] * Rinverse



    resultant.Update_image()

    return resultant














def value(Upper, Base, lock = 0) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None



    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base


    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                hslB = cc.RGBtoHSV(Base.rgb[i][k])
                hslU = cc.RGBtoHSV(Upper.rgb[i][k])

                colorR = [0, 0, 0, 0]
                colorR[0] = hslB[0]
                colorR[1] = hslB[1] * alphaB
                colorR[2] = hslU[2]
                colorR[3] = resultant.rgb[i][k][3]
                colorR = cc.HSVtoRGB(colorR)

                resultant.rgb[i][k][0] = colorR[0] * Rinverse
                resultant.rgb[i][k][1] = colorR[1] * Rinverse
                resultant.rgb[i][k][2] = colorR[2] * Rinverse


    elif lock == 1 :
        
        for v in Base.sparce :

            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k] / 255
            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]

            hslB = cc.RGBtoHSV(Base.rgb[i][k])
            hslU = cc.RGBtoHSV(Upper.rgb[i][k])

            colorR = [0, 0, 0, 0]
            colorR[0] = hslB[0]
            colorR[1] = hslB[1] * alphaB
            colorR[2] = hslU[2]
            colorR[3] = resultant.rgb[i][k][3]
            colorR = cc.HSVtoRGB(colorR)
            
            resultant.rgb[i][k][0] = colorR[0] * Rinverse
            resultant.rgb[i][k][1] = colorR[1] * Rinverse
            resultant.rgb[i][k][2] = colorR[2] * Rinverse



    resultant.Update_image()

    return resultant













def overlay(Upper, Base, lock = 0) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None



    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base

    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                for m in range (0, 3) :

                    colorB = (Base.rgb[i][k][m] * alphaB) / 255
                    colorU = (Upper.rgb[i][k][m] * alphaU) / 255

                    if colorB < 0.5 :
                        colorR = 2 * colorB * colorU
                    
                    else :
                        colorR = 1 - (2 * (1 - colorB) * (1 - colorU))
                    
                    colorR = int(colorR)
                    colorR = colorR * 255
                    resultant.rgb[i][k][m] = colorR * Rinverse

    elif lock == 1 :

        for v in Base.sparce :

            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k] / 255
            alphaU = Upper.Alpha[i][k] / 255

            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]


            for m in range (0, 3) :
                colorB = (Base.rgb[i][k][m] * alphaB) / 255
                colorU = (Upper.rgb[i][k][m] * alphaU) / 255


                if colorB < 0.5 :
                    colorR = 2 * colorB * colorU
                
                else :
                    colorR = 1 - (2 * (1 - colorB) * (1 - colorU))
                

                colorR = int(colorR)
                colorR = colorR * 255
                resultant.rgb[i][k][m] = colorR * Rinverse

    resultant.Update_image()

    return resultant













def screen(Upper, Base, lock = 0) :

    if Upper == None and Base != None:

        return Base

    if Base == None and Upper != None :

        return Upper

    if Base == None and Upper == None :

        return None



    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]

    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    resultant = Base

    if lock == 0 :

        for i in range(0, length) :
            for k in range(0, height) :

                if Base.Alpha[i][k] < Upper.Alpha[i][k] :

                    resultant.rgb[i][k][3] = Upper.Alpha[i][k]
                    resultant.Alpha[i][k] = Upper.Alpha[i][k]

                else :

                    resultant.rgb[i][k][3] = Base.Alpha[i][k]
                    resultant.Alpha[i][k] = Base.Alpha[i][k]

                alphaB = Base.Alpha[i][k] / 255
                alphaU = Upper.Alpha[i][k] / 255
                if resultant.rgb[i][k][3] == 0:
                    Rinverse = 0
                else :
                    Rinverse = 255 / resultant.rgb[i][k][3]

                for m in range (0, 3) :

                    colorB = (Base.rgb[i][k][m] * alphaB) / 255
                    colorU = (Upper.rgb[i][k][m] * alphaU) / 255

                    
                    colorR = colorB + colorU - (colorU * colorB)
                    
                    colorR = int(colorR)
                    colorR = colorR * 255
                    resultant.rgb[i][k][m] = colorR * Rinverse

    elif lock == 1 :

        for v in Base.sparce :

            i = v[0]
            k = v[1]

            resultant.rgb[i][k] = Base.rgb[i][k]


            if i > length or k > height:

                continue

            alphaB = Base.Alpha[i][k] / 255
            alphaU = Upper.Alpha[i][k] / 255

            if resultant.rgb[i][k][3] == 0:
                Rinverse = 0
            else :
                Rinverse = 255 / resultant.rgb[i][k][3]


            for m in range (0, 3) :
                colorB = (Base.rgb[i][k][m] * alphaB) / 255
                colorU = (Upper.rgb[i][k][m] * alphaU) / 255


                colorR = colorB + colorU - (colorU * colorB)
                

                colorR = int(colorR)
                colorR = colorR * 255
                resultant.rgb[i][k][m] = colorR * Rinverse

    resultant.Update_image()

    return resultant


