for number in range(1, 11):
    print(number)

oddSum = 0

for num in range(1, 11):
    if num % 2 is not 0:
        oddSum = oddSum + num

print(oddSum)
