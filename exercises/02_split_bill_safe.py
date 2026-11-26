#Safe Bill Splitter
try:
    total_bill = float(input("Enter the total bill amount: "))
    num_people = int(input("Enter the number of people to split the bill: "))
    tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): ")) 
    amount_per_person = (total_bill + (total_bill * tip_percentage / 100)) / num_people
except ValueError:
    print("Please enter valid numbers for the bill and number of people.")
except ZeroDivisionError:
    print("The number of people cannot be zero.")
else:
    if num_people <= 0:
        print("The number of people must be greater than zero.")
    elif int(num_people) != num_people:
        print("The number of people must be a whole number.")
    elif total_bill <= 0:
        print("The total bill amount must be greater than zero.")
    elif tip_percentage < 0:
        print("The tip percentage cannot be negative.")
    else:
        print(f"Each person should pay: ${amount_per_person:.2f}")  