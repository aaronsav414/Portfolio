import random
from random import shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
final_password = ""

def choose_letters():
    global password, nr_letters
    while int(nr_letters) > 0:
        random_letter = letters[random.randrange( 0, len(letters) - 1 )]
        password.append(random_letter)
        nr_letters -= 1

    else:
        choose_symbols()

def choose_symbols():
    global password, nr_symbols
    while int(nr_symbols) > 0:
        random_symbol = symbols[random.randrange( 0, len(symbols) - 1 )]
        password.append(random_symbol)
        nr_symbols -= 1

    else:
        choose_numbers()

def choose_numbers():
    global password, nr_numbers, final_password
    while int(nr_numbers) > 0:
        random_number= numbers[random.randrange( 0, len(numbers) - 1 )]
        password.append(random_number)
        nr_numbers -= 1

    else:
        shuffle(password)
        final_password = "".join([str(let) for let in password])




choose_letters()

choose_symbols()

choose_numbers()
print(final_password)

