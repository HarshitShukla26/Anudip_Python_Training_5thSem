def check_eligibility():

    roll=input("Enter Student Roll Number: ")
    company=input("Enter Company Name: ")

    student_found=False
    company_found=False

    student_cgpa=0

    try:

        file=open("students.txt","r")

        for line in file:

            data=line.strip().split(",")

            if data[0]==roll:

                student_found=True
                student_cgpa=float(data[3])

                break

        file.close()

        if not student_found:
            print("Student Not Found")
            return

        file=open("companies.txt","r")

        for line in file:

            data=line.strip().split(",")

            if data[0].lower()==company.lower():

                company_found=True

                required_cgpa=float(data[1])

                break

        file.close()

        if not company_found:
            print("Company Not Found")
            return

        print("\nStudent CGPA :",student_cgpa)
        print("Required CGPA :",required_cgpa)

        if student_cgpa>=required_cgpa:

            print("Eligible")

        else:

            print("Not Eligible")

    except FileNotFoundError:

        print("Required File Not Found")