from word_class import word_manager
import random
from zodziai import lietuviski_zodziai
from visual import HANGMANPICS



def symbol_hider(symbol: str) -> None:
    if game.guessing == []:

        indexes = [index for index, letter in enumerate(game.word) if letter == symbol]
        game.symbol_hider()
        game.changing_to_list()
        for index in indexes:
            game.guessing[index] = symbol
        game.back_to_string()
        return game.guessing


    else:
        indexes = [index for index, letter in enumerate(game.word) if letter == symbol]
        game.changing_to_list()
        for index in indexes:
            game.guessing[index] = symbol
        game.back_to_string()
        if game.guessing == game.word:
            print(f"Atspejai! zodis buvo {game.word}")
            game.emptying_guesses()
            menu()
            Guesses = 10

        else:
            return game.guessing


def hangman() -> None:
    Guesses = 10

    while True:
        print(HANGMANPICS[10 - Guesses])
        try:
                guess = str(input("Guess the letter or the entire word  ").capitalize())
        except ValueError:
                print("Please enter a valid input.")
                continue

        if len(guess) > 1 and game.word == guess:
            print("teisingai")
            print(guess)

        elif len(guess) > 1 and game.word != guess:
            Guesses -= 1
            if Guesses == 0:
                print("rip")
                print(HANGMANPICS[10 - Guesses])
                break
            print("Nepataikei")

        if game.guessing == game.word:
            break

        elif len(guess) == 1 and guess in game.word:
            print(HANGMANPICS[10 - Guesses])
            print(f"Atspejai raide:  {symbol_hider(guess)}")

        elif len(guess) == 1 and guess not in game.word:
            Guesses -= 1
            print(HANGMANPICS[10 - Guesses])
            print(f"tokios raides nera: {game.guessing}")
            if Guesses == 0:
                print("rip")
                menu()
                break

            print(f"liko {Guesses} bandymai")


def menu() -> str | None:
    try:
        pasirinkimas = int(input("Hi! What would you like to do?  \n 1. Play \n 2. Quit \n"))
    except ValueError:
        print("Please enter a valid number.")
        menu()

    if pasirinkimas == 1:
        global game
        game = word_manager(random.choice(lietuviski_zodziai))
        hangman()

    elif pasirinkimas == 2:
        print("Bye bye!")
        

    elif pasirinkimas != 1 and pasirinkimas != 2:
        print("Please enter a number between 1 and 2.")
        menu()



menu()
