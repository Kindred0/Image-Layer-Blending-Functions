import Blend_Functions as BF
import Layer
import Color_converter as convert

Base_path = input("Enter the path of the Base Image\t: ")
Upper_path = input("Enter the path of the Upper Image\t: ")

Base = Layer.layer(Base_path)
Upper = Layer.layer(Upper_path)

Resultant = BF.addition(Upper, Base)
print("The Resultant Image")
Resultant.display()

Resultant = BF.subtraction(Upper, Base)
print("The Resultant Image")
Resultant.display()
