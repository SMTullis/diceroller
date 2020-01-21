import random

def roll_die(sides):
    """
    roll_die() returns a function to simulate rolling a die with n sides.

    Parameters:
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
    rolling n number of dice. 

    Parameters:
        n: integer greater than 0
        die_func: a function returning a single integer

    Example:
        rolldice(5, roll_die(6)) # Simulates rolling 5d6.
    """
    if n <= 1:
        return die_func()

    return die_func() + roll_dice(n - 1, die_func)

def roll_with_modifier(n, die_func, modifier):
    """
    roll_with_modifier() simulates rolling n number of dice and adds an integer
    to the final value. 

    Parameters:
        n: an integer greater than 0
        die_func: function returning a single integer
        modifier: an integer

    Example:
        roll_with_modifier(3, roll_die(8), 3) # Simulates rolling 3d8+3
    """
    def roll():
        return roll_dice(n, die_func) + modifier

    return roll
