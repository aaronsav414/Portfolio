import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_card():
    global cards, user_count, computer_count
    while len(user_cards) < 2:
        num = random.choice(cards)
        user_cards.append(num)
    while len(computer_cards) < 2:
        num = random.choice(cards)
        computer_cards.append(num)

def calculate_score():
    global game_on, user_count, computer_count

    # Calculate Black Jack
    if len(user_cards) == 2 and sum(user_cards) == 21:
        user_cards.clear()
        user_cards.append(0)
        print("Black Jack! You Win!")
        game_on = False
    elif len(computer_cards) == 2 and sum(computer_cards) == 21:
        computer_cards.clear()
        computer_cards.append(0)
        print("Black Jack! House Wins! Sorry, you lose.")
        game_on = False
    for num in enumerate(user_cards):
        if num == 11 and sum(user_cards) > 21:
            user_cards.remove(11)
            user_cards.append(1)
    for number in enumerate(computer_cards):
        if number == 11 and sum(computer_cards) > 21:
            computer_cards.remove(11)
            computer_cards.append(1)

def compare():
    global game_on, user_cards, computer_cards
    print_cards()
    if sum(user_cards) == sum(computer_cards) or (sum(user_cards) > 21 and sum(computer_cards) > 21):
        print("Its a Draw!")
    elif sum(user_cards) <= 21:
        if sum(user_cards) > sum(computer_cards) or sum(computer_cards) > 21:
            print("You Win!")
    elif sum(computer_cards) <= 21:
        if sum(computer_cards) > sum(user_cards) or sum(user_cards) > 21:
            print("House Wins! Sorry, you lose.")

    game_on = False
    user_cards.clear()
    computer_cards.clear()

def print_cards():
    global user_cards, computer_cards
    print(user_cards)
    print(computer_cards)
    print(f"Your Score is {sum(user_cards)}")
    print(f"Computer Score is {sum(computer_cards)}")


def game():
    global cards, game_on, user_cards, computer_cards

    deal_card()
    print(user_cards)
    print(computer_cards)
    choice = input("Do you want to Hit or Stay? ").lower()
    if choice == "hit":
        user_cards.append(random.choice(cards))
        calculate_score()
        game()
    else:
        while sum(computer_cards) <= 17:
            computer_cards.append(random.choice(cards))
            calculate_score()
        calculate_score()
        compare()
        game_on = False

game_on = False

while game_on == False:
    choice = input("Would you like to play a game of Black Jack. 'Y' or 'N'? ").lower()
    if choice == "y":
        game_on = True
        print(logo)
        game()
    elif choice == "n":
        game_on = "off"


