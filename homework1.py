# Question 1:
# Create a calculator using functions that asks for two numbers and performs a calculation
# that the user inputs... Loop until the user chooses not to perform any more calculations.

while True:
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Enter q or Q to Exit")
    user_choice = input("Enter Your Choice : ")
    if user_choice == "q" or user_choice == "Q":
        break
    num1 = float(input("Enter Your First Number : "))
    num2 = float(input("Enter Your Second Number : "))
    if user_choice == "1":
        print(num1, "+", num2, "=", (num1+num2))
    elif user_choice == "2":
        print(num1, "-", num2, "=", (num1-num2))
    elif user_choice == "3":
        print(num1, "*", num2, "=", (num1*num2))
    elif user_choice == "4":
        if num2 == 0.0:
            print("DIVISION '0' ERROR!")
        else:
            print(num1, "/", num2, "=", (num1/num2))
    else:
        print("INVALID CHOICE!")


