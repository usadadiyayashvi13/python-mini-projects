
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def divi(a,b):
    return a / b

def main():
    print("------simple calcultor------")
   

    num1 = int(input("Enter your number:-"))
    num2 = int(input("Enter your number:-"))

    op =input("Please choose an operation (+,-,*,/):")
      
    if op == "+":
       print("Result", add(num1,num2))
    elif op == "-":
        print("Result", sub(num1,num2))
    elif op == "*": 
        print("Result", mul(num1,num2))
    elif op == "/": 
        print("Result", divi(num1,num2))
   
main()   



