def search_student():

    roll=input("Enter Roll Number: ")

    found=False

    try:

        file=open("students.txt","r")

        for line in file:

            data=line.strip().split(",")

            if data[0]==roll:

                print(line.strip())

                found=True

        file.close()

        if not found:
            print("Student Not Found")

    except FileNotFoundError:
        print("File Not Found")

def search_company():

    cname=input("Enter Company Name: ")

    found=False

    try:

        file=open("companies.txt","r")

        for line in file:

            data=line.strip().split(",")

            if data[0].lower()==cname.lower():

                print(line.strip())

                found=True

        file.close()

        if not found:
            print("Company Not Found")

    except FileNotFoundError:
        print("File Not Found")