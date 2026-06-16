def add_student():

    roll=input("Enter Roll Number: ")
    name=input("Enter Name: ")
    branch=input("Enter Branch: ")
    cgpa=input("Enter CGPA: ")
    skill=input("Enter Skill: ")
    phone=input("Enter Phone Number: ")

    file=open("students.txt","a")

    file.write(roll+name+branch+cgpa+skill+phone)

    file.close()

    print("Student Added Successfully")


def view_students():

    try:
        file=open("students.txt","r")

        print("STUDENT RECORDS")

        for line in file:
            print(line.strip())

        file.close()

    except FileNotFoundError:
        print("No Records Found")


def update_student():

    roll=input("Enter Roll Number to Update: ")

    try:
        file=open("students.txt","r")

        records=file.readlines()

        file.close()

        file=open("students.txt","w")

        found=False

        for line in records:

            data=line.strip().split(",")

            if data[0]==roll:

                found=True

                name=input("Enter New Name: ")
                branch=input("Enter New Branch: ")
                cgpa=input("Enter New CGPA: ")
                skill=input("Enter New Skill: ")
                phone=input("Enter New Phone: ")

                newline=roll+","+name+","+branch+","+cgpa+","+skill+","+phone+""

                file.write(newline)

            else:
                file.write(line)

        file.close()

        if found:
            print("Record Updated")
        else:
            print("Student Not Found")

    except FileNotFoundError:
        print("File Not Found")


def delete_student():

    roll=input("Enter Roll Number to Delete: ")

    try:
        file=open("students.txt","r")

        records=file.readlines()

        file.close()

        file=open("students.txt","w")

        found=False

        for line in records:

            data=line.strip().split(",")

            if data[0]==roll:
                found=True

            else:
                file.write(line)

        file.close()

        if found:
            print("Record Deleted")
        else:
            print("Student Not Found")

    except FileNotFoundError:
        print("File Not Found")