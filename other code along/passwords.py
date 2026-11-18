"""
Author: Prince Francis Okoi

Purpose: Write functions with parameters and call those functions multiple times with arguments.

Creative addition: Number of attempts on line 105
"""
#Constants/list
LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|",";",":","'","\"",",",".","<",">","?","/","\\","`","~"]


def word_in_file(word, filename, case_sensitive=False):
    #Reads a file where each line contains a single word.
    #Returns True if the word exists in the file, otherwise False.

    with open("wordlist.txt", "r", encoding="utf-8") as filename:
        for line in filename:
            line = line.strip()

            if case_sensitive:
                if word == line:
                    return True
            else:
                if word.lower() == line.lower():
                    return True

    return False


def word_has_character(word, character_list):
    """
    Returns True if any character in word exists in character_list.
    """
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
    """
    Calculates complexity score (0–4) based on character types.
    """
    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


def password_strength(password, min_length=10, strong_length=16):
    """
    Determines password strength from 0 to 5.
    """

    # Dictionary check (case-insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # Common password check (case-sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Length checks
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) > strong_length - 1:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Complexity-based strength
    complexity = word_complexity(password)
    strength = 1 + complexity

    return strength

def main():
    """
    User input loop.
    """
    while True:
        password = input("Enter a password to test (Q to quit): ")

        if password.lower() == "q":
            print("Goodbye!")
            break

        strength = password_strength(password)
        print(f"Password strength: {strength}\n")


if __name__ == "__main__":
    main()