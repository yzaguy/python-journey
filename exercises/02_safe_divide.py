# Safe divider
try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    result = a / b
except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("You can't divide by zero.")
else:
    print(f"Result: {result:.2f}")