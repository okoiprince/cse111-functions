def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """ 
    text_list = []

    with open (filename, "rt") as text_file:

        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    return text_list

def main():
    provinces_list = read_list("provinces.txt")

    #print the entire list
    print(provinces_list)
    
    #count the number of times Alberta appears in the initial list
    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the list")

    #remove the first element from the list
    provinces_list.pop(0)

    #remove the last element from the list 
    provinces_list.pop()

    #replace all occurrence of AB with Alberta 
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    print()
    print(provinces_list)

    #call the count method which count the number of times Alberta appears in the list
    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list")

# Call the main function.
if __name__ == "__main__":
    main()
