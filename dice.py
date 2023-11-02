import random

# Roll the dice
def roll_dice():
    return random.randint(1, 6)

# Roll the dice and print the result
result = roll_dice()
print(f"You rolled a {result}")
