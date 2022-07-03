import random


def dice_game():
    code = input("Podaj ciąg znaków opisujący rzut, format(xDy+z): ")
    global index_d
    index_d = 0
    global index_operation
    index_operation = 0
    operation_list = ["+", "-"]
    global operation
    operation = 0
    global dice_throw
    dice_throw = 1
    global dice_range
    dice_range = 0
    global z
    z = 0
    i = 0
    global result
    result = 0
    if code.index("D") == 0:
        index_d = 0
    else:
        index_d = code.index("D")
    for op in code:
        if op in operation_list:
            operation = op
            index_operation = code.index(operation)
            z = code[index_operation + 1:]
        else:
            pass
    if index_d == 0:
        pass
    else:
        dice_throw = code[0:index_d]
    if operation != 0:
        dice_range = code[index_d + 1:index_operation]
    else:
        dice_range = code[index_d + 1:]
    dice_throw = int(dice_throw)
    dice_range = int(dice_range)
    z = int(z)

    # Obliczenia
    if operation == 0:
        for i in range(0, dice_throw):
            result += random.randint(1, dice_range + 1)
            print(f"Result to: {result}")
            i += 1
        return result
    elif operation == "+":
        for i in range(0, dice_throw):
            result += random.randint(1, dice_range + 1)
            print(f"Result to: {result}")
            i += 1
        return result + z
    elif operation == "-":
        for i in range(0, dice_throw):
            result += random.randint(1, dice_range + 1)
            print(f"Result to: {result}")
            i += 1
        return result - z


print(dice_game())
