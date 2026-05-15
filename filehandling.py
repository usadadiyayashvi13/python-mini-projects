import os

file_name = "user.txt"

if not os.path.exists(file_name):
    open(file_name,"w").close()

# singup function
def singup():
    print("/n------singup-------")
    username = input("enter your name:-")
    password = input("enter your password:-")

# check if user already exits
    with open(file_name,"r")as f:
        for line in f:
            u,p =line.strip().split(",")
            if u == username:
                print("User name already exists!")
                return
    with open(file_name,"a")as f:
        f.write(username +","+ password + "\n")
        print("Singup Successful!")

# login function

def login():
    print("/n------Login------")
    username = input("enter your name:-")
    password = input("enter your password:-")

    with open(file_name,"r")as f:
        for line in f:
             u,p =line.strip().split(",")
             if u == username and p == password:
                    print("Login Successful")
                    return
    print("Invalid username and password")

def main():

    print("=====Login System=====")
    print("1. Singup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice:-")

    if choice == "1":
        singup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Good byee")
    else:           
        print("Invalid choice")
main()
