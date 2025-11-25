from Graphics.RectFunctions import RectArea
from Graphics.RectFunctions import RectPerimeter
from Graphics.CirFunctions import CirArea
from Graphics.CirFunctions import CirPerimeter
from Graphics.DGraphics.SphereFunctions import SpArea
from Graphics.DGraphics.SphereFunctions import SpPerimeter
from Graphics.DGraphics.CuboidFunctions import CubArea
from Graphics.DGraphics.CuboidFunctions import CubPerimeter

l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle Perimeter=",RectPerimeter(l,b))

r=int(input("enter radius of circle:"))
print("circle area=",CirArea(r))
print("circle perimeter=",CirPerimeter(r))

r=int(input("enter radius of sphere:"))
print("sphere area=",SpArea(r))
print("sphere volume=",SpPerimeter(r))

l=int(input("enter cuboid length:"))
b=int(input("enter cuboid breadth:"))
h=int(input("enter cuboid height:"))
print("cuboid area=",CubArea(l,b,h))
print("cuboid perimeter=",CubPerimeter(l,b,h))

