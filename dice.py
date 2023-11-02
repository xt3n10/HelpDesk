from random import randint


# Roll the dice
def roll_dice():
    return randint(1, 20)


# Roll the dice and print the result
result = roll_dice()
print(f"You rolled a {result}")
