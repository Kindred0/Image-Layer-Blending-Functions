
import Layer

def addition(Upper, Base) :    

    """ The resultant layer takes the dimension of the Base layer and inital matrix """

    resultant = Base


    """ Finding the smallest of the two layers """

    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]
    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    """ The actual addition blending Function """

    for i in range(0, length) :
        for k in range(0, height) :

            """ Inititally the upper layer is projected to the base layer """

            resultant.rgb[i][k] = Upper.rgb[i][k]

            """ Checks if the alpha is greater for the Upper layer """

            if Base.rgb[i][k][3] > Upper.rgb[i][k][3] :

                """ If yes, the alpha value is replaced by the greater alpha value """

                resultant.rgb[i][k][3] = Base.rgb[i][k][3]

            """ The RGB channels of the resultant layer is replaced with the sum of the RGB channels of the two layers """

            """ Assigning Red Channel """

            color = (Base.rgb[i][k][0] * (Base.rgb[i][k][3] / 255)) + (Upper.rgb[i][k][0] * (Upper.rgb[i][k][3] / 255))

            if color > 255 :
                color = 255
            elif color < 0 :
                color = 0
            
            resultant.rgb[i][k][0] = color

            """ Assigning Green Channel """

            color = (Base.rgb[i][k][1] * (Base.rgb[i][k][3] / 255)) + (Upper.rgb[i][k][1] * (Upper.rgb[i][k][3] / 255))

            if color > 255 :
                color = 255
            elif color < 0 :
                color = 0
            
            resultant.rgb[i][k][1] = color

            """ Assigning Blue Channel """

            color = (Base.rgb[i][k][2] * (Base.rgb[i][k][3] / 255)) + (Upper.rgb[i][k][2] * (Upper.rgb[i][k][3] / 255))

            if color > 255 :
                color = 255
            elif color < 0 :
                color = 0
            
            resultant.rgb[i][k][2] = color


    resultant.Update_HSL()
    return resultant

    
def subtraction(Upper, Base) :

    resultant = Base

    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]
    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]

    """ The actual subtraction blending Function """

    for i in range(0, length) :
        for k in range(0, height) :

            resultant.rgb[i][k] = Upper.rgb[i][k]

            if Base.rgb[i][k][3] > Upper.rgb[i][k][3] :
                resultant.rgb[i][k][3] = Base.rgb[i][k][3]

            """ The RGB channels of the resultant layer is replaced with the RGB channels of Upper subtracted with RGB channels of Base """

            """ Assigning Red Channel """

            color = (Base.rgb[i][k][0] * (Base.rgb[i][k][3] / 255)) - (Upper.rgb[i][k][0] * (Upper.rgb[i][k][3] / 255))

            if color > 255 :
                color = 255
            elif color < 0 :
                color = 0
            
            resultant.rgb[i][k][0] = color

            """ Assigning Green Channel """

            color = (Base.rgb[i][k][1] * (Base.rgb[i][k][3] / 255)) - (Upper.rgb[i][k][1] * (Upper.rgb[i][k][3] / 255))

            if color > 255 :
                color = 255
            elif color < 0 :
                color = 0
            
            resultant.rgb[i][k][1] = color

            """ Assigning Blue Channel """

            color = (Base.rgb[i][k][2] * (Base.rgb[i][k][3] / 255)) - (Upper.rgb[i][k][2] * (Upper.rgb[i][k][3] / 255))

            if color > 255 :
                color = 255
            elif color < 0 :
                color = 0
            
            resultant.rgb[i][k][2] = color


    resultant.Update_HSL()
    return resultant


"""def normal(Upper, Base) :

    resultant = Base

    if Base.dimension[0] < Upper.dimension[0] :
        length = Base.dimension[0]
    else :
        length = Upper.dimension[0]
    if Base.dimension[1] < Upper.dimension[1] :
        height = Base.dimension[1]
    else :
        height = Upper.dimension[1]"""