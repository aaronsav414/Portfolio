import random
from hangman_art import stages, logo
from hangman_words import word_list

# Select word for game
chosen_word = random.choice(word_list)

lives = stages.copy()

chosen_letters = []

# Blank list to display to user
blanks = list("_" * len(chosen_word))

print(logo)

game_on = True

while game_on == True:

    print(lives[-1])
    print(len(lives) - 1)
    print(blanks)
    # User inputs a letter

    if len(lives) == 1:
        print(lives[0])
        print("You Lose! Try again.")
        game_on = False
        break

    guess = input("Guess a letter: ").lower()

    if guess in chosen_letters:
        print("You already chose that letter.")

    chosen_letters.append(guess)

# check if chose letter is in chosen word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            blanks[position] = letter
            print(f"{guess.upper()} is in the word.")

    if guess not in chosen_word:
        lives.pop()
        print("Uh oh, that letter isn't in the word.")

# chemk if the player has won
    elif "_" not in blanks:
        game_on = False
        print("You Win!")
        print(blanks)


