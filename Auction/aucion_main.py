from auction_art import logo
print(logo)
import random
from auction_things import thing_list
print(f"Today at the auction we have {random.choice(thing_list)} .Place your bets!")
bids = {}
boolen = False

def clear():
    print('\n' * 50)

def auction(x):
    highest_bind = 0
    winner = ""
    for bidder in x:
        bid_amount = x[bidder]
        if(bid_amount > highest_bind):
            highest_bind = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bind}.")

while not boolen:
    name = input("What's your name?\n")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_cont = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if(should_cont == 'no'):
        boolen = True
        auction(bids)
    else:
        clear()

