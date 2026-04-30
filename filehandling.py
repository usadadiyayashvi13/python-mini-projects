# print("1. Add note")
# print("2. view note")

# choice = int(input("Enter choice:-"))

# if choice == 1:
#     note=(input("Enter note"))
#     with open("note.txt", "a")as f:
#         f.write(note + "\n")

# elif choice == 2:
#     with open("note.txt", "r")as f:
#         print(f.read())    
# else:
#     print("not found")



# import os

# file_name = "user.txt"

# if not os.path.exists(file_name):
#     open(file_name,"w").close()

# # singup function
# def singup():
#     print("/n------singup-------")
#     username = input("enter your name:-")
#     password = input("enter your password:-")

# # check if user already exits
#     with open(file_name,"r")as f:
#         for line in f:
#             u,p =line.strip().split(",")
#             if u == username:
#                 print("User name already exists!")
#                 return
#     with open(file_name,"a")as f:
#         f.write(username +","+ password + "\n")
#         print("Singup Successful!")

# # login

# def login():
#     print("/n------Login------")
#     username = input("enter your name:-")
#     password = input("enter your password:-")

#     with open(file_name,"r")as f:
#         for line in f:
#              u,p =line.strip().split(",")
#              if u == username and p == password:
#                     print("Login Successful")
#                     return
#     print("Invalid username and password")

# def main():

#     print("=====Login System=====")
#     print("1. Singup")
#     print("2. Login")
#     print("3. Exit")

#     choice = input("Enter choice:-")

#     if choice == "1":
#         singup()
#     elif choice == "2":
#         login()
#     elif choice == "3":
#         print("Good byee")
#     else:
#         print("Invalid choice")
# main()

    
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("1. Add")
    print("2. Divide")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a / b)

    else:
        print("Invalid choice")

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program finished")