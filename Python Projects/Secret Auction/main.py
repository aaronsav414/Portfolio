import os

#HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidding = False



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bidder(bidding_record):
    """Checks the 'bidding record' to return the highest bidder in the auction."""
    global bidding
    highest_bid = 0
    bidder_name = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            bidder_name = bidder
    print(f"{bidder_name} wins with a bid of {highest_bid}.")

    bidding = False

print(logo)
on_button = input("On or Off: ").lower()
if on_button == "on":
    bidding = True
else:
    bidding = False

bidders = {}

while bidding == True:

    name = str(input("What is your name? "))
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    print(bidders)
    choice = str(input("Are there any other bidders? Yes or No? ")).lower()

    if choice == "yes":
        os.system("clear")
    else:
        highest_bidder(bidders)
        bidding = False



