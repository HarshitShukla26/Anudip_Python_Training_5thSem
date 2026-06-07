#Program for library book availability
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

#TASK 1: Books currently unavailable
print("Unavailable Books:")
for book in books:
    if books[book]==0:
        print(book)

#TASK 2: Count available books
count=0
for book in books:
    if books[book]>0:
        count+=1

print("Number of available books",count)

#TASK 3: Find book with maximum copies
for book in books:
    max_book=book
    max_copies=books[book]
    break

for book in books:
    if books[book]>max_copies:
        max_copies=books[book]
        max_book=book

print("Book with maximum copies",max_book)

#TASK 4: Create a list of books having less than 3 copies
less_than_3=[]

for book in books:
    if books[book]<3:
        less_than_3.append(book)

print("Books having less than 3 copies:")
print(less_than_3)

#TASK 5: Total number of books available
total=0
for book in books:
    total+=books[book]

print("Total number of books available",total)