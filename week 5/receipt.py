import os
import csv
def read_dictionary(filename, key_column_index):
    dictionary_list = {}

    with open(filename, "rt") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ",")
        next(csv_reader)
        for row in csv_reader:
            key_value = row[key_column_index]
            dictionary_list[key_value] = row

    return dictionary_list

def main():
    KEY_INDEX = 0
    products_dict = read_dictionary("products.csv", KEY_INDEX)

    print(products_dict)

    print("Current working directory:", os.getcwd())


if __name__ == "__main__":
    main()