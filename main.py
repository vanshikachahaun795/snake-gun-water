print("Program Started")

import random


def game_win(user, computer):
    if user == computer:
        return None

    # Snake vs Water
    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False

    # Water vs Gun
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False

    # Gun vs Snake
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False


# Computer chooses randomly
rand_no = random.randint(1, 3)

print("Computer's turn: Snake(s), Water(w), Gun(g)")

if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "w"
else:
    computer = "g"

# User input
user = input("Your turn: Snake(s), Water(w), Gun(g): ").lower()

# Decide winner
result = game_win(user, computer)

print("\nYou chose:", user)
print("Computer chose:", computer)

if result is None:
    print("It's a Draw!")
elif result:
    print("You Win!")
else:
    print("You Lose!")