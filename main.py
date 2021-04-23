import genius
import area
import perimeter

print("Genius.py")
print("=========")
print("3 + 4 = " + str(genius.Add(4, 3)))
print("9 - 3 = " + str(genius.Substract(9, 3)))

print("area.py")
print("=======")
print("L'aire du carré de 4 cm de côté = " + str(area.SquareArea(4)))
print("L'aire du rectangle de longueur 7 cm et 4 cm de largeur = " + str(area.RectangleArea(7,4)))

print("L'aire du cercle ayant un rayon de 4 cm = " + str(area.CircleArea(4)))
print("L'aire du triangle ayant une base de 4 cm et une hauteur de 7 cm = " + str(area.TriangleArea(4,7)))

print("perimeter.py")
print("============")
print("Le périmètre du carré de 4 cm de côté = " + str(perimeter.SquarePerimeter(4)))
print("L'aire du rectangle de longueur 7 cm et 4 cm de largeur = " + str(perimeter.RectanglePerimeter(7,4)))
print("L'aire du cercle ayant un rayon de 4 cm = " + str(perimeter.CirclePerimeter(4)))
print("L'aire du triangle ayant pour côtés 14, 7 et 9 cm  = " + str(perimeter.TrianglePerimeter(14,7,9)))
