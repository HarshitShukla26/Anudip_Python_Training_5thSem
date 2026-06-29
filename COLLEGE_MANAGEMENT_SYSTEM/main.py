from authentication import *
from student import *
from company import *
from eligibility import *
from application import *
from search import *
from selection import *
from report import *
from backup import *

if login():

    while True:

        print("------- PLACEMENT MANAGEMENT SYSTEM -------")

        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")

        print("5. Add Company")
        print("6. View Companies")
        print("7. Update Company")
        print("8. Delete Company")

        print("9. Check Eligibility")

        print("10. Apply For Job")
        print("11. View Applications")

        print("12. Search Student")
        print("13. Search Company")

        print("14. Select Student")
        print("15. View Selected Students")

        print("16. Placement Report")

        print("17. Backup Students")
        print("18. Backup Companies")
        print("19. Backup Applications")

        print("20. Exit")

        choice=int(input("Enter Choice: "))

        if choice==1:
            add_student()

        elif choice==2:
            view_students()

        elif choice==3:
            update_student()

        elif choice==4:
            delete_student()

        elif choice==5:
            add_company()

        elif choice==6:
            view_companies()

        elif choice==7:
            update_company()

        elif choice==8:
            delete_company()

        elif choice==9:
            check_eligibility()

        elif choice==10:
            apply_job()

        elif choice==11:
            view_applications()

        elif choice==12:
            search_student()

        elif choice==13:
            search_company()

        elif choice==14:
            select_student()

        elif choice==15:
            view_selected_students()

        elif choice==16:
            placement_report()

        elif choice==17:
            backup_students()

        elif choice==18:
            backup_companies()

        elif choice==19:
            backup_applications()

        elif choice==20:
            print("Thank You")
            break

        else:
            print("Invalid Choice")