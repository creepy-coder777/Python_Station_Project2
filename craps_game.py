import random

print("""
=============Welcome to the Game of Craps!===========
Instructions:
 - Roll two dice.
 - If the sum is 7 or 11 → You win immediately.
 - If the sum is 2, 3, or 12 → Casino wins immediately.
 - If the sum is 4, 5, 6, 8, 9, or 10 → That number becomes your goal.
   Keep rolling until you hit the goal again to win.
   But if you roll a 7 first, you lose.
""")

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"The sum of dice is {die1} + {die2} = {die1 + die2}")
    return die1 + die2

first_roll = roll_dice()

if first_roll in [7, 11]:
    print("You won")
elif first_roll in [2, 3, 12]:
    print("You lose")
else:
    goal = first_roll
    print(f"Now your goal number is {goal}")
    while True:
        roll = roll_dice()
        if roll == goal:
            print("You win")
            break
        elif roll == 7:
            print("You lose")
            break
print("=============End of the Game!===========")
