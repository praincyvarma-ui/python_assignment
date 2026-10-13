
# Task--1 safe_divide

"""def safe_divide(a, b):
    try:  
        return a / b
    except ZeroDivisionError :
        return "cannot divide by zero"

print(safe_divide(10, 2))
print(safe_divide(20,0))"""


# Task--2 zomato rating system
"""
try:
    reviews = int(input("enter the number of reviews:"))
    stars = int(input("enter total stars:"))

    average_rating = stars / reviews

    print("average rating:",average_rating)

except ValueError:
    print("please enter number only:" )

except ZeroDivisionError:
    print("number of reviews cannot be zero:") """

# Task--3 playlist duration
"""
class invaliddurationError(Exception):
    pass

def get_playlist_duration(songs):
    total_seconds = 0

    for duration in songs:
       if duration < 0 :
           raise invaliddurationError("cannot be nagetive error")

       total_seconds += duration
    return total_seconds/ 60
    
try:
    songs = [ 120,234,256,321,53]
    total = get_playlist_duration(songs)

    print("total playlist duraions:", total, "minutes")

except invaliddurationError as e:
    print("Error",e)
"""

# Task--4  flipkart summary

"""try:
    price = float(input("enter item price:"))
    quantity = int(input("enter the quantity:"))

    total_price = price * quantity
except ValueError:
    print("invalid input:","please enter number only")
else:
    print("total price:",total_price)
finally:
    print("Thank you for shopping")"""

# Task--5  AI- generated division programe
"""
try:
    num1 = float(input("enter the number:"))
    num2 = float(input("enter the number:"))

    result = num1 / num2 
    print("result:",result)
except ValueError:
    print("enter the value number only:")
except ZeroDivisionError:
    print("number is cannot be zero:")

print("\nLearning:")
print("I learned that try-except helps handle errors without crashing the program.")"""