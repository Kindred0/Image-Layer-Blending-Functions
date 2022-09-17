
import Color_converter as cc
from PIL import Image
import numpy


class layer :

    def __init__(self, path = None, width = 1 , height = 1) :

        # Inititally the image will have 100% opacity

        self.Opacity = 100

        if path != None :

            # The Actual Image

            self.image = Image.open(path)

            #The Matrix if the image in RGBA format

            self.rgb = numpy.asarray(self.image)

            # To change the reading mode from read only to read and write

            self.rgb = self.rgb.copy()
            self.rgb.setflags(write = 1)

            # Dimesion of the image

            self.dimension = self.image.size
            self.dimension = (self.dimension[1], self.dimension[0])

            # The Matrix of the image in HSL format, Currently Unassigned to save space

            self.hsl = numpy.array([])

            # The Matrix containing the alpha values according to the opacity of the image.

            self.Alpha = numpy.zeros([self.dimension[0], self.dimension[1]])

            # The reading mode of the image

            self.mode = self.image.mode

            self.sparce = []

            # Constructing the Alpha matrices

            for i in range(0, self.dimension[0]) :
                for k in range(0, self.dimension[1]) :
                    if self.mode == 'RGBA' :
                        self.Alpha[i][k] = self.rgb[i][k][3]

                        if self.rgb[i][k][3] != 0 :
                            self.sparce.append((i, k))
                        

                    elif self.mode == 'RGB' or self.mode == 'L' :

                        self.Alpha[i][k] = 255



        else :

            self.rgb = numpy.zeros([width, height, 4])

            self.image = None

            self.dimension = (width, height)

            self.Alpha = numpy.zeros([width, height])

            self.mode = "RGBA"  

    # To set the opacity of the image and also change the alpha values of the Alpha Matrix accordingly

    def Set_Opacity(self, opacity) :
        self.Opacity = opacity

        if self.Opacity > 100 :
             self.Opacity = 100
        elif self.Opacity < 0 :
            self.Opacity = 0


        
        for i in range(0, self.dimension[0]) :
            for k in range(0, self.dimension[1]) :
                if self.mode == 'RGBA' :
                    self.Alpha[i][k] = self.rgb[i][k][3] * (self.Opacity / 100)
                    self.Alpha[i][k] = int(self.Alpha[i][k])

                elif self.mode == 'RGB' or 'L' :
                    self.Alpha[i][k] = 255 * (self.Opacity / 100)
                    self.Alpha[i][k] = int(self.Alpha[i][k])


    # To construct the RGBA Matrix in case the 

    def Update_image(self) :
        self.image = Image.fromarray(self.rgb)


    def Construct_HSL(self) :
        self.hsl = []
        temp = []
        for i in range(0, self.dimension[0]) :
            for k in range(0, self.dimension[1]) :
                temp.append(cc.RGBtoHSL(self.rgb[i][k]))
            self.hsl.append(temp)
            temp = []
        self.hsl = numpy.ndarray(self.hsl)



    # To Construct the Sparce Matrix 

    def Construct_sparce(self) :
        self.sparce = []
        for i in range(0, self.dimension[0]) :
            for k in range(0, self.dimension[1]) :
                if self.Alpha[i][k] != 0 :
                    self.sparce.append((i , k))





    # Display Image

    def display(self) :
        self.image.show()


    # Display RGB Matrix 

    def show_rgb(self) :
        for i in self.rgb :
            print("\n\nrow\n")
            for k in i :
                print(k, end= " ")


    #Display HSL Matrix 

    def show_hsl(self) :
        self.Construct_HSL()
        for i in self.hsl :
            print("\n\nrow\n")
            for k in i :
                print(k, end= " ")


