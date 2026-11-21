# Trip cost calculator
billAmount = float(input("Whats the Bill Amount (US $): "))
tipPercentage = float(input("How much Tip you want to give (in %): "))
partyCnt = int(input("Total Number people in the Party: "))

tipAmount = billAmount * (tipPercentage / 100)
totalAmount = billAmount + tipAmount
amountPerPerson = totalAmount / partyCnt

print(f"Tip Amount is  ${tipAmount:.2f}.")
print(f"Total Amount is  ${totalAmount:.2f}.")
print(f"Amount per person is  ${amountPerPerson:.2f}.")