"""
Author: Prince Francis Okoi

Purpose: To write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total. 

Creative addition: Added extra code to print a "return by" date that is 9:00 PM 30 days in the future at the bottom of the receipt on line 83 

"""

import csv
import time
from datetime import datetime, timedelta

SALES_TAX_RATE = 0.06  # 6%
KEY_INDEX = 0

def read_dictionary(filename, key_column_index):
    dictionary_list = {}

    with open(filename, "rt") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ",")
        next(csv_reader)
        for row in csv_reader:
            key_value = row[key_column_index]
            dictionary_list[key_value] = row

    return dictionary_list

def read_requests(filename):
    requests = []
    with open(filename, "rt") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        next(csv_reader)  # skip header
        for row in csv_reader:
            product_number = row[0]
            quantity = int(row[1])
            requests.append((product_number, quantity))
            
    return requests

def main():
    try:
        products_dict = read_dictionary("products.csv", KEY_INDEX)
        requests_list = read_requests("request.csv")

        print("Prince's Enterprise\n")

        subtotal = 0
        total_items = 0

        # Print the item in request list
        for product_number, quantity in requests_list:
            try:
                product = products_dict[product_number]
                product_name = product[1]
                product_price = float(product[2])
                item_total = product_price * quantity

                subtotal += item_total
                total_items += quantity

                print(f"{product_name}: {quantity} @ {product_price:.2f}")

            except KeyError:
                print(f"Product {product_number} not found in inventory.")

        sales_tax = round(subtotal * SALES_TAX_RATE, 2)
        total_due = round(subtotal + sales_tax, 2)

        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_due:.2f}")
        print(f"Thank you for shopping at the Prince's Enterprise.")

        # Current date and time
        current_time = time.ctime()
        print(current_time)

        # Added code for Return by date after 30 days from now at 9:00 PM
        now = datetime.now()
        return_date = (now + timedelta(days=30)).replace(hour=21, minute=0, second=0, microsecond=0)
        print(f"Return by: {return_date.strftime('%a %b %d %I:%M %p %Y')}")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except PermissionError as e:
        print(f"Error: Permission denied - {e.filename}")
    except KeyError as e:
        print(f"Error: Product not found - {e}")



if __name__ == "__main__":
    main()