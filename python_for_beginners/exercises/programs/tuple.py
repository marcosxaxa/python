birthdays = (1991, 1995, 2017, 2018)
print(birthdays)

birthdays_list = list(birthdays)
print(birthdays_list)

del(birthdays_list[0])
birthdays = tuple(birthdays_list)
print(birthdays)