# Task--1 use for loop find total order value

"""order_amounts = [120,250,90,310,150]

total = 0

for amount in order_amounts:
    total += amount

print("total order value:",total)"""

# Task --2 while loop  se score check karna 
"""
scores = [45,78,102,34,67,89]

i = 0

while i < len(scores) :
    if scores[i] > 100 :
        break
    print(scores[i])
    i += 1"""

# Task --3 continue se below 200 prices skip karna

"""
item_prices = [299, 499, 199, 999, 149]

total = 0

for price in item_prices:
    if price < 200:
        continue

    total += price

print("Total:", total)"""

# Task -- 4 enumerate () se song posision print karna
"""
songs = ["Kesariya", "Believer", "Shape of You", "Blinding Lights", "Excuses"]

for position, song in enumerate(songs, start=1):
    print(position, song)"""

# Task -- 5 Followers ko Category mein Divide Karna

followers = [120, 1500, 23000, 800, 45000]

for count in followers:
    if count < 1000:
        print("Micro")
    elif count <= 10000:
        print("Influencer")
    else:
        print("Celebrity")