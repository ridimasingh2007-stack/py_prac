import math

print("Welcome to Riri's Scientific Calculator 🧮")

def get_number(prompt):
    """Get a valid number from user with error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Error: Please enter a valid number!")

def safe_math_operation(operation, *args):
    """Safely perform math operations with error handling"""
    try:
        return operation(*args)
    except ValueError as e:
        return f"❌ Math Error: {str(e)}"
    except ZeroDivisionError:
        return "❌ Error: Cannot divide by zero!"
    except OverflowError:
        return "❌ Error: Result too large!"
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"

while True:
    print("\n" + "="*50)
    print("🔢 Select operation:")
    print("1. ➕ Add")
    print("2. ➖ Subtract") 
    print("3. ✖️  Multiply")
    print("4. ➗ Divide")
    print("5. ² Square")
    print("6. √ Square Root")
    print("7. ^ Power")
    print("8. 📐 Sin")
    print("9. 📐 Cos")
    print("10. 📐 Tan")
    print("11. 📊 Log10")
    print("12. 📊 Natural log (ln)")
    print("13. 🔄 Factorial")
    print("14. 📏 Absolute Value")
    print("q. ❌ Quit")
    print("="*50)

    choice = input("Enter choice: ").strip().lower()

    if choice == 'q':
        print("👋 Exiting... Thank you for using Riri's Calculator!")
        break

    # Two-operand operations
    if choice in ['1', '2', '3', '4', '7']:
        print(f"\n🔢 You selected: {['', 'Addition', 'Subtraction', 'Multiplication', 'Division', '', '', 'Power'][int(choice)]}")
        
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = num1 + num2
            print(f"✅ Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"✅ Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"✅ Result: {num1} × {num2} = {result}")
        elif choice == '4':
            result = safe_math_operation(lambda x, y: x / y, num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"✅ Result: {num1} ÷ {num2} = {result}")
        elif choice == '7':
            result = safe_math_operation(math.pow, num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"✅ Result: {num1} ^ {num2} = {result}")

    # Single-operand operations
    elif choice in ['5', '6', '8', '9', '10', '11', '12', '13', '14']:
        operations = {
            '5': ('Square', lambda x: x ** 2),
            '6': ('Square Root', lambda x: math.sqrt(x) if x >= 0 else None),
            '8': ('Sin', lambda x: math.sin(math.radians(x))),
            '9': ('Cos', lambda x: math.cos(math.radians(x))),
            '10': ('Tan', lambda x: math.tan(math.radians(x))),
            '11': ('Log10', lambda x: math.log10(x) if x > 0 else None),
            '12': ('Natural Log', lambda x: math.log(x) if x > 0 else None),
            '13': ('Factorial', lambda x: math.factorial(int(x)) if x >= 0 and x == int(x) else None),
            '14': ('Absolute Value', lambda x: abs(x))
        }
        
        operation_name, operation_func = operations[choice]
        print(f"\n🔢 You selected: {operation_name}")
        
        num = get_number("Enter number: ")
        
        # Special validation for specific operations
        if choice == '6' and num < 0:
            print("❌ Error: Cannot calculate square root of negative number!")
        elif choice in ['11', '12'] and num <= 0:
            print("❌ Error: Logarithm requires positive numbers!")
        elif choice == '13' and (num < 0 or num != int(num)):
            print("❌ Error: Factorial requires non-negative integers!")
        else:
            result = safe_math_operation(operation_func, num)
            if isinstance(result, str):
                print(result)
            elif result is None:
                print("❌ Error: Invalid input for this operation!")
            else:
                print(f"✅ Result: {operation_name}({num}) = {result}")
    
    else:
        print("❌ Invalid choice! Please select a valid option (1-14 or q).")
    
    # Ask if user wants to continue
    if input("\n🔄 Perform another calculation? (y/n): ").strip().lower() == 'n':
        print("👋 Thank you for using Riri's Calculator!")
        break

