def select_student():

    roll=input("Enter Student Roll Number: ")
    company=input("Enter Company Name: ")

    file=open("selected_students.txt","a")

    file.write(roll+","+company+"\n")

    file.close()

    print("Student Selected Successfully")

def view_selected_students():

    try:

        file=open("selected_students.txt","r")

        print("\nSELECTED STUDENTS")

        for line in file:
            print(line.strip())

        file.close()

    except FileNotFoundError:
        print("No Records Found")