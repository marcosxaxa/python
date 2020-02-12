number1 = int(input("Type the first number: \n"))
number2 = int(input("Type the first number: \n"))
operation = input("What do you want to do? 1 - subtract 2 - sum 3 - division 4 - mutiply ")

if (operation == "1"):
    result = number1 - number2
    print("The result of the subtraction of {} and {} is {}".format(number1, number2, result))



