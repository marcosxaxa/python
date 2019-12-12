def helloWorld():
    print("Hello World")


def sumNumberts(num1, num2):
    sum = num1 + num2
    print("The sum of the numbers is {}".format(sum))


sumNumberts(5, 2)

helloWorld()
"""
to define a function the same rules of variable definition apply
we have to start with the word def followed by the name of the
function. Do not forget the parentesis e colon.
In the follow example, the function namesAndAge accepts two 
parameters which can be defined by other variables.
"""
def namesAndAge(name, age):
    print("Your name is {} and you are {} years old".format(name, age))


name = input("What is your name?\n")
age = input("How old are you?\n")
namesAndAge(name, age)

def triangleCalculation(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        return "This is a equilateral triangle"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "This is a Isosceles triangle"
    else:
        return "This is a Scalene triangle"

triangleCalculation(1, 2, 3)