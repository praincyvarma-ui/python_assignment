
"""
Tasks
1.
Create three variables in Python: user_name, fav_app, and daily_usage_hours. Assign your own name, your favorite app
 (like Instagram or Zomato), and how many hours you use it daily.
2.
Write a Python script that declares variables for product_name, price, and is_available to represent an item on Flipkart.
 Print each variable and its data type using the type() function.
3.
Demonstrate the difference between single-line and multi-line comments in Python by writing a script that explains how a Spotify
 playlist recommendation system might work. Use # for single-line and triple quotes for multi-line comments.
4.
Create variables for order_total, delivery_region, and discount_percent to represent a Zomato order. Follow Python naming
 conventions and print a sentence using all three variables, like 'Order from [region] totals ₹[order_total] with 
 [discount_percent]% discount.'
5.
Write a Python script that intentionally mixes tabs and spaces for indentation, then fix the script so it runs without
 errors.<br><br><em><strong>Hint:</strong> Use only spaces for indentation, as per Python's best practices.</em>

"""
# task .1  mai three variable banana hai

"""user_name = "Praincy"
fav_app = "Instagram"
daily_usage_hours = 3

print("Name:", user_name)
print("Favorite App:", fav_app)
print("Daily Usage Hours:", daily_usage_hours)"""

# task .2  product variable and data type
"""
product_name = "laptop"
price = 60000
is_available = True

print(product_name)
print(type(product_name))

print(price)
print(type(price))

print(is_available)
print(type(is_available))"""

# task .3  single line comment and multiline comment


#1 single line comment ke liye #  execute karna
#2 milti line comment ke liye """ ,""" 

# Spotify recommends songs based on your listening history.  

"""
Spotify recommendation system can analyze:
1. Songs you listen to
2. Artists you like
3. Your playlists
4. Your listening history

Based on this information, Spotify recommends
songs that you may like.
"""    

# task .4 zomato order , variable and string formatting
"""
order_price = 5000
delivery_region = "Ahmedabad"
discount_percentage = 10


print(f"order from {delivery_region} total {order_price} with {discount_percentage}% discount.")"""

# task .5  tabs and spaces in indentation
"""
# wrong Code tabs + spaces.

name = "Praincy"

if name == "Praincy":
    print("Hello Praincy")
	print("Welcome to Python")

#right code only use spaces.

name = "praincy"

if name == "praincy":
    print("hello praincy")
    print("welcome python")"""