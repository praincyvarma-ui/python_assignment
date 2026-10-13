# Task--1 movies ko iterater aur next se print karo
"""
movies = ["Dhurandhar","Avatar","War 2","Stree 2","Kantara"]

movies_iterater =iter(movies)

print(next(movies_iterater))
print(next(movies_iterater))
print(next(movies_iterater))
print(next(movies_iterater))
print(next(movies_iterater))"""


#Task--2  enumerate()

"""
songs = [ "Kesariya","Tum Hi Ho","Apna Bana Le","Heeriye","Chaleya","Tera Ban Jaunga"]

for position, songs in enumerate(songs , start=1):
    print (f"{position} . {songs}")"""

# Task--3 zip()

"""food_items = ["pizza","burger","sendwich","chocalate",]
prices = [234,456,547,548]

for food, price in zip(food_items,prices):
    print (f'{food}-{price}')"""

#Task--4 generator + yeild() + next


"""def insta_posts_generator(posts):          
    for post in posts:
        yield post

posts = ["new photo upload","wekend vibes","beutifull moment","sunday vibes"]

post_generator = insta_posts_generator(posts)

while True :
    try:
          print(next(post_generator))

    except StopIteration :
           print("all post have been printed")
           break"""

# Task--5 cashback generated

"""def cashback_generator(transactions):
    for amount in transactions:
        cashback = amount * 0.05
        yield cashback

transactions=[240,450,560,670,720]

cashback = cashback_generator(transactions)

for value in cashback:
    print(f'cashback:, {value}')"""

    