import random
import hangman_art
import hangman_words
word = random.choice(hangman_words.word_list)
lives = 6
end_of_game = False

print(hangman_art.logo)
display = []
for _ in range(len(word)):
    display += '_'

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if(guess in display):
        print(f"You've already guessed {guess}")
    for position in range(len(word)):
        if(guess == word[position]):
            display[position] = guess
    if(guess not in display):
        lives -= 1
        if(lives == 0):
            end_of_game = True
            print("You lose(")
        
    print(f"{' '.join(display)}")   
    if '_' not in display:
        end_of_game = True
        print("You win")
    
    print(hangman_art.stages[lives])
