from random import choice

words = [
    "Dive",
    "Leaf",
    "Glow",
    "Hunt",
    "Calm",
    "Brick",
    "Frost",
    "Maple",
    "Swing",
    "Grain",
    "Lantern",
    "Thunder",
    "Diamond",
    "Journal",
    "Victory",
    "Cascade",
    "Treasure",
    "Sunlight",
    "Frontier",
    "Mountain",
    "Embrace",
    "Backpack",
    "Headlamp",
    "Painting",
    "Marshland",
    "Adventure",
    "Waterfall",
    "Crossword",
    "Playground",
    "Starburst",
]

lives: int = 0
solved: list = []
word: str = ""


def init_game() -> None:
    global word, solved, lives
    word = choice(words).lower()
    lives = 6
    solved = ["_" for f in range(len(word))]


def print_solved() -> str:
    string = ""
    for c in solved:
        string += c
    return string


def game() -> None:
    global word, solved, lives
    while "_" in solved and lives > 0:
        has_found = False
        guess = input("Írd be a tipped:")
        for i in range(len(word)):
            if guess == word[i]:
                solved[i] = guess
                has_found = True
        if has_found:
            print(f"{guess} was in the word! So far you have {print_solved()}")
        else:
            lives -= 1
            print(
                f"{guess} was not in the word! You have {lives} lives left. So far you have {print_solved()}"
            )
    else:
        if "_" not in solved:
            print(f'Congratulations! You have guessed the word "{print_solved()}!"')
        elif lives == 0:
            print(f'Sorry, you lost. The word was "{word}"')

        answer = "whatever"
        while not answer in ["", "y", "n"]:
            answer = input(
                "Would you like to play another round?(Yes: y No: n or press enter)"
            )
        if answer == "y":
            init_game()
            game()
        else:
            pass


if __name__ == "__main__":
    init_game()
    game()
