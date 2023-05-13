import random
import string
import os
import nltk
from nltk.corpus import wordnet
from nltk.corpus import words
words = words.words()

def NewLine():
    for i in range(50):
        print()

def Game():
    YN = input("Do You Want To Play Hangman? (Y/N)").lower()
    if YN == "y":
        Score = 0
        Total = 0
        size = ""
        answer = random.choice(words).lower()
        length = len(answer)
        chars = ["-" for _ in range(length)]
        letters = list(answer)
        for i in range(length):
            size += chars[i]
        guesses = []
        Start(length, size, answer, chars, letters, guesses, Score, Total, wordnet)
    else:
        print("Cya Next Time")
              
def PlayAgain():
    Score = 0
    Total = 0
    size = ""
    answer = random.choice(words).lower()
    length = len(answer)
    chars = ["-" for _ in range(length)]
    letters = list(answer)
    for i in range(length):
        size += chars[i]
    guesses = []
    Start(length, size, answer, chars, letters, guesses, Score, Total, wordnet)
    
def Guess(length, size, answer, chars, letters, guesses, Score, Total, wordnet):
    print(f"Word: {size}")
    print(f"Guesses: {guesses}")
    guessed_letter = input("What Is Your Guess?").lower()
    if guessed_letter in string.ascii_lowercase:
        if guessed_letter == " " or guessed_letter == "":
            NewLine()
            print("Invalid Response")
            Guess(length, size, answer, chars, letters, guesses, Score, Total, wordnet)
        else:
            if guessed_letter in guesses:
                NewLine()
                print("You already guessed that letter!")
                Guess(length, size, answer, chars, letters, guesses, Score, Total, wordnet)
            else:
                guesses.append(guessed_letter)
                if guessed_letter in letters:
                    for i in range(length):
                        if guessed_letter == letters[i]:
                            chars[i] = guessed_letter
                    size = "".join(chars)
                    NewLine()
                    print(f"Correct! {guessed_letter} is in the word.")
                    Total = int(Total) + 1
                else:
                    NewLine()
                    print(f"Sorry, {guessed_letter} is not in the word.")
                    Score = int(Score) + 1
                    Total = int(Total) + 1
                if "-" not in chars:
                    print(f"You have guessed the word, {size} correctly!")
                    print(f"Your score was {Score} points.")
                    print(f"You guessed {Total} letters.")
                    synsets = wordnet.synsets(answer)
                    if synsets:
                        first = synsets[0]
                        definition = first.definition()
                        print(f"Definition:{definition}")
                    else:
                        print("No definition found")
                    play = input("Play Again? (Y/N)").lower()
                    if play == "y":
                        PlayAgain()
                    else:
                        NewLine()
                        print("Cya Next Time")
                else:
                    Guess(length, size, answer, chars, letters, guesses, Score, Total, wordnet)
    elif guessed_letter == "debug":
        NewLine()
        print(f"DEBUG: The Answer Is '{answer}'")
        Guess(length, size, answer, chars, letters, guesses, Score, Total, wordnet)
    else:
        NewLine()
        print("Invalid Response")
        Guess(length, size, answer, chars, letters, guesses, Score, Total, wordnet)
def Start(length, size, answer, chars, letters, guesses, Score, Total, wordnet):
    NewLine()
    print(f"Word is {length} letters")
    Guess(length, size, answer, chars, letters, guesses, Score, Total, wordnet)
        
Game()
