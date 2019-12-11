user1 = int(input("Type a number: \n"))
user2 = int(input("Type a number: \n"))

def findGreaterNumber(num1, num2):
    if num1 > num2:
        print('The number of the first user is greater')
    elif num1 == num2:
        print('The numbers are equal!')
    else:
        print('The number of the second user is greater')

findGreaterNumber(user1, user2)