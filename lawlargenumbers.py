import random

def roll_dice(n):
    return [random.randint(1, 6) for _ in range(n)]

def verify_law_of_large_numbers(trials):
    expected_value = 3.5
    print("Expected value: " + str(expected_value))
    for trial in trials:
        rolls = roll_dice(trial)
        average = sum(rolls) / len(rolls)
        print("Trials: " + str(trial) + " Trial average: " + str(round(average, 6)))

trials = [100, 1000, 10000, 100000, 500000]
verify_law_of_large_numbers(trials)


