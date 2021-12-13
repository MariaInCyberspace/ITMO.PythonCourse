import math
from PIL import Image
from math import *
import re

count = 0
val = 0.9

for i in range(0, 10000, 1):
    count += 1
    val += 0.1

print(count)
print(0.9 + 10000 * 0.1)
print(val)
print(val == 1000.9)

a = 5
b = 5
a = b

# == (checks if operands' values are equal
print(a == b)

# is (checks if memory addresses are equal
print(a is b)

print("Input your string")
# a, b = map(int, input().split())
print("Input your string")
# c, d = map(str, input().split())


print(2 * 2 ** 3)

test_string = "art123aer234"
result = re.split('\d+', test_string)
print(result)

# help(int)

help(re.split)
