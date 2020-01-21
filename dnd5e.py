def roll_with_advantage(roll_func):
    """
    advantage() rolls two dice and implements a conditional test to return
    the higher value.

    Parameters:
        roll_func: a function returning an integer
    """
    return max(roll_func(), roll_func())

def roll_with_disadvantage(roll_func):
    """
    disadvantage() rolls two dice and implements a conditional test to return
    the lower value.

    Parameters:
        roll_func: a function returning an integer
    """
    return min(roll_func(), roll_func())
