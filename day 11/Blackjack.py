import random

from art import logo



def deal_Card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card =random.choice(cards)
    return card
def calculate_score(cards):
    #returning sum will be 0 or actual sum below 21
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,dealer_score):
    if user_score==dealer_score:
        return "It is a draw"
    elif dealer_score==0:
        return "You Lost"
    elif user_score ==0:
        return "Won with a blackjack"
    elif user_score>21:
        return "You went over. You lose"
    elif dealer_score>21:
        return "Dealer went over. You lose"
    elif user_score>dealer_score:
        return "User wins!!"
    else:
        return "You lose"
def play_game():
    print(logo)
    is_game_over= False
    User= []
    Dealer=[]
    for _ in range(2):
        User.append(deal_Card())
        Dealer.append(deal_Card())

    while is_game_over== False:
        user_score=calculate_score(User)
        dealer_score= calculate_score(Dealer)
        print(f"Your cards are: {User}, Current score: {user_score}")
        print(f" Computer's first cards are: {Dealer[0]}")
        if user_score==0 or dealer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal= input("type 'y' to get another card, type 'n' to pass")
            if user_should_deal== "y":
                User.append(deal_Card())
               #print(User)
            else:
                is_game_over= True

    while dealer_score!=0 and dealer_score<17:
        Dealer.append((deal_Card()))
        dealer_score= calculate_score(Dealer)
    print(f" Your final hand: {User}, final score: {user_score}")
    print(f" Dealer's final hand: {Dealer}, final score: {dealer_score}")
    print(compare(user_score,dealer_score))

while input("You want to play a game of Blackjack? 'y' or 'n'") == "y":
    play_game()

