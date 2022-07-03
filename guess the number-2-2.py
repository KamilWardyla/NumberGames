import random


def guess_the_number_2(big=1000, small=0, guess_number=0):
    print("Imagine a number between 0 and 1000!")
    i = 1
    while True:
        if i == 1:
            guess_number = int((big - small) / 2 + small)
        else:
            pass
        print(f"Your number is {guess_number}")
        ans = input("")
        try:
            if ans == "too small":
                small = guess_number
                guess_number = int((big - small) / 2 + small)
                i += 1
            elif ans == "too big":
                big = guess_number
                guess_number = int((big - small) / 2 + small)
                i += 1
            elif ans == "you win":
                return "You win!"
            else:
                raise Exception("""You have entered a wrong value, enter:
too small <- if number is too small
too big <- if number is too big
you win <- if computer guessed the number
                 """)
            if i > 10:
                print("Nie oszukuj!")
                continue
        except Exception as err:
            print(err)


print(guess_the_number_2())