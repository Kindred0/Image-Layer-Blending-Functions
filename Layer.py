
from csv import writer
import Color_converter as color
from PIL import Image
import numpy


class layer :
    def __init__(self, row, coloumn) :

        self.rgb = numpy.zeros([row, coloumn, 4])

        self.image = Image.fromarray(self.rgb)

        self.hsv = numpy.zeros([row, coloumn, 4])
        
        self.shape = (row, coloumn)

        self.Alpha = numpy.array([])

        self.mode = "rgba" 

    def __init__(self, i) :

        """ The Actual Image """
        self.image = Image.open(i)

        """ The matrix of the image in RGB """
        self.rgb = numpy.asarray(self.image)
        self.rgb = self.rgb.copy()
        self.rgb.setflags(write=1)

        """ Dimension of the image """
        self.shape = self.image.size

        """ The matrix of the image in HSV """
        self.hsv = numpy.zeros([self.shape[0], self.shape[1], 4])

        """ The sparce matrix of the image of non-zero alpha's """
        self.Alpha = numpy.array([])

        """ The type of image """
        self.mode = self.image.mode

        """ Obtaining the HSV matrix from the RGB matrix """
        for i in range(0, self.shape[0]) :
            for k in range(0, self.shape[1]) :
                self.hsv[i][k] = color.to_hsv(self.rgb[i][k])



    """ To update the image in case the RGB matrix is transformed """
    def Update_image(self) :
        self.image = Image.fromarray(self.rgb)


    """ To update the RGB matrix in case the HSV matrix is transformed """
    def Update_RGB(self) :
        for i in range(0, self.shape[0]) :
            for k in range(0, self.shape[1]) :
                self.rgb[i][k] = color.to_rgb(self.hsv[i][k])
        self.Update_image()


    """ To Update the HSV matrix in case the RGB matrix is transformed """
    def Update_HSV(self) :
        for i in range(0, self.shape[0]) :
            for k in range(0, self.shape[1]) :
                self.hsv[i][k] = color.to_hsv(self.rgb[i][k])


    def __del__(self) :
        self.image.close()


    def show(self) :
        self.image.show()


    def show_rgb(self) :
        for i in self.rgb :
            print("\n\nrow\n")
            for k in i :
                print(k, end= " ")


    def show_HSV(self) :
        for i in self.hsv :
            print("\n\nrow\n")
            for k in i :
                print(k, end= " ")


