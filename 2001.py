import random

def salon_gier(computer_points=0, user_points=0):
    while True:
        enter = input("Press enter to roll a dice")
        throw1_computer = random.randint(1, 6)
        print(throw1_computer)
        throw2_computer = random.randint(1, 6)
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
        throw1_user = random.randint(1, 6)
        throw2_user = random.randint(1, 6)
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


print(salon_gier())