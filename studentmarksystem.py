name = input("Enter your name:-")
marks = []

for i in range(5):
    m = int(input(f"Enter subject{i+1} marks:-"))
    marks.append(m)

total = sum(marks)
percentage = total / 5

print("Total:" , total)
print("Percentange:", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >=50:
    print("Grade C")
else:
    print("Fail")



with open("data.txt","r")as f:
    print(f.read())
 
with open("data.txt", "a") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Marks: {marks}\n")
    f.write(f"Total: {total}\n")
    f.write(f"Percentage: {percentage}\n")
   
    f.write("----------------------\n")

# 🔍 File read karo
with open("data.txt", "r") as f:
    print("\n📂 Saved Data:\n")
    print(f.read())