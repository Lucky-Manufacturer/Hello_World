price = float(input("Total price: "))
tip = float(input("What % of tip would you like to leave? "))

#if "%" in tip:
#    tip = tip.replace ("%"," ")

print((price / 100) * tip)