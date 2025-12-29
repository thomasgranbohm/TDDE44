import random

def dice_rolls_until(sides, target):
    rolls = []
    s = 0 

    while s < target:
        a = random.randint(1, sides)
        s += a
        rolls.append(s)

    return rolls

def count_pairs(values):
    if len(values) <= 1:
        return 0
    
    pairs = 0
    for i in range(1, len(values)):
        if values[i] == values[i - 1]:
            pairs += 1
    
    return pairs
