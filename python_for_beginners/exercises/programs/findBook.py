collectionOfBooks = ["The Lord of the Rings", "Game of Thrones", "Harry Potter"]

print("Enter the name of the book: \n")
bookToBeChecked = input()

for book in collectionOfBooks:
    if bookToBeChecked == book:
        print("The book is in the collection!")
        #the break statement is to stop the loop when the book is found
        break
#this else statement is related to the for loop.
#so if the book can't be found, the else will be trigered once only.
else:
    print("Could not find this book")