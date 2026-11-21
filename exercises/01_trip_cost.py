# Trip cost calculator
distance = float(input("Trip distance (miles): "))
mpg = float(input("Your car's miles per gallon: "))
gas_price = float(input("Gas price per gallon ($): "))

gallons = distance / mpg
cost = gallons * gas_price

print(f"You'll use {gallons:.1f} gallons.")
print(f"Trip cost: ${cost:.2f}")