
from csv import writer
import Color_converter as color
from PIL import Image
import numpy


class layer :
    def __init__(self, row, coloumn) :

        self.rgb = numpy.zeros([row, coloumn, 4])

        self.image = Image.fromarray(self.rgb)

        self.hsl = numpy.zeros([row, coloumn, 4])
        
        self.dimension = (row, coloumn)

        self.Alpha = numpy.array([])

        self.mode = "rgba" 

        self.Opacity = 100

    def __init__(self, i) :

        """ The Actual Image """
        self.image = Image.open(i)

        """ The matrix of the image in RGB """
        self.rgb = numpy.asarray(self.image)

        """ Change the reading mode to read and write """
        self.rgb = self.rgb.copy()
        self.rgb.setflags(write=1)

        """ Dimension of the image """
        self.dimension = self.image.size

        """ The matrix of the image in HSL """
        self.hsl = numpy.zeros([self.dimension[0], self.dimension[1], 4])

        """ The sparce matrix of the image of non-zero alpha's """
        self.Alpha = numpy.array([])

        """ The type of image """
        self.mode = self.image.mode

        """ Setting the opacity of the image to a full 100% , Opacity represents the transparency of the layer """
        self.Opacity = 100

        """ Obtaining the HSL matrix from the RGB matrix """
        for i in range(0, self.dimension[0]) :
            for k in range(0, self.dimension[1]) :
                self.hsl[i][k] = color.RGBtoHSL(self.rgb[i][k])



    """ To update the image in case the RGB matrix is modified """
    def Update_image(self) :
        self.image = Image.fromarray(self.rgb)


    """ To update the RGB matrix in case the HSL matrix is modified """
    def Update_RGB(self) :
        for i in range(0, self.dimension[0]) :
            for k in range(0, self.dimension[1]) :
                self.rgb[i][k] = color.HSLtoRGB(self.hsl[i][k])
        self.Update_image()


    """ To Update the hsl matrix in case the RGB matrix is modified """
    def Update_HSL(self) :
        for i in range(0, self.dimension[0]) :
            for k in range(0, self.dimension[1]) :
                self.hsl[i][k] = color.RGBtoHSL(self.rgb[i][k])
        self.Update_image()


    def __del__(self) :
        self.image.close()


    def display(self) :
        self.image.show()


    def show_rgb(self) :
        for i in self.rgb :
            print("\n\nrow\n")
            for k in i :
                print(k, end= " ")


    def show_hsl(self) :
        for i in self.hsl :
            print("\n\nrow\n")
            for k in i :
                print(k, end= " ")


