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

def roll_die(sides):
    """
    roll_die() returns a function to simulate rolling a die with n sides.

    Arguments
    sides: an integer greater than 0.

    Example:
    d10 = roll_die(10)
    d10() # Returns an integer 1 through 10.
    """
    def roll():
        return random.randint(1, sides)

    return roll

def roll_dice(n, die_func):
    """
    roll_dice() is a recursive function returning an integer value to simulate
    rolling n number of dice. The die_func argument provides a

    Arguments:
    n: integer greater than 0
    die_func: a function returning a single integer

    Example:
    rolldice(5, roll_die(76)) # Simulates rolling 5d6.
    """
    if n == 1:
        return die_func()

    return die_func() + roll_dice(n - 1, die_func)

def roll_with_modifier(n, die_func, modifier):
    """
    roll_with_modifier() simulates rolling n number of dice and adds an integer
    to the final value. It returns a function to pass as an argument to other
    functions.

    Arguments:
    n: an integer greater than 0
    die_func: function returning a single integer
    modifier: an integer

    Example:
    roll_with_modifier(3, roll_die(8), 3) # Simulates rolling 3d8+3
    """
    def roll():
        return roll_dice(n, die_func) + modifier

    return roll

def advantage(roll_func):
    """
    advantage() rolls two dice and implements a conditional test to return
    the higher value.

    Arguments:
    roll_func: a function returning an integer
    """
    return use_higher(roll_func(), roll_func())

def disadvantage(roll_func):
    """
    disadvantage() rolls two dice and implements a conditional test to return
    the lower value.

    Arguments:
    roll_func: a function returning an integer
    """
    return use_lower(roll_func(), roll_func())

def use_higher(x, y):
    if x > y:
        return x

    return y

def use_lower(x, y):
    if x < y:
        return x

    return y

def parse_die_input(x):
    return re.match("(\d*)d(\d+)([\+\-]?\d*)", x).group(1, 2, 3)

def main():
    die = parse_die_input(input("What is the dice code?"))
    num, sides, mod = map(die, int)
    status = input(
        "Do you have advantage or disadvantage?\n"
        "Please enter 'a', 'd', or 'n'.\n>"
    ).lower()

    result = 0

    if status in ("a", "advantage"):
        result = advantage(roll_with_modifier(num, roll_die(sides), mod))
    elif status in ("d", "disadvantage"):
        result = disadvantage(roll_with_modifier(num, roll_die(sides), mod))
    else: result = roll_with_modifier(num, roll_die(sides), mod)

    return result
