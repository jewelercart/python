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

"""This program runs a simulation where it rolls a six-sided die a specific number of 
times for each number of trials in the array. For each trial, it calculates the average roll, 
prints the number of trials, and the average of the rolls. According to the law of large numbers, 
you should see the averages getting closer and closer to the expected value of 3.5 as 
the number of trials increases."""
