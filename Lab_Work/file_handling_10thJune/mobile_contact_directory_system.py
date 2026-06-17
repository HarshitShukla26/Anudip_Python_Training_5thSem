import os

os.chdir(os.path.dirname(__file__))

FILE_NAME="contacts.txt"


def load_contacts():
    contacts=[]

    file=open(FILE_NAME, "r")

    for line in file:
        line=line.strip()

        if line!="":
            data=line.split(",")

            contacts.append([data[0], data[1]])

    file.close()

    return contacts


def save_contacts(contacts):
    file=open(FILE_NAME, "w")

    for contact in contacts:
        file.write(contact[0]+contact[1])

    file.close()


def display_contacts():
    contacts=load_contacts()

    print("All Contacts")

    for contact in contacts:
        print(contact[0],contact[1])


def search_contact():
    name=input("Enter Name : ")

    contacts=load_contacts()

    found=False

    for contact in contacts:
        if contact[0].lower()==name.lower():
            print("Contact Found")
            print("Name :",contact[0])
            print("Number :",contact[1])
            found=True

    if found == False:
        print("Contact Not Found")


def add_contact():
    name=input("Enter Name : ")
    number=input("Enter Number : ")

    contacts=load_contacts()

    contacts.append([name,number])

    save_contacts(contacts)

    print("Contact Added Successfully")


def update_contact():
    name=input("Enter Name : ")

    contacts=load_contacts()

    found=False

    for contact in contacts:
        if contact[0].lower()==name.lower():

            new_number=input("Enter New Number : ")

            contact[1]=new_number

            save_contacts(contacts)

            print("Contact Updated Successfully")

            found=True
            break

    if found==False:
        print("Contact Not Found")


def delete_contact():
    name=input("Enter Name : ")

    contacts=load_contacts()

    found=False

    for contact in contacts:

        if contact[0].lower()==name.lower():

            contacts.remove(contact)

            save_contacts(contacts)

            print("Contact Deleted Successfully")

            found=True
            break

    if found==False:
        print("Contact Not Found")


def vowel_contacts():
    contacts=load_contacts()

    print("Contacts Starting With Vowel")

    for contact in contacts:

        first_letter=contact[0][0].lower()

        if first_letter in "aeiou":
            print(contact[0],contact[1])


while True:

    print("===== Contact Management System =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowel")
    print("7. Exit")

    choice=input("Enter Choice : ")

    if choice=="1":
        display_contacts()

    elif choice=="2":
        search_contact()

    elif choice=="3":
        add_contact()

    elif choice=="4":
        update_contact()

    elif choice=="5":
        delete_contact()

    elif choice=="6":
        vowel_contacts()

    elif choice=="7":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")