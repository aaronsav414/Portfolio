import random

from game_data import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# Chose random number for data list

a = []
b = []
count = 0

game_on = False

def shuffle():
    global a, b, data
    a = random.choice(data)
    b = random.choice(data)
    display()
    while a == b:
        b = random.choice(data)

def zero_out():
    global a, b, count, game_on
    count = 0
    a.clear()
    b.clear()
    game_on = False
    choice = input("Would you like to play Higher or Lower? Y or N: ").lower()
    if choice == "y":
        game_on = True

def compare():
    global a, b, count
    choice = input("Who has more followers? A or B ").lower()
    if choice == "a":
        if a['follower_count'] > b['follower_count']:
            print("You got it!")
            count += 1
            shuffle()
            compare()
        else:
            print('Sorry "B" has more followers.')
            zero_out()
    else:
        if a['follower_count'] < b['follower_count']:
            print("You got it!")
            count += 1
            shuffle()
            compare()
        else:
            print('Sorry "A" has more followers.')
            zero_out()

def display():
    global a, b, count, game_on
    print(f"The count is {count}.")
    print(f"Compare A: {a['name']} a {a['description']} from {a['country']}.")
    print(vs)
    print(f"Compare B: {b['name']} a {b['description']} from {b['country']}.")

choice = input("Would you like to play Higher or Lower? Y or N: ").lower()
if choice == "y":
    game_on = True

while game_on == True:
    print(logo)
    shuffle()
    compare()









