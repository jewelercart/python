import statistics

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = file.readlines()
    return [int(num) for num in numbers]

def calculate_mean(numbers):
    return statistics.mean(numbers)

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_mode(numbers):
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        return 'No unique mode found'

def calculate_variance(numbers):
    return statistics.variance(numbers)

def calculate_std_dev(numbers):
    return statistics.stdev(numbers)

def start_statistics_calculator():
    numbers = read_numbers_from_file("mydata.txt")

    print(f"Mean: {calculate_mean(numbers)}")
    print(f"Median: {calculate_median(numbers)}")
    print(f"Mode: {calculate_mode(numbers)}")
    print(f"Variance: {calculate_variance(numbers)}")
    print(f"Standard Deviation: {calculate_std_dev(numbers)}")

start_statistics_calculator()

"""In this version, the read_numbers_from_file function opens the file, reads each 
line, and converts them to integers. The numbers are then passed to the other functions to 
calculate the mean, median, mode, variance, and standard deviation, which are then printed. 
Make sure your mydata.txt file is in the same 
directory as your script, or provide the appropriate path to the file."""