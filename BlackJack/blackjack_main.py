from blackjack_art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def clean():
    print('\n' * 50)

def deal_cards(x):
    return random.sample(x, 2)

def calculate_score(x):
   if len(x) == 2):
        return 0
    if 11 in cards and sum(x) > 21:
        x.re if (sum(x) == 21 amove(11)
        x.append(1)
    return sum(x)
        
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
    print(logo)
    user_cards = deal_cards(cards)
    computer_cards = deal_cards(cards)
    end_of_game = False

    while not end_of_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if(user_score == 0 or computer_score == 0 or user_score > 21):
            end_of_game = True
        else:
            user_scould_deal = input("Type 'yes' to get another card , type 'no' to pass:").lower()
            if(user_scould_deal == 'yes'):
                user_cards.append(random.choice(cards))
            else:
                end_of_game = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game Blackjack? Type 'yes' or 'no':\n") == 'yes':
    clean()
    play_game() 
