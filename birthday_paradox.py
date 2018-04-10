"""
Solution to the birthday paradox (assuming iid birthdays and simplifying to
365 days) by simulation
"""
from random import randint
from collections import Counter
from math import sqrt


def find_double():
    """Returns the number of people when a birthday double first occurs"""
    number_people = 0
    birthdays = set()
    no_double = True
    MAX_NO_DOUBLE = 100 # prevent runaway simulation
    
    while no_double and number_people < MAX_NO_DOUBLE:
        number_people += 1
        date = randint(1, 365)
        if date in birthdays:
            no_double = False
        else:
            birthdays.add(date)
            
    return number_people

def get_moe(numbers):
    """Returns the confidence interval at 95th percentile of a Poisson

    numbers: iterable of count occurrences
    """
    n = len(numbers)
    L = sum(numbers) / n
    margin_of_error = 1.96 * sqrt(L/n)
    return margin_of_error

def find_better_than_even():
    """Returns the number of people when a likelihood of >50% first occurs
    """
    successes = Counter()
    attempts = Counter()
    max_prob = 0
    iters = 0

    while (1 - max_prob) > .5 and iters < 1000: # prevent runaway simulation
        attempt = [str(find_double())]
        successes.update(attempt)
        attempts.update([str(x) for x in range(int(attempt[0])+1)])

        index, cnt = successes.most_common(1)[0]
        seen = attempts[index]
        if seen > 1:
            prob = cnt / attempts[index]
            
            if prob > max_prob:
                max_prob = prob
        iters += 1
        
    return index, iters

def run_simulation():
    """Returns the number of people needed to have >50% chance of doubled bday
    """
    threshold = .1
    obs = []
    not_confident = True
    while not_confident:
        idx, iters = find_better_than_even()
        obs.append(int(idx))
        if len(obs) % 100 == 0:
            print('Observed better than not chance at {idx} people. MOE: {moe}'.format(idx=idx, moe = get_moe(obs)))
        if get_moe(obs) < threshold:
            not_confident = False
    runs = len(obs)
    mean = sum(obs) / runs
    print('Simulation finished after {runs} runs: {mean} people are needed'.format(runs=runs, mean=mean))
    return mean

if __name__ == "__main__":
    run_simulation()

