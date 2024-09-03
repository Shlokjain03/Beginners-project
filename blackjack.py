import random


def deal_cards():
    #return  random card from deck
    cards = [11,2,3,4,5,6,7,8,910,10,10,10]
    card=random.choice(cards)
    return cards


def calcu_score(cards):
    # take list of cards & return score
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare (u_score,c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose "
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win "
    else:
        return "You lose "
def game():
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_over=False

    for i in range (2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())


    while not is_over:
        user_score=calcu_score(user_cards)
        computer_score=calcu_score(computer_cards)
        print(f" Your cards: {user_cards}, current_score:{user_score}")
        print(f"Computer first cards:{computer_cards[0]}")

        if user_score ==0 or computer_score ==0 or user_score>21:
            is_over:True
        else:
            user_should_continue=input("Type y for another car and n to pass: \n ")
            if user_should_continue =="y":
                user_cards.append(deal_cards())
            else:
                is_over=True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_cards())
        computer_score=calcu_score(computer_cards)

    print(f"Your final hand:{user_cards} ,final score{user_score}")
    print(f"Computer final hand{computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play game of Blackjack? Type y or n: \n ") =="y":
    print("\n" *15)
    game()