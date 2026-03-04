from art import logo
from replit import clear
import random

def pick_card():
    """ Returns a random card from the deck of cards presented to the user"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_hand):
    """ Function takes a hand of cards, and returns the current score  of the hand.
        In case the score is blackjack with 2 cards and 21 points, it returns 0
        In case of ace in hand and score > 21, it will replace score 11 with 1"""
    
    if len(cards_hand) == 2 and sum(cards_hand) == 21:
        return 0
    
    if 11 in cards_hand and sum(cards_hand) > 21:
        cards_hand[cards_hand.index(11)] = 1

    return sum(cards_hand)

def compare_scores(user_score, dealer_score):
    """ The function takes the score from computer and dealer, then it decides on the winner. """

    if dealer_score > 21 and user_score > 21:
        return "You lose miserably. You went over 21."
    
    if user_score == dealer_score:
        return "It is a draw. Better luck next time."
    elif dealer_score == 0:
        return "You lose. The dealer has a Blackjack :("
    elif user_score == 0:
        return "Congratulations. Blackjack, you win!"
    elif user_score > 21:
        return "Oh man. You went over. You lost."
    elif dealer_score > 21:
        return 'Congrats. You have won!!! Dealer went over 21.'
    elif user_score > dealer_score:
        return 'You win!'
    else: 
        return "You lose!"
    
def setup_hands(computer_hand, user_hand): 
    """initialization of players and computers hands"""

    clear()
    

    print(logo)


    user_hand.clear()
    computer_hand.clear()

    for i in range(2):

        user_hand.append(pick_card())

        computer_hand.append(pick_card())

def play_game():
    """ Setup of the main game functionality for blackjack"""
    isGameOver = False
    
    dealers_hand = []
    players_hand = []
    

    setup_hands(dealers_hand, players_hand)

    while not isGameOver:

        players_score = calculate_score(players_hand)
        dealers_score = calculate_score(dealers_hand)


        print(f"    Your hand is: {players_hand} and your current score is {players_score}.")
        print(f"    Dealer's first card: {dealers_hand[0]}")

        if players_score == 0 or dealers_score == 0 or players_score > 21:
            isGameOver = True
        else:
            pick_again = input('Would you like to pick another card? Type \'y\' or \'n\' ')
            if pick_again == 'y':
                players_hand.append(pick_card())
            else:
                isGameOver = True

    while dealers_score != 0 and dealers_score < 17:
        dealers_hand.append(pick_card())
        dealers_score = calculate_score(dealers_hand)



    print(f"     Your final score: {players_score} and your final hand is {players_hand}")
    print(f"     Computer's final score: {dealers_score} and your final hand is {dealers_hand}")
    print(f"{compare_scores(players_score, dealers_score)}")


while input("Would you like to play a game of blackjack (y/n) ") == 'y':
    clear()
    play_game()