def apply_job():

    roll=input("Enter Student Roll Number: ")
    company=input("Enter Company Name: ")

    file=open("applications.txt","a")

    file.write(roll+","+company+",Applied\n")

    file.close()

    print("Application Submitted Successfully")

def view_applications():

    try:

        file=open("applications.txt","r")

        print("\nAPPLICATION RECORDS")

        for line in file:
            print(line.strip())

        file.close()

    except FileNotFoundError:
        print("No Applications Found")

def search_application():

    roll=input("Enter Roll Number: ")

    found=False

    try:

        file=open("applications.txt","r")

        for line in file:

            data=line.strip().split(",")

            if data[0]==roll:

                print(line.strip())

                found=True

        file.close()

        if not found:
            print("Application Not Found")

    except FileNotFoundError:
        print("File Not Found")

