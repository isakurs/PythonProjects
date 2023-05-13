import random
import string
import os
import nltk
from nltk.corpus import wordnet
from nltk.corpus import words

def Run():
    # Create lists of words starting with each letter
    word_lists = {}
    for letter in string.ascii_lowercase:
        word_lists[letter] = [word for word in words.words() if word.startswith(letter)]

    # Prompt the user for an acronym
    acronym = input("Input Acronym: ")

    # Create dictionary for the corresponding words
    words_dict = {}
    for i, letter in enumerate(acronym):
        if letter in word_lists:
            if letter not in words_dict:
                words_dict[letter] = []
            words_dict[letter].append(random.choice(word_lists[letter]))

    # Print the variables
    for i, letter in enumerate(acronym):
        var_name = "pos_" + str(i+1)
        if letter in words_dict:
            print(words_dict[letter].pop(0))
        else:
            print(var_name + ": No word found for letter " + letter)
    Run()

Run()
