import random


def play_2001(computer_points=0, user_points=0):
    while True:
        try:
            cube1 = input("Chose the first cube type(Dy): ")
            cube2 = input("Chose the second cube type(Dy): ")
            dice_type = [3, 4, 6, 8, 10, 12, 20, 100]
            dice_range_cube1 = cube1[1:]
            dice_range_cube1 = int(dice_range_cube1)
            dice_range_cube2 = cube2[1:]
            dice_range_cube2 = int(dice_range_cube2)
            user_dice_range_cube1 = int(dice_range_cube1)
            user_dice_range_cube2 = int(dice_range_cube2)
            computer_range_cube1 = random.choice(dice_type)
            computer_range_cube2 = random.choice(dice_type)
            if dice_range_cube1 and dice_range_cube2 not in dice_type:
                raise Exception("There is not such cube")
        except Exception as e:
            print(e)
            continue
        throw1_computer = random.randint(1, computer_range_cube1)
        print(throw1_computer)
        throw2_computer = random.randint(1, computer_range_cube2)
        print(throw2_computer)
        computer_points += throw1_computer + throw2_computer
        if throw1_computer + throw2_computer == 7:
            computer_points = computer_points / 7
            computer_points = int(computer_points)
            print(f"Computer points : {computer_points}")
        elif throw1_computer + throw2_computer == 11:
            computer_points = computer_points * 11
            print(f"Computer points : {computer_points}")
        else:
            print(f"Computer points : {computer_points}")
        throw1_user = random.randint(1, user_dice_range_cube1)
        throw2_user = random.randint(1, user_dice_range_cube2)
        user_points += throw1_user + throw2_user
        if throw1_user + throw2_user == 7:
            user_points = user_points / 7
            user_points = int(user_points)
            print(f"User points: {user_points}")
        elif throw1_user + throw2_user == 11:
            user_points = user_points * 11
            print(f"User points: {user_points}")
        else:
            print(f"User points: {user_points}")
        if computer_points >= 2001:
            return "Computer Wins"
        elif user_points >= 2001:
            return "User Wins"


print(play_2001())
