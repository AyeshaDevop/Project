import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Roll results: Die 1 = {die1}, Die 2 = {die2}, Total = {total}")

def main():

    print("Simulating rolling two dice three times:")
    roll_dice()
    roll_dice()
    roll_dice()

if __name__ == '__main__':
    main()
