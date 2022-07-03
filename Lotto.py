import random


def lotto():
    gamer_numbers = []
    sum_hit_numbers = 0
    lotto_numbers = random.sample(list(range(1, 50)), 6)
    i = 0
    while i < 6:
        try:
            x = int(input("Give ma a number: "))
        except ValueError:
            print("You have entered a wrong value, enter the number between 1 and 49")
            continue
        if x not in range(1, 50):
            print("You have entered number outside the scope, enter the number between 1 and 49")
            continue
        elif x in gamer_numbers:
            print("You have already entered this number before")
            continue
        else:
            gamer_numbers.append(x)
            i += 1
    gamer_numbers = sorted([str(n) for n in gamer_numbers])
    lotto_numbers = [str(n) for n in lotto_numbers]
    str_games_numbers = ",".join(gamer_numbers)
    str_lotto_numbers = ",".join(lotto_numbers)
    print(f"Your numbers are {str_games_numbers}")
    print(f"Number from the draw: {str_lotto_numbers}")
    for number in gamer_numbers:
        if number in lotto_numbers:
            sum_hit_numbers += 1
        else:
            continue
    return f"You guessed {sum_hit_numbers} numbers"


print(lotto())
