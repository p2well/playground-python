import random


def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total


def main():
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")

    player1_roll = roll_dice()
    player2_roll = roll_dice()

    print(player1 + " rolled: " + str(player1_roll))
    print(player2 + " rolled: " + str(player2_roll))

    if player1_roll > player2_roll:
        print(player1 + " wins!")
    elif player2_roll > player1_roll:
        print(player2 + " wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
