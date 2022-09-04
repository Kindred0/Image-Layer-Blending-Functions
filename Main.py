from Blend_Functions import addition
import Layer

Base_path = input("Enter the path of the Base Image\t: ")
Upper_path = input("Enter the path of the Upper Image\t: ")

Base = Layer.layer(Base_path)
Upper = Layer.layer(Upper_path)

Resultant = addition(Upper, Base)
print("The Resultant Image")
Resultant.show()