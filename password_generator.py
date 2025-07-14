import random
import string

def password_generator(length=8, use_uppercase=True, use_numbers=True, use_special_chars=True):
    #if length is less than 1, raise an error
    if length < 1:
        raise ValueError("Password length must be at least 1")
    #create a pool of characters based on user preferences
    characters = string.ascii_lowercase
    #add uppercase letters, numbers, and special characters based on user input if user wants them
    if use_uppercase:
        characters += string.ascii_uppercase
    #add numbers and special characters based on user input only if user wants them
    if use_numbers:
        characters += string.digits
    #add special characters based on user input only if user wants them
    if use_special_chars:
        characters += string.punctuation

    #generate a random password from the character pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    try:
        #get user input for password generation parameters
        length = int(input("Enter the desired password length (default 8): ") or 8)
        use_uppercase = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
        use_numbers = input("Include numbers? (y/n, default y): ").lower() != 'n'
        use_special_chars = input("Include special characters? (y/n, default y): ").lower() != 'n'

        #generate password based on user input
        password = password_generator(length, use_uppercase, use_numbers, use_special_chars)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"An error occurred: {e}")