#Author Prince Francis Okoi

#Calculate the customers discount for tuesday and wednesdays for a retail store

from datetime import datetime

#Constants declaration
DISCOUNT_RATE = 0.1
TAX_RATE = 0.06
TUES = 1
WED = 2

#Declare Variables
current_date = datetime.now()
week_day = current_date.weekday()
print(week_day)
print(current_date)
#subtotal = float(input("Enter the value of Subtotal: "))
subtotal = 0
discount = 0
quantity = 1

#Iterate through data
while quantity != 0:
    quantity = int(input("Enter the quantity: "))
    if quantity != 0:
        price = float(input("Enter the unit Price: "))
        subtotal += quantity * price

#Compute the week days
if week_day == TUES or week_day == WED:
    if subtotal >= 50:
        discount = subtotal * DISCOUNT_RATE
    elif subtotal < 50:
        shortfall = 50 - subtotal
        print(f"Purchase additional: ${shortfall:.2f} items to get Discount")
    else:
        print("No Data")

print(f"Discount: ${discount:.2f}")
print(f"Total order: ${subtotal:.2f}")

#Compute the sales tax and discount
subtotal -= discount
tax = subtotal * TAX_RATE
total = subtotal + tax

#Print sales tax and total due
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Due: ${total:.2f}")