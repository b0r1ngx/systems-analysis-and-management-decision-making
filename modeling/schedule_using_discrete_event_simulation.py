from enum import Enum


# decision rule / heuristic rule
class DecisionRule(Enum):
    short_jobs_first = 1  # - «короткие» работы в первую очередь.
    long_jobs_first = 2  # - «длинные» работы в первую очередь.
    minimum_reserve_jobs_first = 3  # работы с минимальным резервом в первую очередь.
    belonging_to_entry_levels_jobs_first = 4  # работы, принадлежащие начальным уровням в первую очередь.


def schedule(workers: int, decision_rule: DecisionRule):
    return "TODO: Implement"


if __name__ == '__main__':
    result = schedule(
        workers=3,
        decision_rule=DecisionRule.long_jobs_first
    )
    print(result)
