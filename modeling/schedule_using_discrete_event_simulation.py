from enum import Enum


# decision rule / heuristic rule
class DecisionRule(Enum):
    short_jobs_first = 1  # min (t\ij)
    long_jobs_first = 2  # max (t\ij)
    minimum_reserve_jobs_first = 3  # min (rez\ij)
    belonging_to_entry_levels_jobs_first = 4  # min (lev\ij)


def schedule(workers: int, decision_rule: DecisionRule):
    return "TODO: Implement"


if __name__ == '__main__':
    result = schedule(
        workers=3,
        decision_rule=DecisionRule.long_jobs_first
    )
    print(result)
