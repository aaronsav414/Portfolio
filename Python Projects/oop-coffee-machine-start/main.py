from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
menu_item = MenuItem


machine_on = False

power_button = input("Turn on Machine. Y or N ").lower()
if power_button == "y":
    machine_on = True
elif power_button == "off":
    machine_on = False


while machine_on == True:
    names = ['latte', 'espresso', 'cappuccino']
    options = menu.get_items()
    choice = str(input(f"What would you like? {options}: "))
    if choice == "off":
        machine_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    for name in names:
        if name == choice:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

