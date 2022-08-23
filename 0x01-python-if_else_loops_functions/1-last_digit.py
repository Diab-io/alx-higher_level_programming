#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last = num_str[-1]
if int(last) == 0:
    print(f"Last digit of {number} is {int(last)} and is 0")
elif int(last) > 5:
    print(f"Last digit of {number} is {int(last)} and is greater than 5")
elif int(last) < 6 and int(last) != 0:
    print(f"Last digit of {number} is {int(last)} and is less than 6 and not 0")