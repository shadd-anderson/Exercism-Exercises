"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == 0:
        return 50 if len(set(dice)) == 1 else 0

    elif category == 1:
        return dice.count(1)

    elif category == 2:
        return dice.count(2) * 2

    elif category == 3:
        return dice.count(3) * 3

    elif category == 4:
        return dice.count(4) * 4

    elif category == 5:
        return dice.count(5) * 5

    elif category == 6:
        return dice.count(6) * 6

    elif category == 7:
        nums = set(dice)
        if len(nums) == 2 and dice.count(nums.pop()) in {2, 3}:
                return sum(dice)
        else:
            return 0

    elif category == 8:
        if dice.count(dice[0]) >= 4:
            return dice[0] * 4
        elif dice.count(dice[1]) == 4:
            return dice[1] * 4
        else:
            return 0

    elif category == 9:
        if {1, 2, 3, 4, 5}.issubset(dice):
            return 30
        else:
            return 0

    elif category == 10:
        if {2, 3, 4, 5, 6}.issubset(dice):
            return 30
        else:
            return 0

    elif category == 11:
        return sum(dice)

    else:
        return 0
