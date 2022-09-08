


from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import Layer 
import Blend_Functions as Bf




#Functions used in GUI



def Error():
   top = Toplevel(root)
   top.geometry("250x50")
   top.title("Error")
   Label(top, text = "No Base Layer Selected!").place(x = 50, y = 15)

def select_Base() :
    types = (("PNG Files", "*.png"), ("JPG Files", "*.jpg"))
    path = askopenfilename(
        title = 'Open a file',
        initialdir = '/',
        filetypes = types)

    showinfo( title = 'Selected File', message = path)

    global BaseImage
    BaseImage = Layer.layer(path)
    img = (Image.open(path)).resize((170, 170))
    img = ImageTk.PhotoImage(img)
    global Blabel
    if Blabel != None :
        Blabel.destroy()
    Blabel = Label(Basecanvas, image = img)
    Blabel.image = img
    Blabel.pack(anchor = 'center')

def select_Second() :
    types = (("PNG Files", "*.png"), ("JPG Files", "*.jpg"))
    path = askopenfilename(
        title = 'Open a file',
        initialdir = '/',
        filetypes = types)

    showinfo( title = 'Selected File', message = path)

    global SecondImage 
    SecondImage =  Layer.layer(path)
    img = (Image.open(path)).resize((170, 170))
    img = ImageTk.PhotoImage(img)
    global Slabel
    if Slabel != None :
        Slabel.destroy()
    Slabel = Label(Secondcanvas, image = img)
    Slabel.image = img
    Slabel.pack(anchor = 'center')


def select_Upper() :
    types = (("PNG Files", "*.png"), ("JPG Files", "*.jpg"))
    path = askopenfilename(
        title = 'Open a file',
        initialdir = '/',
        filetypes = types)

    showinfo( title = 'Selected File', message = path)

    global UpperImage 
    UpperImage = Layer.layer(path)
    img = (Image.open(path)).resize((170, 170))
    img = ImageTk.PhotoImage(img)
    global Ulabel
    if Ulabel != None :
        Ulabel.destroy()
    Ulabel = Label(Uppercanvas, image = img)
    Ulabel.image = img
    Ulabel.pack(anchor = 'center')

def Save_image() :
    print("Still not coded yer thank you")


def temp() :
    tip = Toplevel(root)
    tip.geometry("250x100")
    tip.title("Info")
    info = "Second Layer\t: \nOpacity\t: {}\nlock\t: {}\nMode\t: {}"

    Label(tip, text = info.format(OpacityS.get(), lockS.get(), ModeS.get())).place(x = 50, y = 15)


def blend() :
    if BaseImage == None :
        Error()
        return
    
    #Blending Base Layer with Second Layer

    if ModeS.get() == "Normal" :

        Resultant = Bf.normal(SecondImage, BaseImage)
    
    elif ModeS.get() == "Addition" :
        
        Resultant = Bf.addition(SecondImage, BaseImage)

    elif ModeS.get() == "Subtraction" :
        
        Resultant = Bf.subtraction(SecondImage, BaseImage)

    else :
        Resultant = Bf.addition(SecondImage, BaseImage)

    
    #Blending the Resultant Layer with the Upper Layer

    if ModeU.get() == "Normal" :

        Resultant = Bf.normal(UpperImage, Resultant)

    elif ModeU.get() == "Addition" :

        Resultant = Bf.addition(UpperImage, Resultant)

    elif ModeU.get() == "Subtraction" :

        Resultant = Bf.subtraction(SecondImage, BaseImage)

    else :

        Resultant = Bf.addition(UpperImage, Resultant)


    #Setting the Resultant image in the GUI


    img = Resultant.image.resize((700, 700))
    img = ImageTk.PhotoImage(img)
    global Mlabel
    if Mlabel != None :
        Mlabel.destroy()
    Mlabel = Label(Maincanvas, image = img)
    Mlabel.image = img
    Mlabel.place(x = 150, y = 0)

BaseImage = None
UpperImage = None
SecondImage = None




Slabel = None
Blabel = None
Ulabel = None
Mlabel = None




#GUI Design Codes 




#Setting the Window  
root = Tk()

root.title("Blending Modes")
root.geometry('1265x765')

root.configure(bg = "#1f1f1f")

#Setting the Base layer and its options
Baselayer = Frame(root, height = 250, width = 250, bg = "#2e2e2e")
Baselayer.place(x = 5, y = 505)

