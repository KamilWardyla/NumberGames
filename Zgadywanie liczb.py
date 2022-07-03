import random


def guess_the_number():
    while True:
        y = random.randrange(1, 100)
        #print(y)
        try:
            n = int(input("Guess the number: "))
        except ValueError:
            print("It's not a number!")
            continue
        if n < y:
            print("Too small!")
        elif n > y:
            print("Too big!")
        elif n == y:
            return "You win!"


print(guess_the_number())