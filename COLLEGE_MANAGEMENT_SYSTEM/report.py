def placement_report():

    try:

        student_file=open("students.txt","r")
        students=student_file.readlines()
        student_file.close()

        company_file=open("companies.txt","r")
        companies=company_file.readlines()
        company_file.close()

        application_file=open("applications.txt","r")
        applications=application_file.readlines()
        application_file.close()

        selected_file=open("selected_students.txt","r")
        selected=selected_file.readlines()
        selected_file.close()

        print("\nPLACEMENT REPORT")

        print("Total Students :",len(students))
        print("Total Companies :",len(companies))
        print("Total Applications :",len(applications))
        print("Selected Students :",len(selected))

        if len(students)>0:

            percentage=(len(selected)/len(students))*100

            print("Placement Percentage :",percentage)

    except FileNotFoundError:

        print("Required File Not Found")