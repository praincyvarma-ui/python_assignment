# Task--1 product and electronics

"""class Product:
    def get_discount(self):
        return 0


class Electronics(Product):
    def get_discount(self):
        return 10



product = Product()
electronics = Electronics()

print("Product Discount:", product.get_discount())
print("Electronics Discount:", electronics.get_discount())"""


# Task--2  foodorder aur zomatoorder

"""class foodorder:
    def __init__(self,base_price):
         self.base_price = base_price

    def calculate_total(self):
        return self.base_price

class zomatoorder(foodorder):
    def calculate_total(self):
        delivery_charge = self.base_price * 0.05
        return self.base_price + delivery_charge

food_order = foodorder(1500)
zomato_order = zomatoorder(2000)

print("food order total:", food_order.calculate_total())

print("zomato order total:",zomato_order.calculate_total())"""

# Task--3 show_bonus and plymorphism
"""
class influencer:
    def bonus(self):
        return 2000

class brandmanager:
    def bonus(self):
        return 5000

def show_bonus(employee):
    print("bonus:",employee.bonus())

Influencer =influencer()
brand_manager= brandmanager()

show_bonus(Influencer)
show_bonus(brand_manager)"""

# Task--4 user and premiumuser

"""class User:
    def get_status(self):
        return "active"


class PremiumUser(User):
    def get_status(self):
        return "premium"


user = User()
premium_user = PremiumUser()

print("User Status:", user.get_status())
print("Premium User Status:", premium_user.get_status())"""

