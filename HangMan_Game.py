import random

words = ["apple","mango","banana","orange","grapes","papaya"]
word = random.choice(words)
guessed = []
wrong_guesses = 0
max_attempts = 6
hangman = [
    """

     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    
"""
]
print("Welcome to HangMan Game")
print("Hint: It is fruit.")

while wrong_guesses < max_attempts:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else: display += "_"

    print(hangman[wrong_guesses])
    print("Word: ", display)

    if "_" not in display:
        print("Congratulation! You have Won!")
        print("The Fruit was : ", word)
        break
    guess = input("guess tht letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue
    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(hangman[wrong_guesses])
    print("Game Over!")
    print("The fruit was:", word)