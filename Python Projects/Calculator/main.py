logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(first_num, second_num):
    return first_num + second_num

def subtract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num

def keep_calculating():
    global first_num, answer, calc_on
    choice = input("Keep calculating. Yes or No? ").lower()
    if choice == "yes":
        first_num = answer
        print(f"First number is {first_num}")
    else:
        print("Resetting")
        calc_on = False
        first_num = 0
        answer = 0

def start():
    global first_num, calc_on
    if calc_on == False:
        choice = str(input("On or Off: "))
        if choice == "on":
            calc_on = True
            first_num = float(input("Pick a number: "))
        else:
            calc_on = False

def choose_operator():
    global first_num, second_num, answer, calc_on
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    
    for operation in operations:
        print(operation)
    operator = input("Pick an operation: ")
    if operator in operations:
        calculate = operations[operator]
        second_num = float(input("Pick a second number: "))
        answer = calculate(first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {answer}")
    else:
        print(first_num)
        choose_operator()

    # if operator == "+":
    #     result = add(first_num, second_num)
    #     print(f"{first_num} + {second_num} = {result}")
    # elif operator == "-":
    #     result = subtract(first_num, second_num)
    #     print(f"{first_num} - {second_num} = {result}")
    # elif operator == "*":
    #     result = multiply(first_num, second_num)
    #     print(f"{first_num} * {second_num} = {result}")
    # elif operator == "/":
    #     result = divide(first_num, second_num)
    #     print(f"{first_num} / {second_num} = {result}")
    # else:
    #     print("Please enter a valid operator.")

calc_on = False
first_num = 0
second_num = 0
answer = 0

start()

while calc_on == True:
    choose_operator()
    keep_calculating()
    start()




