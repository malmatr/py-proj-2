import random
from art import logo

EASY_LEVEL_GUESSES = 10 
HARD_LEVEL_GUESSES = 5 

def set_difficulty():
    difficulty_level = input("Choose a difficulty level: (easy/hard) \n")

    if difficulty_level == 'easy':
        return EASY_LEVEL_GUESSES
    elif difficulty_level == 'hard':
        return HARD_LEVEL_GUESSES

def determine_guess(players_guess, target, guess_number):
    if players_guess == target:
        print("You have guessed it correctly! Good job")
        return 0
    elif players_guess > target:
        print("Too high. Guess Again")
        return guess_number - 1
    elif players_guess < target:
        print("Too low. Guess Again")
        return guess_number - 1

def game():

    print(logo)
    print("I am thinking of the number between 1 and 100.")

    number_of_guesses = set_difficulty()

    number_goal = random.randint(1,100)
    
    while number_of_guesses > 0:

        print(f"You have {number_of_guesses} remaining to guess a number.")
        user_guess = int(input('Make a guess: '))


        number_of_guesses = determine_guess(user_guess, number_goal, number_of_guesses)

game()