#Step 4

import random
from hangman_art import stages, logo
from hangman_words import word_list


end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
print(logo)

#Create blanks
display = []
wrong_answers = []
for _ in range(word_length):
    display += "_"
stickman_pos = 6
print(display)
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    lose_a_life = True
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        wrong_answers += guess
        stickman_pos -= 1    
    
    print(stages[stickman_pos])
    print(wrong_answers)
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    
    if stickman_pos == 0:
        end_of_game = True
        print(stages[stickman_pos])
        print(display)
        print(f"the word was {chosen_word}")
        print("You Lose")

#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.