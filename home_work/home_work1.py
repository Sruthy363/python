rice_price = 45
sugar_price = 40
oil_price = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

rice = rice_price * rice_qty
sugar = sugar_price * sugar_qty
oil = oil_price * oil_qty

print("Total price for rice", rice)
print("Total price for sugar", sugar)
print("Total price for oil", oil)

total_bill = rice + sugar + oil
print("Total bill", total_bill)

bill_int = int(total_bill)
print("Total bill in int", bill_int)

bill_str = str(total_bill)
print("Total bill in str", bill_str)

import random
delivery_charge = random.randint(5, 10)
final_bill = total_bill + delivery_charge
print("Delivery charge is", delivery_charge)
print("Final bill is", final_bill)
