import Layer

def addition(Upper, Base) :    
    dimension = Base.shape

    """ The resultant layer takes the dimension of the Base layer and inital matrix """

    resultant = Base


    """ Finding the smallest of the teo layers """

    if Base.shape[0] < Upper.shape[0] :
        length = Base.shape[0]
    else :
        length = Upper.shape[0]
    if Base.shape[1] < Upper.shape[1] :
        height = Base.shape[1]
    else :
        height = Upper.shape[1]

    """ The actual addition blending Function """

    for i in range(0, length) :
        for k in range(0, height) :

            """ Inititally the upper layer is projected to the base layer """

            resultant.hsv[i][k] = Upper.hsv[i][k]

            """ The value points in the HSV matrix is replaced the sum of the value points of the two layers"""

            value = Base.hsv[i][k][2] + Upper.hsv[i][k][2]
            if value > 100 :
                value = 100
            elif value < 0 :
                value = 0
            resultant.hsv[i][k][2] = value

    resultant.Update_RGB()
    return resultant

    
    