#Setting the Second layer and its options
Secondlayer = Frame(root, height = 250, width = 250, bg = "#2e2e2e")
Secondlayer.place(x = 5, y = 255)

#Setting the Upper layer and its option
Upperlayer = Frame(root, height = 250, width = 250 , bg = "#2e2e2e")
Upperlayer.place(x = 5, y = 5)

#Setting up all the menus in each frame

Basemenu = Frame(Baselayer, height = 80, width = 250, bg = "#a0a0a0")
Basemenu.pack(side = 'top')

Secondmenu = Frame(Secondlayer, height = 80, width = 250, bg = "#a0a0a0")
Secondmenu.pack(side = 'top')

Uppermenu = Frame(Upperlayer, height = 80, width = 250, bg = "#a0a0a0")
Uppermenu.pack(side = 'top')

#Setting up all the canvas in each frame
Basecanvas = Frame(Baselayer, height = 170 , width = 250 , bg = "#2e2e2e")
Basecanvas.pack(side = 'bottom')

Secondcanvas = Frame(Secondlayer, height = 170 , width = 250 , bg = "#2e2e2e")
Secondcanvas.pack(side = 'bottom')

Uppercanvas = Frame(Upperlayer, height = 170 , width = 250 , bg = "#2e2e2e")
Uppercanvas.pack(side = 'bottom')

Mainmenu = Frame(root, height = 45, width = 1000, bg = "#c0c0c0")
Mainmenu.place(x = 260 , y = 5)

Maincanvas = Frame(root, height = 700, width = 1000, bg = "#5f5f5f")
Maincanvas.place(x = 260, y = 55)
#Setting alpha locks for Base layer and Upper layer
lockB = BooleanVar()
lockS = BooleanVar()


#Assigning the locks to its frames/layers
alphalockS = Checkbutton(Secondlayer, text = "Alpha", variable = lockS, onvalue = 1, offvalue = 0, height = 1, width = 10, background = "#a0a0a0" , activebackground = "#a0a0a0")
alphalockS.place(x = 170, y = 6)

alphalockB = Checkbutton(Basemenu, text = "Alpha", variable = lockB, onvalue = 1, offvalue = 0, height = 1, width = 10, background = "#a0a0a0", activebackground = "#a0a0a0")
alphalockB.place(x = 170, y = 6)

#Setting the Opacity Slider for all layers
OpacityB = IntVar()
OpacityU = IntVar()
OpacityS = IntVar()

OpacityB.set(100)
OpacityS.set(100)
OpacityU.set(100)

#Assigning the sliders to its frames/layers
ScaleB = Scale(Basemenu, variable = OpacityB, from_ = 0, to = 100, orient = HORIZONTAL, length = 235, background = "#a0a0a0", bd = 0)
ScaleB.place(x = 5, y = 40)

ScaleS = Scale(Secondmenu, variable = OpacityS, from_ = 0, to = 100, orient = HORIZONTAL, length = 235, background = "#a0a0a0", bd = 0)
ScaleS.place(x = 5, y = 40)

ScaleU = Scale(Uppermenu, variable = OpacityU, from_ = 0, to = 100, orient = HORIZONTAL, length = 235, background = "#a0a0a0", bd = 0)
ScaleU.place(x = 5, y = 40)


#Setting up the dropbox for Upper and Second layers

ModeU = StringVar()
ModeS = StringVar()

#Assigning the dropboxes to frames/layers

option = ["Normal", "Addition", "Subtraction", "Multiply", "Devide", "Overlay", "Screen", "Soft Light", "Hard Light", "Hues", "Saturation", "Luminosity", "Darken", "Lighten"]
ModeU.set("Normal")
ModeS.set("Normal")

BlendU = OptionMenu(Uppermenu, ModeU, *option,)
BlendU.place(x = 5, y = 5)

BlendS = OptionMenu(Secondmenu, ModeS, *option)
BlendS.place(x = 5, y = 5)


#Setting Open Button in each layer to open an image

OpenS = Button(Secondmenu, text = "Open", command = select_Second)
OpenU = Button(Uppermenu, text = "Open", command = select_Upper)
OpenB = Button(Basemenu, text = "Open", command = select_Base)

OpenS.place(x = 130, y = 7)
OpenU.place(x = 130, y = 7)
OpenB.place(x = 130, y = 7)


Combine = Button(Mainmenu, text = "Blend", command = blend)
Combine.place(x = 900, y = 10)

Save = Button(Mainmenu, text = "Save", command = Save_image)
Save.place(x = 950, y = 10)
root.mainloop()