import random
from guessing_number_art import logo
easy_level = 5
hard_level = 10

def clear():
    print('\n' * 50)

def check_answer(g,a,t):
    if(g > a):
        print("Too high.")
        return t - 1
    if(g < a):
        print("Too low.")
        return t - 1
    else:
        print(f"You got it! The answer was {a}.")

def foo():
    level = input("Type 'easy' if you want to choose easy level, type 'hard' if you want hard level\n")
    if level == 'easy':
        return easy_level
    if(level == 'hard'):
        return hard_level
    else:
        return "Your level is not available."

def play_game():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    guess = 0 
    turns = foo()
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            clear()
            return
        elif guess != answer:
            print("Guess again.")
            

play_game()

