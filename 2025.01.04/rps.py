from random import randint

def parseInput(_input: str) -> int:
    rock = ["0", "ko","kő", "rock"]
    paper = ["1", "papir", "papír", "paper"]
    scissors = ["2", "ollo", "olló", "scissors"]
    _input = _input.lower()

    if _input in rock:
        return 0
    elif _input in paper:
        return 1
    elif _input in scissors:
        return 2
    else:
        return -1

def getWinner(_machine: int, _human: int) -> int:
    if _machine == _human:
        return -1
    # Define a win map where a key beats its value
    win_map = {
        0: 1,  # rock beats scissors
        1: 2,  # paper beats rock
        2: 0   # scissors beats paper
    }
    return 1 if win_map[_machine] == _human else 0


def gameloop() -> None:
    machine_choice = randint(0, 2)
    human_choice = -1
    while human_choice == -1:
        human_choice = parseInput(input("Kő, papír vagy olló?: "))

    match getWinner(machine_choice, human_choice):
        case -1:
            print("Döntetlen!")
        case 0:
            print("Gép nyert!")
        case 1:
            print("Ember nyert!")
    
    if input("Szeretnél új játékot indítani?(y/n): ").lower() in ["y", "yes", "yeah", "ye", ""]:
        gameloop()
    else:
        print("Rendben! Kilépés..")


if __name__ == "__main__": gameloop()

