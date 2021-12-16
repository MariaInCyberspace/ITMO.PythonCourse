from my_modules import random_list_mod as r
from my_modules import random_number_mod as rn
import math as m  # To use the 'fsum' function
import statistics as s  # To calculate mean, median and standard deviation

# Get a list of random integers
my_list = r.get_list_of_random_integers(10)

# Calculate the sum of all the numbers in this list
# And use imported math and statistics modules to calculate the mean, median and standard deviation
print("-" * 50)
print(f"\nHere's a list of random integers:\n\t{my_list}")
print(f"\n\tSum of all the numbers in the list: {m.fsum(my_list)}",
      f"\n\tMean of the listed data is: {s.mean(my_list)}",
      f"\n\tMedian of the listed data is: {s.median(my_list)}",
      f"\n\tStandard deviation: {s.stdev(my_list)} \n")
print("-" * 50)

# Get a random number
print(f"\nThis a random number between 1 and 100: {rn.generate_random_integer(1, 100)}")

print("-" * 50)
