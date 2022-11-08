import random

OPERATION = 0
DICE_THROW = 1
DICE_RANGE = 0
Z = 0


class DiceRangeError(Exception):
    pass


def check_dice_equation():
    print("""
x - number of throws 
y - cube type
z - optional modificator
""")
    code = input("Enter cube code, format(xDy+Z): ")
    global OPERATION, DICE_THROW, DICE_RANGE, Z
    index_of_operation = 0
    operation_list = ["+", "-"]
    dice_type = [3, 4, 6, 8, 10, 12, 20, 100]
    Z = 0
    if code.index("D") == 0:
        index_of_d = 0
    else:
        index_of_d = code.index("D")

    for op in code:
        if op in operation_list:
            OPERATION = op
            index_of_operation = code.index(OPERATION)
            Z = code[index_of_operation + 1:]
    if index_of_d != 0:
        DICE_THROW = code[0:index_of_d]
    if OPERATION != 0:
        DICE_RANGE = code[index_of_d + 1:index_of_operation]
    else:
        DICE_RANGE = code[index_of_d + 1:]
    DICE_THROW = int(DICE_THROW)
    DICE_RANGE = int(DICE_RANGE)
    Z = int(Z)
    if DICE_RANGE not in dice_type:
        raise DiceRangeError("There is not such cube")


def dice_game():
    global OPERATION
    throw_types = {"0": throw_dice, "+": lambda: throw_dice() + Z, "-": lambda: throw_dice() - Z}
    while True:
        try:
            check_dice_equation()
            return throw_types[str(OPERATION)]()
        except DiceRangeError:
            print("Enter the correct cube code")


def throw_dice():
    result = 0
    for i in range(0, DICE_THROW):
        result += random.randint(1, DICE_RANGE)
        print(f"Result to: {result}")
    return result


print(dice_game())
