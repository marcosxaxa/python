ages = {"Marcos": 28, "Brenna": 24, "Marvin": 2, "Gustsavo": 1}
print(ages)

ages["Brenna"] = 25
print(ages)

copy_of_ages = ages.copy()
ages.clear()
print(ages)
print("Break")
print(copy_of_ages)