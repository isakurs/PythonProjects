import random
import string
import os
import nltk
from nltk.corpus import wordnet
from nltk.corpus import words
words = words.words()

def Find():
    prompt = input("Find Word:").lower()
    if prompt == "gay":
        print(f"{prompt} is in the wordlist")
        synsets = wordnet.synsets(prompt)
        if synsets:
            first = synsets[0]
            definition = first.definition()
            print(f"Definition:{definition}")
            print("Example: Sean Brickmeier")
            Find()
        else:
            print("No definition found")
            Find()

    elif prompt == "mistake":
        print(f"{prompt} is in the wordlist")
        synsets = wordnet.synsets(prompt)
        if synsets:
            first = synsets[0]
            definition = first.definition()
            print(f"Definition:{definition}")
            print("Example: Nicholas Bonilla")
            Find()
        else:
            print("No definition found")
            Find()
    elif prompt == "kitten":
        print(f"{prompt} is in the wordlist")
        synsets = wordnet.synsets(prompt)
        if synsets:
            first = synsets[0]
            definition = first.definition()
            print(f"Definition:{definition}")
            print("Example: Isakur Stefansson")
            Find()
        else:
            print("No definition found")
            Find()
    elif prompt == "poor":
        print(f"{prompt} is in the wordlist")
        synsets = wordnet.synsets(prompt)
        if synsets:
            first = synsets[0]
            definition = first.definition()
            print(f"Definition:{definition}")
            print("Example: Victor (Too Poor For A Last Name)")
            Find()
        else:
            print("No definition found")
            Find()
    else:
        if prompt in words:
            print(f"{prompt} is in the wordlist")
            synsets = wordnet.synsets(prompt)
            if synsets:
                first = synsets[0]
                definition = first.definition()
                print(f"Definition:{definition}")
                Find()
            else:
                print("No definition found")
                Find()
        else:
            print("Word not found")
            Find()

Find()
        
