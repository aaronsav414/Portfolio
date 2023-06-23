import random

attempts = 0
number_to_guess = random.choice(range(1, 101))
chosen_num = 0

game_on = False

def reset():
    global game_on, attempts, chosen_num, number_to_guess
    number_to_guess = random.choice(range(1, 101))
    chosen_num = 0
    attempts = 0
    game_on = False

def guess():
    global chosen_num
    print(f"You have {attempts} attempts remaining to guess the number.")
    num_guess = int(input("Make a guess. "))
    chosen_num = num_guess

def check_guess():
    global  game_on, chosen_num, attempts, number_to_guess
    if attempts == 0:
        print("You ran out of guesses. Try again.")
        print(f"The number to guess was {number_to_guess}.")
        reset()
    if chosen_num == number_to_guess:
        print("You guessed the number! Nice job!")
        print(f"The number to guess was {number_to_guess}.")
        reset()
    elif chosen_num < number_to_guess:
        attempts -= 1
        print("Too Low.")
        print("Guess again.")
    elif chosen_num > number_to_guess:
        attempts -= 1
        print("Too High.")
        print("Guess again.")

def game():
    global game_on, attempts
    choice = input("Choose a difficulty. Type 'hard' or 'easy': ")
    if choice == "hard":
        attempts = 5
    else:
        attempts = 10
    while game_on == True:
        guess()
        check_guess()

while game_on == False:
    choice = input("Would you like to start the game? 'Y' or 'N' ").lower()

    if choice == "y":
        game_on = True
        print("Welcome to the Number Guessing Game!")
        print("Im thinking of a number between 1 and 100.")
        game()

    else:
        reset()
        game_on = "off"







