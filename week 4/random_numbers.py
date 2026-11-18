def append_random_numbers(number_list, quantity=1):
    while True:
        number = float(input("Enter the number: "))
        if number != 0.0:
         number_list.append(number)

        elif number == 0.0:
            break
    
def main():
    numbers = [16.2, 75.1, 52.3]

    print(numbers)

    append_random_numbers(numbers)

    print(numbers)
    
    append_random_numbers(numbers, 0)

    
# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
