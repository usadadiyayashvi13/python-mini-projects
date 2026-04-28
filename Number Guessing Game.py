import random

number = random.randint(1,50)

print("Guess the number (1 to 50)")
print("You have 5 chance")

for i in range(5):
    guess = int(input("Enter your guess:-"))

    if guess == number:
        print("Your win 🎉")
        break

    elif guess > number:
        print("To high")

    else:
        print("To low")

else:
    print("You lost")
    print("Number was:", number)


    