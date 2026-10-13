# Task--1 math module

"""import math

number = 25
factorial_number = 5

print("squre root:",math.sqrt(number))
print("factorial :",math.factorial(factorial_number))
print("value of pi:",math.pi)"""

# Task--2 os module

"""import os

files = os.listdir()
print("image files:")

for file in files:
    if file.lower().endswith(".jpg") or file.lower().endswith(".png"):
        print(files)"""

# Task--3 datetime module
"""import datetime

date_input = input("Enter date (YYYY-MM-DD): ")

date_object = datetime.datetime.strptime(date_input, "%Y-%m-%d")

day = date_object.strftime("%A")

print("Day:", day)"""

# Task--4 

"""def format_follower_count(n):
    if n >= 1000000:
        return f"{n / 1000000:.1f}M"
    elif n >= 1000:
        return f"{n / 1000:.1f}K"
    else:
        return str(n)


from insta_utils import format_follower_count

followers = [1500, 2300000, 8500]

for count in followers:
    print(format_follower_count(count))"""

# Task--5

"""import statistics

numbers = [10, 20, 30, 40, 50]

average = statistics.mean(numbers)

print("Numbers:", numbers)
print("Average:", average)"""
