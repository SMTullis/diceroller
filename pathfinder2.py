OUTCOMES = ("Critical Success", "Success", "Failure", "Critical Failure")

def classify_result(die, mod, tn):
    """classify_result() determines the outcome of a d20 roll per the Pathfinder second edition ruleset.
    
    parameters:
        die: the result of the d20 die
        mod: the modifier applied to the d20
        tn: the target number
    """
    result = base_result(die + mod, tn)
    natural = nat_adj(die)
    crit = crit_adj(tn - die - mod)

    return OUTCOMES[cap_number(result + natural + crit)]

def base_result(x, tn):
    """base_result() determines whether the total result succeeds or fails.
    
    parameters:
        x: the total result of the d20 die and modifier
        tn: the target number
    """
    base = 1
    if x < tn:
        base = 2

    return base
    
def nat_adj(die):
    """nat_adj() determines if there should be a success modifier for the base result. On a natural 20, the success is upgraded by one tier; on a natural 1, the success is downgraded by one tier.
    
    parameters:
        die: the result of the d20 die
    """
    results = {20: -1, 1: 1}
    return results.get(die, 0)

def critical_adj(diff):
    """critical_adj determines if there should be a critical adjustment to the success value. If the total result exceeds the target number by 10 or more, it is a critical success; if the total result fails by 10 or more, it is a critical failure.
    
    parameters:
        diff: the difference between the total result and the target number
    """
    if diff >= 10:
        modifier = -1
    elif diff <= -10:
        modifier = 1

    return 0 + modifier

def cap_number(x):
    return min(len(OUTCOMES) - 1,  max(0, x))
