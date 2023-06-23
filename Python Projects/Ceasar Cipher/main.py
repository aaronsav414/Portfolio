alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

on = True

def encrypt():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encoded_message = ""
    for char in text:
        if char in alphabet:
            encoded_character = (alphabet.index(char) + shift) % len(alphabet)
            encoded_message += alphabet[encoded_character]
        else:
            print("I dont know what that was. Try again")
            encrypt()

    print(f"The encoded text is {encoded_message}")


def decrypt():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encoded_message = ""
    for char in text:
        if char in alphabet:
            encoded_character = (alphabet.index(char) - shift) % len(alphabet)
            encoded_message += alphabet[encoded_character]
        else:
            print("I dont know what that was. Try again")
            decrypt()
    print(f"The encoded text is {encoded_message}")


def startup():
    global on
    on = False
    choice = input("To feel the power type 'on', otherwise peace out: ")
    if choice == "on":
        print(logo)
        program()

def program():
    global on
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode":
        encrypt()
        startup()
    elif direction == "decode":
        decrypt()
        startup()
    elif direction == "off":
        print("Power Off")
        on = False
    else:
        print("Sorry bro dats the wrong entry. Try something else.")
        startup()



startup()


# Second Method

# alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# on = False
#
# def program():
#
#     cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     start_text = input("Type your message:\n").lower()
#     shift_amount = int(input("Type the shift number:\n"))
#
#     encoded_message = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for letter in start_text:
#         encoded_character = (alphabet.index(letter) + shift_amount) % len(alphabet)
#         encoded_message += alphabet[encoded_character]
#     print(f"The {cipher_direction}d text is {encoded_message}")
#
# while on == False:
#     power = input("Type on to feel the power: ")
#     if power == "on":
#         program()
# else:
#     print("Power Down")

