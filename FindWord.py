import random
import string
import os
import nltk
from nltk.corpus import wordnet
from nltk.corpus import words
words = words.words()

def Find():
    prompt = input("Find Word:").lower()
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
        
