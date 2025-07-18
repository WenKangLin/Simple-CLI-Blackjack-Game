import random

from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def win_condition(player_score, dealer_score):
    if player_score > 21:
        print("You went over. Dealer wins!")
    elif dealer_score > 21:
        print("Dealer went over. You win!")
    elif dealer_score > player_score:
        print("Dealer wins!")
    elif dealer_score < player_score:
        print("You win!")
    else:
        print("Push!")

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def play_blackjack():
    player_hand = [random.choice(cards), random.choice(cards)]
    dealer_hand = [random.choice(cards), random.choice(cards)]
    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            hit = input("Type 'h' to hit or 's' to stand: ")
            if hit == 'h':
                player_hand.append(random.choice(cards))
            else:
                while dealer_score < 17:
                    dealer_hand.append(random.choice(cards))
                    dealer_score = calculate_score(dealer_hand)
                game_over = True

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    win_condition(player_score, dealer_score)

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    print(logo)
    play_blackjack()