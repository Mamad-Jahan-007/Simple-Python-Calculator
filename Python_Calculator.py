# A simple calculator --- Python
def Menu():
    print("--- Simpel calculator ---")
    print("--- Menu ---")
    print("--- 1. Add (+)")
    print("--- 2. Minus (-)")
    print("--- 3. Multiply (*)")
    print("--- 4. Divide (/)")
    print("--- 5. Remainder of division (%)")
    print("--- 0. Exit")

def Add():
    Number_1 = float(input("The number 1: "))
    Number_2 = float(input("The number 2: "))
    print("Answer: ",Number_1 + Number_2)
    
def Minus():
    Number_1 = float(input("The number 1: "))
    Number_2 = float(input("The number 2: "))
    print("Answer: ",Number_1 - Number_2)
    
def Multiply():
    Number_1 = float(input("The number 1: "))
    Number_2 = float(input("The number 2: "))
    print("Answer: ",Number_1 * Number_2)

def Divide():
    Number_1 = float(input("The number 1: "))
    Number_2 = float(input("The number 2: "))
    try:
        print("Answer: ",Number_1 / Number_2)
    except ZeroDivisionError:
        print("Error: The Number 2 is ZERO!")
        
def R_O_Division():
    Number_1 = float(input("The number 1: "))
    Number_2 = float(input("The number 2: "))
    try:
        print("Answer: ",Number_1 % Number_2)
    except ZeroDivisionError:
        print("Error: The Number 2 is ZERO!")
# The main program    
while True:
    Menu()
    User_Choice = str(input("Enter the number you want: "))
    if User_Choice == "0":
        print("Good lock!")
        break
    elif User_Choice == "1":
        Add()
    elif User_Choice == "2":
        Minus()
    elif User_Choice == "3":
        Multiply()
    elif User_Choice == "4":   
        Divide()
    elif User_Choice == "5":   
        R_O_Division()
    else:
        print("<<< Enter a specific number >>>")
















