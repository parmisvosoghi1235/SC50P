from random import randint


def main():
    level = get_level()
    score = 0

    # 10 problems total
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        answer = a + b

        tries = 0
        while tries < 3:
            try:
                user = int(input(f"{a} + {b} = "))
                if user == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{a} + {b} = {answer}")

    print(f"Score: {score}")


def get_level():
    """Prompt user for difficulty level between 1–3"""
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    """Return a random integer for given level"""
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    else:
        return randint(100, 999)


if __name__ == "__main__":
    main()
