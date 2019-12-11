"""
1 - read the names os the students
2 - Rank the top 3 students
3 - Reward students $500 to the first, $300 to the second, and $100 to the third
4 - Appreciate students who score 950 or above
"""

def readStudents():
    print("Enter the number of students: ")
    numberOfStudents = int(input())
    global studentNames, studentsMarks
    studentNames = []
    studentsMarks = []
    for student in range(0, numberOfStudents):
        print("Enter the name of the student: ")
        studentNames.append(input())
        print("Enter the mark: ")
        studentsMarks.append(int(input()))
    for i in range(0, numberOfStudents):
        print("The name of the student is {}, and the score is {}".format(studentNames[i], studentsMarks[i]))
        #print(studentNames)


def rankStudents(studentNames, studentsMarks):
    try:
        studentsMarks, studentNames = zip(*sorted(zip(studentsMarks, studentNames), reverse = True))
        print("{} has secured the highst score, {}".format(studentNames[0], studentsMarks[0]))
        print("{} has secured the second highst score, {}".format(studentNames[1], studentsMarks[1]))
        print("{} has secured the third highst score, {}".format(studentNames[2], studentsMarks[2]))
    except IndexError:
        print("Enter a minimum of 3 students")

def rewardStudents(studentNames, studentsMarks, reward):
    studentsMarks, studentNames = zip(*sorted(zip(studentsMarks, studentNames), reverse = True))
    print("{} has gained a money prize of ${}".format(studentNames[0], reward[0]))
    print("{} has gained a money prize of ${}".format(studentNames[1], reward[1]))
    print("{} has gained a money prize of ${}".format(studentNames[2], reward[2]))


def sortStudent(studentNames, studentsMarks):
    studentsMarks, studentNames = zip(*sorted(zip(studentsMarks, studentNames), reverse = True))
    return studentNames
    return studentsMarks


def appreciateStudent(studentNames, studentsMarks):
    studentsMarks, studentNames = zip(*sorted(zip(studentsMarks, studentNames), reverse = True))
    for record in studentsMarks:
        if record >= 950:
            indexMarks = studentsMarks.index(record)
            #print(indexMarks)
            print("Congratulations on scoring {} points, {}!".format(record, studentNames[indexMarks]))
    



readStudents()
rankStudents(studentNames, studentsMarks)
reward = (500, 300, 100)
rewardStudents(studentNames, studentsMarks, reward)
appreciateStudent(studentNames, studentsMarks)
