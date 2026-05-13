# import modules 

import random 
import math
import statistics

# starting variables 

vals_1_100   = range(1,100)
vals_sample  = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius       = random.randint(3,10)
pi           = math.pi

# Calculations for subset (75 samples)

sum_sample    = sum(vals_sample)
avg_sample    = statistics.mean(vals_sample)
median_sample = statistics.median(vals_sample)

# Calculations for superset (200 choices)

avg_choices    = statistics.mean(vals_choices)
median_choices = statistics.median(vals_choices)
mode_choices   = statistics.mode(vals_choices)
stdev_choices  = statistics.stdev(vals_choices)
var_choices    = statistics.variance(vals_choices)

# Circle calculations — area = pi * radius squared

area       = pi * (radius ** 2)
area_ceil  = math.ceil(area)
area_floor = math.floor(area)

# Print results

print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sum_sample}")
print(f"Average of 75 sample values: {avg_sample:.2f}")
print(f"Median of 75 sample values: {median_sample}")

print('\n')

print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {avg_choices:.2f}")
print(f"Median of 200 values: {median_choices}")
print(f"Mode of 200 values: {mode_choices}")
print(f"Standard deviation of 200 values: {stdev_choices:.2f}")
print(f"Variance of 200 values: {var_choices:.2f}")

print('\n')

print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_ceil} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_floor} (rounded down to the nearest integer)")