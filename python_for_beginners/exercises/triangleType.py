def triangleCalculation(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        print("This is a Equilateral triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("This is a Isosceles triangle")
    else:
        print("This is a Scalene triangle")



triangleCalculation(3, 3, 3)