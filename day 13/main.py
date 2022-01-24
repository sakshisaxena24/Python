from art import logo
from art import vs
from game_data import data

import random
print(logo)

def get_accoundetails(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f" {account_name}, a {account_desc}, from {account_country}")

def check_answer(guess, a_followers,b_followers):
    if a_followers > b_followers:
        return guess=="a"
    else:
        return guess == "b"
game_should_continue = True
score= 0
account_b = random.choice(data)
while game_should_continue:
    account_a= account_b
    account_b = random.choice(data)

    while account_b==account_a:
        account_b= random.choice(data)

    print(f"Compare A{get_accoundetails(account_a)}")
    print(vs)
    print(f"Compare B{get_accoundetails(account_b)}")

    guess = input("Who has more followers A or B? ").lower()

    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower,b_follower)
    print("______________________________________________________")
    if is_correct:
        score+=1
        print(f"You are right! ,current score: {score}")
    else:
        game_should_continue= False
        print(f"You are wrong , final score :{score}")