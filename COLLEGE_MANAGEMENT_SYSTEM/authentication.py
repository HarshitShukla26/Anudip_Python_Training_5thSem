def login():

    username=input("Enter Username: ")
    password=input("Enter Password: ")

    try:

        file=open("admin.txt","r")

        for line in file:

            data=line.strip().split(",")

            if username==data[0] and password==data[1]:

                file.close()

                print("Login Successful")
                return True

        file.close()

        print("Invalid Username or Password")
        return False

    except FileNotFoundError:

        print("admin.txt not found")
        return False