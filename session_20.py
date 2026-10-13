"""Tasks
1.
Create a Python class called Product with a private attribute _price. Initialize _price in the constructor and write a
 method to display its value.
2.
Add getter and setter methods for the _price attribute in your Product class to safely access and update the price. Make
 sure the setter prevents setting a negative price.<br><br><em><strong>Hint:</strong> Raise a ValueError if the new price
 is less than zero.</em>
3.
Build a class called Playlist that has a private attribute _songs (a list of song names). Write methods to add a song,
 remove a song, and get the current list of songs using proper encapsulation.
4.
Create an abstract class PaymentMethod with an abstract method pay(amount). Then, create two subclasses: UPI and CreditCard,
each implementing the pay method with a print statement showing how the payment would be processed.<br><br><em><strong>Hint
:</strong> Use the abc module for abstraction.</em>"""

# Task--1  product class  with private _price

"""class product:
    def __init__(self,price):
        self.price = price

    def display_price (self):
        print("product_price:",self.price)

b1= product(500)
b1.display_price()"""

# Task--2 get / set
"""
class product:
    def __init__(self,price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self,price):
        if price < 0:
            raise ValueError("price cannot be nagetive")
        self._price = price
b1 = product(456)

print("current price:",b1.get_price())

b1.set_price(3572)
print("update price:",b1.get_price())"""

# Task--3 playlist class with private _songs.
"""
class playlist:
    def __init__(self):
        self._songs = []

    def add_songs(self,song):
        self._songs.append(song)

    def remove_song(self,song):
        if song in self._songs:
            self._songs.remove(song)
        else:
            print("not found song")

    def get_songs(self):
        return self._songs
     
playlist = playlist()

playlist.add_songs("keshriya")
playlist.add_songs("tum ho to")
playlist.add_songs("bolna")

print("playlist:",playlist.get_songs())

playlist.remove_song("tum ho to")

print("update_songs:",playlist.get_songs())"""

   
# Task--4 abstraction using payment method
"""
from abc import ABC , abstractmethod

class paymentmethod(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class UPI(paymentmethod):
        
    def pay(self,amount):
        print("payment of rupees", amount , "process through UPI")
        
class creditcard(paymentmethod):
        
    def pay(self , amount):
        print("payment of card", amount,"process through cerdit  card")

upi_payment = UPI()
card_payment = creditcard()

upi_payment.pay(500)
card_payment.pay(62562)"""


                                                                                                                                                                                                                 


