# total = 0

# while True:
#     expense = input("Enter expense amount (or type done to finish): ")

#     if expense.lower() == "done":
#         break

#     expense = int(expense)

#     total = total + expense

# print("Total spent:", total)

expenses = []
total = 0

budget = int(input("Enter your budget: "))

while True:
    print("\nExpense Tracker:")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. View summary")
    print("4. View Expense Stat")
    print("5. Exit")

    choice = input("Enter your choice: ")


    if choice == '1':
        expense_name = input("Enter the expense name: ")
        expense_amount = int(input("Enter the expense amount: "))
        expenses.append((expense_name, expense_amount))
        total += expense_amount
        print("Expense added successfully!")
    elif choice == '2':
        print("\nExpense History: ")

        for item in expenses:
            print("- ", item[0], ":", item[1])
    elif choice == '3':
        print("\nExpense Summary:")
        print(f"Total spent: ${total}")
        print(f"Remaining budget: ${budget - total}")

    elif choice == '4':
        if len(expenses) > 0:
            average = total / len(expenses)
            print("Average expense:", average)

            max_expense = max(expenses, key=lambda x: x[1])
            print("Highest expense:", max_expense[0], max_expense[1])
        else:
            print("No expenses recorded yet.")

    elif choice == '5':
        print("Exiting tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


            



