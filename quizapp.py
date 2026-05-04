question ={
    "Who created Python?" : "guido van rossum",
    "Python kis type ki programming language hai?" : "high-level",
    "What is Variable?" : "variable ek container hota hai jo data store karta hai.",
    "How many operations in Python?" : "7",
    "Python me kitne main types ke loops hote hain?" : "2 type"
}

score = 0
for q, ans in question.items():
    user =input(q).lower()

    if user == ans:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Your score:", score)        
