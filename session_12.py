# Task--1  lambda function

"""gst_price = lambda price : price * 1.18

print(gst_price(100))
print(gst_price(250))
print(gst_price(500))
"""
"""
Task--2.Given a list of song titles from Spotify with extra spaces and inconsistent casing, use map() and a lambda function 
to clean each title so that it is stripped of spaces and converted to title case (e.g., ' shape OF you ' → 'Shape Of You')"""
"""
songs = [' shape of you ',' perfect ']

spotify_songs = list(map(lambda song : song.strip().title(), songs))

print(spotify_songs)"""  

"""Tsak--3.
Use filter() and a lambda function to extract only those Flipkart product names from a list that start with the letter
 'S' (case-insensitive)."""

"""products = ["airpods","iphone","samsung","saree","sampoo"]

s_product = list(filter(lambda product : product.lower().startswith("s"),products))

print(s_product)"""

"""Task--4.
Given a list of order amounts from a Zomato cart [120, 340, 560, 80], use reduce() from functools to calculate the
total bill amount."""

"""from functools import reduce
amounts = [120,340,560,80]

total_bill =reduce(lambda x,y: x + y,amounts)

print("total_bill:",total_bill)"""



"""5.
Use ChatGPT or Copilot to generate a Python code snippet that uses map(), filter(), and reduce() together to process
a list of numbers: first double each number, then filter to keep only numbers greater than 100, and finally sum the result.
Paste and test the generated code with the list [40, 60, 80, 120]."""

"""from functools import reduce

numbers = [40,60,80,120]

doubled = list(map(lambda x : x * 2,numbers))

filtered = list(filter(lambda x : x > 100,doubled))

total_price = reduce(lambda x,y : x + y ,filtered)

print("doubled:",doubled)
print("filtered:",filtered)
print("total_price:",total_price)"""