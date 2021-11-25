from art import logo
print(logo)
bidding={}
bidding_finished= False

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid= bid_amount
            winner = bidder
    print(f"The winner is {winner} and won with higgest bid of {highest_bid}")
while not bidding_finished:
    name = input("What is your name?")
    bid_price = int(input("What is your bid price"))
    bidding[name] = bid_price
    user_choice = input("More biiders? 'yes or no'")
    if(user_choice=="no"):
        bidding_finished= True
        print("Bye")

highest_bidder(bidding)
