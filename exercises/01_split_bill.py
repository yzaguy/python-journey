# Bill Splitter
amt_bill = float(input("What's the Total Bill Amount (US $): "))
percent_tip = float(input("How much Tip you want to give (in %): "))
num_people = int(input("Total Number people in the Party: "))

amt_tip = amt_bill * (percent_tip / 100)
amt_total = amt_bill + amt_tip
amt_person = amt_total / num_people

print(f"Tip Amount is ${amt_tip:.2f}.")
print(f"Total Amount is ${amt_total:.2f}.")
print(f"Amount per person is ${amt_person:.2f}.")