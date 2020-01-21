"""
This repo explores an implementation of a basic dice roller using functional
programming dynamics.

Arguably, the randomness of this repository violates the predictability aspect
of functional programming. However, it can also be said that the functions
are still predictable within a certain range.

The documentation below uses the dice notation from various roleplaying games
(RPGs). Dice notation is as follows:

    ndx+m

Where n is the number of dice being rolled, x is the number of sides on each
die, and m is a modifier added to the total of the dice. For instance, 2d6+4
means that 2 dice with 6 sides (a standard die) will be rolled and 4 added to
the resulting sum of the dice; the final value will vary from 6 (1 + 1 + 4) to
16 (6 + 6 + 4).
"""

import random
import re

def parse_die_input(x):
    return re.match("(\d*)d(\d+)([\+\-]?\d*)", x).group(1, 2, 3)

def compare_to_target_number(x):
    return n >= x

def classify_result(x):
    def classify(die_result, modified):
        result = 2 + critical_adjustment(die_result)
        if compare_to_target_number(x)(modified):
            result -= 1

        return (
            "Critical success", "Success", "Failure", "Critical failure"
        )[result]

    return classify

def critical_adjustment(x):
    if x == 20:
        modifier = -1
    elif x == 1:
        modifier = 1
    else: modifier = 0

    return modifier

def main():
    die = parse_die_input(input("What is the dice code?"))
    num, sides, mod = map(int, die)
    status = input(
        "Do you have advantage or disadvantage?\n"
        "Please enter 'a', 'd', or 'n'.\n>"
    ).lower()

    result = 0

    if status in ("a", "advantage"):
        result = advantage(roll_with_modifier(num, roll_die(sides), mod))
    elif status in ("d", "disadvantage"):
        result = disadvantage(roll_with_modifier(num, roll_die(sides), mod))
    else: result = roll_with_modifier(num, roll_die(sides), mod)()

    print(result)

    return

if __name__ == "__main__":
    main()
