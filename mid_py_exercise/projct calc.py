print("Welcome to riri's mini calculator💖")

while True : #keep running until you exit
    print("\nSelect operation")
    print("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. End ")


    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == "5":
        print("Exiting... Goodbye 👋")
        break #stops the loop
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Reslut:", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Error can't divide by zero ❌")
        else:
            print("Result:", num1/num2)
    else:
        print("Invalid choice")
        





    
