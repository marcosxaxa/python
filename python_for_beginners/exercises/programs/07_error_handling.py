def ask():
    while True:
        try:
            number = int(input("Please, provide a number: \n"))
            result = number*number
        except:
            print("This is not a valid number")
            continue
        else:
            print("The number6 square is {}".format(result))
            break



ask()
