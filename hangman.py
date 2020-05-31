import random

words = ['apple', 'banana']


def get_word():
    random_word = random.choice(words)
    random_word = list(random_word.upper())
    return random_word


def draw_hangman(tries):
    hangmanpics = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
        /   |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''']

    print(hangmanpics[tries])


game_word = get_word()
guessed_word = ['_'] * len(game_word)

tries = 0


# Some Information About game
print("\n")
print("Welcome to python hangman game")
print("=" * 100)
draw_hangman(6)

# Initial Game world
print("Guess this letter: ",  " ".join(guessed_word), "\n")

while True:
    print("")
    # Ask for userinput
    guess = input("Guess the letter of a word: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("\n Invalid Character Try again")
        continue

    if guess not in game_word:
        print("\nIncorrect guess")
        draw_hangman(tries)
        tries = tries + 1

        if tries > 6:
            print("You lost the game")
            break

    elif guess in game_word:
        if guess in guessed_word:
            print("\n Already Guessed try another")
            continue
        elif guess not in guessed_word:
            print("\n Good Job!")
            for index, letter in enumerate(game_word):
                if letter == guess:
                    guessed_word[index] = letter

            print("Game Progress: ",  " ".join(guessed_word), "\n")

            if guessed_word == game_word:
                print("You Won the game!!")
                break
