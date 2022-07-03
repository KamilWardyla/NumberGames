import random


def guess_the_number_2(big=1000, small=0, guess_number=random.randrange(0, 1000)):
    print("Imagine a number between 0 and 1000!")
    i = 1
    while i < 11:
        if i == 1:
            guess_number = int((big - small) / 2 + small)
        else:
            pass
        print(f"Your number is {guess_number}")
        ans = input("")
        last_number = guess_number
        #print(f"last number: {last_number}")
        #print(f"small number: {small}")
        #print(f"big number: {big}")

        try:
            if ans == "too small":
                if guess_number > small:
                    small = guess_number
                guess_number = random.randint(last_number, big)
                i += 1
            elif ans == "too big":
                if guess_number < big:
                    big = guess_number
                guess_number = random.randint(small, last_number)
                i += 1
            elif ans == "you win":
                return "You win!"
            else:
                raise Exception("""You have entered a wrong value, enter:
too small <- if number is to small
too big <- if number is to big
you win <- if computer guessed the number
                 """)
        except Exception as err:
            print(err)
    return "You lost"


print(guess_the_number_2())