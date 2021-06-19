import math

price = int(input())

tax_price = math.floor(1.08 * price)

if tax_price < 206:
    print("Yay!")
elif tax_price == 206:
    print("so-so")
else:
    print(":(")