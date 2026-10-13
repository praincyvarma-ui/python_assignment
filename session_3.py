# Task.1 variable and data type .
"""
followers = 1000
average_rating = 4.5
favorite_app = "instagrame"
is_premium_user = True

print(followers, (type(followers)))
print(average_rating, (type(average_rating)))
print(favorite_app, (type(favorite_app)))
print(is_premium_user, (type(is_premium_user)))"""

# Task . 2  type casting + gst

"""price = input("enter the zomato price")

price=float(price)

gst = price * 18 / 100
final_bill = price + gst

print("original price:", price)
print("gst:", gst)
print("final_bill:", final_bill)"""

# Task . 3   product prices

"""prices = ['199.99','299.50','150']

float_prices = []

for price in prices:
    float_prices.append(float(price))

Total = sum(float_prices)

print("float_prices:", float_prices)
print("total cart value:", Total)"""

# Task . 4 function discount_applicable()

"""def is_discount_applicable(order_amount):
    if order_amount > 500 :
        return True
    else:
        return False

print(is_discount_applicable(450))
print(is_discount_applicable(750))
"""

# Task . 5  spotify rating + float + loop + comprehension

"""ratings = ['4.5','3.0','5','4.2']

float_ratings = []

for rating in ratings:
    float_ratings.append(float(rating))

highest_rating = max(float_ratings)

print("float_rating:",float_ratings)
print("highest_rating:",highest_rating)"""