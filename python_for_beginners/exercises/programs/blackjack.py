def black_jack(a,b,c):
    if a+b+c <= 21:
        print(a+b+c)
    elif (a+b+c > 21) and (a == 11 or b == 11 or c == 11):
        result = (a+b+c) - 10
        if result <= 21:
            print(result)
        else:
            print('BUST')
    else:
        print('BUST')

black_jack(9,9,11)

        