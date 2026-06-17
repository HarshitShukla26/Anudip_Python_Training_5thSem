# Library Management System
import os

os.chdir(os.path.dirname(__file__))
FILE_NAME ="books.txt"


def load_books():
    books = []

    file = open(FILE_NAME, "r")

    for line in file:
        line = line.strip()

        if line != "":
            data = line.split(",")

            books.append([data[0], data[1], int(data[2])])

    file.close()

    return books


def save_books(books):
    file = open(FILE_NAME, "w")

    for book in books:
        file.write(book[0] + "," + book[1] + "," + str(book[2]) + "\n")

    file.close()


while True:

    print("\n1. Display Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Unavailable Books")
    print("6. Restocking Books")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        books = load_books()

        for book in books:
            print(book[0], book[1], book[2])

    elif choice == "2":

        bid = input("Enter Book ID: ")

        books = load_books()

        found = False

        for book in books:
            if book[0] == bid:
                print(book[0], book[1], book[2])
                found = True

        if found == False:
            print("Book Not Found")

    elif choice == "3":

        bid = input("Enter Book ID: ")

        books = load_books()

        for book in books:
            if book[0] == bid:

                if book[2] > 0:
                    book[2] = book[2] - 1
                    save_books(books)
                    print("Book Issued")
                else:
                    print("Book Not Available")

    elif choice == "4":

        bid = input("Enter Book ID: ")

        books = load_books()

        for book in books:
            if book[0] == bid:
                book[2] = book[2] + 1
                save_books(books)
                print("Book Returned")

    elif choice == "5":

        books = load_books()

        for book in books:
            if book[2] == 0:
                print(book[0], book[1])

    elif choice == "6":

        books = load_books()

        for book in books:
            if book[2] < 2:
                print(book[0], book[1], book[2])

    elif choice == "7":
        break

    else:
        print("Invalid Choice")