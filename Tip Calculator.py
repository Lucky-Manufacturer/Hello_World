price = float(input("Total price: "))
tip = float(input("What % of tip would you like to leave? "))

print("Total tip amount: " + str((price / 100) * tip))
print("Total :" + str(price + tip))