#BLACK JACK 
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack_game():
    user_cards = draw_cards()
    computer_cards = draw_cards()
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"You'r cards are {user_cards}")
    print(f"Dealer's card is {computer_cards[0]}")
    pass

def draw_cards():
    dealed_cards = []
    for i in range(2):
        dealed_cards.append(random.choice(cards))
    return dealed_cards
def calculate_score(card_list):
    score = 0
    for card in card_list:
        score += card
    return score
is_continue = True
should_continue = input("Do you want to play BlackJack? type y to play and n to exit\n ")
if should_continue == "y":
    is_continue = True
elif should_continue == "n":
    is_continue = False
else:
    print("Wrong input")
while is_continue:
    blackjack_game()
    should_continue = input("Do you want to play BlackJack? type y to play and n to exit\n ")
    if should_continue == "n":
        is_continue = False