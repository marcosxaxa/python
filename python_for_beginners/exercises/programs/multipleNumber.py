userNumber = int(input("Type a number.\n"))

if userNumber % 3 is 0:
    print("Number is a multiple of 3")
    if userNumber % 7 is 0:
        print("Number is also a multiple of 7")
    else:
        print("Number is a multiple of 3, by not a multiple of 7")
else:
    print("Number is neither multiple of 3 or 7")

