import random 
import time

print("Welcome to Wordle Unlimited, ● for correct letter, ○ for correct letter in wrong position, - indicates incorrect ")
time.sleep(0.6)
name = input("What is your name? ")
time.sleep(0.5)

lines = open('words.txt', 'r').read().splitlines()

def verification():
    response = input("Would you like to play another round? (yes/no) ").lower()
    return response == "yes" or response == "y"

def display_Letters(guess,word):
    feedback = []
    for i, letter in enumerate(guess):
        if letter == word[i]:
            feedback.append("●")
        elif letter in word:
            feedback.append("○")
        else:
            feedback.append("-")
    return feedback

while True:
    wordl = random.choice(lines).strip().upper()
    attempt = 0
    
    print(f"\nRound {attempt + 1}: Guess a 5-letter word!")
    
    while attempt < 5:
        guess = input(f"Enter a word, {name}: ").strip().upper()
        if len(guess) != 5 or not guess.isalpha():
            print("Invalid Guess. Please enter a 5-letter word.")
            continue
        
        attempt += 1
        feedback = display_Letters(guess, wordl)
        print(" ".join(feedback))
        if feedback == ["●"]*5:
            print("Congratulations! You guessed the word correctly!")
            break
        else:
            print("Incorrect guess. Try again.")
    
    if attempt == 5:
        print(f"Sorry, you were unable to guess the word. The word was: {wordl}")
    
    if not verification():
        print("Thank you for playing! Goodbye.")
        break

    