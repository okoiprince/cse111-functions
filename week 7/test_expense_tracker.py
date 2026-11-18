import os
import csv
import pytest
from pytest import approx
from expense_tracker import (
    load_expenses,
    save_expense,
    calculate_total,
    filter_by_category
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE= os.path.join(BASE_DIR, "test_expenses.csv")

# Check file path
def setup_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


# CTest functions 
def test_save_expense():
    expense = ("2026-02-17", "Food", 25.5)

    save_expense(TEST_FILE, expense)

    with open(TEST_FILE, "r") as filename:
        reader = csv.reader(filename)
        rows = list(reader)

    assert rows == [["2026-02-17", "Food", "25.5"]]

def test_load_expense():
      # manually create test file
    with open(TEST_FILE, "w", newline="") as filename:
        writer = csv.writer(filename)
        writer.writerow(["2026-02-17", "Food", "10"])
        writer.writerow(["2026-02-17", "Transport", "20"])

    expenses = load_expenses(TEST_FILE)

    assert expenses == [
        ("2026-02-17", "Food", 10.0),
        ("2026-02-17", "Transport", 20.0)
    ]

def test_calculate_total():
    expenses = [
        ("2026-02-17", "Food", 10),
        ("2026-02-17", "Transport", 20)
    ]
    assert calculate_total(expenses) == 30


def test_filter_by_category():
    expenses = [
        ("2026-02-17", "Food", 10),
        ("2026-02-17", "Transport", 20),
        ("2026-02-17", "Food", 5)
    ]

    result = filter_by_category(expenses, "Food")
    assert result == [
        ("2026-02-17", "Food", 10),
        ("2026-02-17", "Food", 5)
    ]


def test_filter_case_insensitive():
    expenses = [("2026-02-17", "Food", 10)]
    result = filter_by_category(expenses, "food")
    assert result == [("2026-02-17", "Food", 10)]


def test_load_missing_file():
    result = load_expenses("nonexistent.csv")
    assert result == []

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
