"""
Author: Prince Francis Okoi

Purpose: To write a program that will 
allow users to record expenses, categorise them and calculate the total 
expense to enable the user make better financial decisions.


"""

import csv
from datetime import datetime

import os

#ensure file is saved in parent folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "expenses.csv")


def load_expenses(filename):
    expenses = []

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                date, category, amount = row
                expenses.append((date, category, float(amount)))
    except FileNotFoundError:
        pass

    return expenses


def save_expense(filename, expense):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense)


def calculate_total(expenses):
    return sum(amount for _, _, amount in expenses)


def filter_by_category(expenses, category):
    return [exp for exp in expenses if exp[1].lower() == category.lower()]

def get_expense_input():
    item = input("Enter item: ")
    amount = float(input("Enter amount: "))
    #Get current date and time of purchase
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (date, item, amount)

def display_summary(expenses):
    if not expenses:
        print("\n No expenses recorded.\n")
        return

    print("\nExpenses:\n")

    
    for date, item, amount in expenses:
        print(f"{date} | {item} | ${amount:.2f}")

    
    print(f"\nTotal spent: ${calculate_total(expenses):.2f}\n")


def main():
    expenses = load_expenses(FILE_NAME)

    while expenses:
        print("Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Exit")

        choice = int(input("Choose option: "))

        if choice == 1:
            expense = get_expense_input()
            save_expense(FILE_NAME, expense)
            expenses.append(expense)
            print("Item saved.\n")

        elif choice == 2:
            display_summary(expenses)

        elif choice == 3:
            cat = input("Enter item name to filter: ")
            filtered = filter_by_category(expenses, cat)
            display_summary(filtered)

        elif choice == 4:
            print("Thank you, Goodbye.")
            break

        else:
            print("Invalid choice. Try again\n")


if __name__ == "__main__":
    main()
