MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

profit = 0.00
count = 0.00

def reset_value(num):
    num = 0.00
    return num


def add_money(drink):
    global count
    coin = input("Insert coins: \nquarter 'q'\ndime 'd'\nnickel 'n'\npenny 'p'\nNot enough coins? reset: ")
    print(f"The coffee is: {drink['cost']}")
    if coin == "q":
        count += 0.25
    elif coin == "d":
        count += 0.10
    elif coin == "n":
        count += 0.05
    elif coin == "p":
        count += 0.01
    elif coin == "r":
        resource_compare(drink, resources)
    else:
        print('invalid entry.')
    check_transaction(drink, profit, count)

def subtract_resources(drink, resources):
    global count
    resources['water'] -= drink['ingredients']['water']
    resources['milk'] -= drink['ingredients']['milk']
    resources['coffee'] -= drink['ingredients']['coffee']
    if count > 0.00:
        count = 0.00
    else:
        pass

def add_resoources(resources):
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100

def check_transaction(drink, profit, count):

    if count < drink['cost']:
        print(count)
        add_money(drink)

    elif count > drink['cost']:
        print("Here is your coffee!")
        profit += count
        print(f"Profit is: {round(profit, 3)}")
        change = count - drink["cost"]
        print(f"Your change is {round(change, 3)}.")
        reset_value(change)

    elif count == drink['cost']:
        print("Here is your coffee!")
        profit += count
        print(f"Profit is: {profit}")

    subtract_resources(drink, resources)



def resource_compare(drink, resources):
    if drink['ingredients']["water"] > resources["water"]:
        print("There is not enough water to make this coffee.")
    elif drink['ingredients']['milk'] > resources["milk"]:
        print("There is not enough milk to make this coffee.")
    elif drink['ingredients']['coffee'] > resources["coffee"]:
        print("There is not enough coffee.")
    else:
        check_transaction(drink, profit, count)




while is_on:
    choice = input("Please choose your coffee.\n espresso \n cappuccino \n latte: ")
    if choice == "off":
        is_on = False
    elif choice == "add resources":
        add_resoources(resources)
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        resource_compare(drink, resources)

    #
    #
    #
    # while payment < drink['cost']:
    #     amount = input("Insert coins")
    #     payment += amount
    # if payment == drink['cost']:

# TODO: 1. Print a report of all the coffee machine resources.


# TODO 2. Check Resources sufficient.


# TODO 3. Process Coins.


# TODO 4. Check transaction successful.
