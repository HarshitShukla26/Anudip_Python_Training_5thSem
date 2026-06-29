def backup_students():

    try:

        source=open("students.txt","r")
        data=source.read()
        source.close()

        target=open("students_backup.txt","w")
        target.write(data)
        target.close()

        print("Student Backup Created")

    except FileNotFoundError:

        print("students.txt not found")

def backup_companies():

    try:

        source=open("companies.txt","r")
        data=source.read()
        source.close()

        target=open("companies_backup.txt","w")
        target.write(data)
        target.close()

        print("Company Backup Created")

    except FileNotFoundError:

        print("companies.txt not found")

def backup_applications():

    try:

        source=open("applications.txt","r")
        data=source.read()
        source.close()

        target=open("applications_backup.txt","w")
        target.write(data)
        target.close()

        print("Application Backup Created")

    except FileNotFoundError:

        print("applications.txt not found")