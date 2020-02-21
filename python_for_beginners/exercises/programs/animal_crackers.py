def animal_crackers(text):
    animals = []
    for item in text.split():
        animals.append(item[0])
    if animals[0] == animals[1]:
        print('True')
    else:
        print('False')
  

animal_crackers('Crazy Cow')

