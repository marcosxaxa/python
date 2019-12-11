students = ["Marcos", "Brenna", "Gustavo"]
marks = [500, 980, 600]


if marks[0] > marks[1] and marks[0] > marks[2]:
    print("{} has the higher marks of all students which is {} and a reward of $500 will be provided".format(students[0], marks[0]))
    
elif marks[0] > marks[1] or marks[0] > marks[2]:
    print("{} has the second higher marks of all students which is {} and a reward of $300 will be provided".format(students[0], marks[0]))
elif marks[0] < marks[1] and marks[0] < marks[2]:
    print("{} has the thrid higher marks of all students which is {} and a reward of $100 will be provided".format(students[0], marks[0]))

if marks[1] > marks[0] and marks[1] > marks[2]:
    print("{} has the higher marks of all students which is {} and a reward of $500 will be provided".format(students[1], marks[1]))
elif marks[1] > marks[1] or marks[0] > marks[2]:
    print("{} has the second higher marks of all students which is {} and a reward of $300 will be provided".format(students[1], marks[1]))
elif marks[1] < marks[1] and marks[0] < marks[2]:
    print("{} has the thrid higher marks of all students which is {} and a reward of $100 will be provided".format(students[1], marks[1]))

if marks[2] > marks[0] and marks[2] > marks[1]:
    print("{} has the higher marks of all students which is {} and a reward of $500 will be provided".format(students[2], marks[2]))
elif marks[2] > marks[0] or marks[2] > marks[1]:
    print("{} has the second higher marks of all students which is {} and a reward of $300 will be provided".format(students[2], marks[2]))
elif marks[2] < marks[1] and marks[2] < marks[0]:
    print("{} has the thrid higher marks of all students which is {} and a reward of $300 will be provided".format(students[2], marks[2])) 