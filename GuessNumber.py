import random

def Prompt():
    prompt = input("Difficulty Level? (Type ? for a list of answers)").lower()
    a = 0
    b = 0
    x = 0
    if prompt == "?":
        print("Acceptable answers: Easy, Normal, Hard, Extreme, ?")
        Prompt()
    elif prompt == "easy":
        a = 0
        b = 100
        Game(a, b, x)
    elif prompt == "normal":
        a = 0
        b = 1000
        Game(a, b, x)
    elif prompt == "hard":
        a = 0
        b = 10000
        Game(a, b, x)
    elif prompt == "extreme":
        a = 0
        b = 1000000
        Game(a, b, x)
    else:
        print("That Is Not A Valid Answer. Please Provide A Valid Answer. (Type ? for a list of answers)")
        Prompt()

def PA():
    PA = input("Play Again? (Y/N)").lower()
    if PA == "y":
        Prompt()
    elif PA == "n":
        return
    else:
        print("Invalid Answer, Please Answer With Y or N")
        PA()

def Game(a, b, x):
    answer = random.randint(a, b)
    Guess(a, b, answer, x)

def Guess(a, b, answer, x):
    guess = input(f"Guess A Number Between {a} and {b}:")
    if not guess.isdigit():
        print("That Is Not A Valid Answer. Please Provide A Valid Answer.")
        Guess(a, b, answer, x)
    elif int(guess) > answer:
        print("Too High")
        x += 1
        Guess(a, b, answer, x)
    elif int(guess) < answer:
        print("Too Low")
        x += 1
        Guess(a, b, answer, x)
    else:
        x += 1
        print(f"Congratulations! You Got It! The Answer Was {answer}!")
        print(f"It Took You {x} Guesses!")
        PA()

Prompt()