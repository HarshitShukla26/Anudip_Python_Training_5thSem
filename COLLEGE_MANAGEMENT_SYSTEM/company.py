def add_company():

    cname=input("Enter Company Name: ")
    cgpa=input("Enter Minimum CGPA: ")
    skill=input("Enter Required Skill: ")
    package=input("Enter Package: ")

    file=open("companies.txt","a")

    file.write(cname+","+cgpa+","+skill+","+package+"\n")

    file.close()

    print("Company Added Successfully")


def view_companies():

    try:

        file=open("companies.txt","r")

        print("\nCOMPANY RECORDS")

        for line in file:
            print(line.strip())

        file.close()

    except FileNotFoundError:
        print("No Company Records Found")


def update_company():

    cname=input("Enter Company Name to Update: ")

    try:

        file=open("companies.txt","r")

        records=file.readlines()

        file.close()

        file=open("companies.txt","w")

        found=False

        for line in records:

            data=line.strip().split(",")

            if data[0].lower()==cname.lower():

                found=True

                cgpa=input("Enter New Minimum CGPA: ")
                skill=input("Enter New Skill: ")
                package=input("Enter New Package: ")

                newline=cname+","+cgpa+","+skill+","+package+"\n"

                file.write(newline)

            else:
                file.write(line)

        file.close()

        if found:
            print("Company Updated")
        else:
            print("Company Not Found")

    except FileNotFoundError:
        print("File Not Found")


def delete_company():

    cname=input("Enter Company Name to Delete: ")

    try:

        file=open("companies.txt","r")

        records=file.readlines()

        file.close()

        file=open("companies.txt","w")

        found=False

        for line in records:

            data=line.strip().split(",")

            if data[0].lower()==cname.lower():
                found=True

            else:
                file.write(line)

        file.close()

        if found:
            print("Company Deleted")
        else:
            print("Company Not Found")

    except FileNotFoundError:
        print("File Not Found")