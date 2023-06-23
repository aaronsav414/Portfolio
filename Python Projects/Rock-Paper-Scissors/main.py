import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

computer_choice = 0
player_choice = 0


choice = int(input("Please choose 0 rock, 1 paper, or 2 scissors: "))

random_choice = int(random.randint(0, 2))

def computer_choice(random_choice):
    global computer_choice, rock, paper, scissors

    if random_choice == 0:
        computer_choice = 0
        print(rock)
    elif random_choice == 1:
        computer_choice = 1
        print(paper)
    else:
        random_choice == 2
        computer_choice = 2
        print(scissors)


def player_choice():
    global player_choice, choice, rock, paper, scissors

    if choice == 0:
        player_choice = 0
        print(rock)
    elif choice == 1:
        player_choice = 1
        print(paper)
    elif choice == 2:
        player_choice = 2
        print(scissors)
    else:
        player_choice = choice

def winner(player_choice, computer_choice):

    if choice >= 3 or choice < 0:
        print("You typed an invalid number try again.")
    elif player_choice == 0 and computer_choice == 2:
        print("Player Wins")
    elif computer_choice == 0 and player_choice == 2:
        print("Computer Wins")
    elif player_choice > computer_choice:
        print("Player Wins")
    elif computer_choice > player_choice:
        print("Computer Wins")
    else:
        player_choice == computer_choice
        print("Draw")

player_choice()
computer_choice(random_choice)
winner(player_choice, computer_choice)