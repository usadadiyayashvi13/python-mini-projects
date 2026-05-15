print("1. Add note")
print("2. view note")

choice = int(input("Enter choice:-"))

if choice == 1:
    note=(input("Enter note"))
    with open("note.txt", "a")as f:
        f.write(note + "\n")

elif choice == 2:
    with open("note.txt", "r")as f:
        print(f.read())    
else:
    print("not found")

