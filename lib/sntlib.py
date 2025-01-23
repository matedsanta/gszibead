def HulyebiztosInt(uzenet: str = "Kérlek írj be egy egész számot: "):

    while True:
        bemenet = input(uzenet)
        try:
            int(bemenet)
            break
        except ValueError:
            print("Kérlek egy egész számot adj meg!")
    return int(bemenet)


def HulyebiztosFloat(uzenet: str = "Kérlek írj be egy valós számot: "):

    while True:
        bemenet = input(uzenet)
        try:
            float(bemenet)
            break
        except ValueError:
            print("Kérlek egy valós számot adj meg!")
    return float(bemenet)


def HulyebizrosStr(szamok: bool = False, uzenet: str = "Kérlek írj be egy szöveget: "):

    while True:
        bemenet = input(uzenet)

        if not szamok:
            try:
                for char in bemenet:
                    if not char.lower() in [
                        "a",
                        "á",
                        "b",
                        "c",
                        "d",
                        "e",
                        "é",
                        "f",
                        "g",
                        "h",
                        "i",
                        "í",
                        "j",
                        "k",
                        "l",
                        "m",
                        "n",
                        "o",
                        "ó",
                        "ö",
                        "ő",
                        "p",
                        "q",
                        "r",
                        "s",
                        "t",
                        "u",
                        "ú",
                        "ü",
                        "ű",
                        "v",
                        "w",
                        "x",
                        "y",
                        "z",
                    ]:
                        raise Exception
                break
            except Exception:
                pass
        else:
            try:
                for char in bemenet:
                    if not char.lower() in [
                        "a",
                        "á",
                        "b",
                        "c",
                        "d",
                        "e",
                        "é",
                        "f",
                        "g",
                        "h",
                        "i",
                        "í",
                        "j",
                        "k",
                        "l",
                        "m",
                        "n",
                        "o",
                        "ó",
                        "ö",
                        "ő",
                        "p",
                        "q",
                        "r",
                        "s",
                        "t",
                        "u",
                        "ú",
                        "ü",
                        "ű",
                        "v",
                        "w",
                        "x",
                        "y",
                        "z",
                        "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9",
                    ]:
                        raise Exception
                break
            except Exception:
                pass

    return bemenet


def Fibonacci(n: int):
    print(f"n is {n}, adding {n-1} and {n-2}...")
    if n == 0 or n == 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)


if __name__ == "__main__":

    print(Fibonacci(HulyebiztosInt()))
