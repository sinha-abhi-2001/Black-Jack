#BLACK JACK 
import random
import os
def deal_card():
    '''Deals a random card from the card list'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare_score(user_score, computer_score):
    if user_score ==0 or computer_score > 21:
        print("You win.")
    elif computer_score == 0 or user_score > 21:
        print("You loose.")
    elif user_score > computer_score:
        print("You win")
    else:
        print("You loose")
def black_jack():
    user_cards= []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        """Dealing 2 cards from the deck to user and computer"""
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"You'r cards are {user_cards} and current score is {user_score}")
        print(f"Dealer's first card is {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            is_game_over = True
        user_should_draw = input("Type y to take another card or n to pass:\n")
        if user_should_draw == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        if computer_score > 21:
            if 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)

    compare_score(user_score, computer_score)
    print(f"You'r score is {user_score} and dealer's score is {computer_score} and cards are {computer_cards}")


is_continue = True
should_continue = input("Do you want to play BlackJack? type y to play and n to exit\n ")
if should_continue == "y":
    is_continue = True
elif should_continue == "n":
    is_continue = False
else:
    print("Wrong input")
while is_continue:
    black_jack()
    should_continue = input("Do you want to play BlackJack? type y to play and n to exit\n ")
    if should_continue == "n":
        is_continue = False
    else:
        os.system('cls')