# Task--1  song class banana
"""
class song:

    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration
# Task 2 song ka object banana

songs = song("keshriya","arjit singh",3)
print("song tittle:",songs.title)
print("song artist:",songs.artist)
print("song duration:",songs.duration)"""


# Task--3 play prewiev ()

"""class song:

     def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration

     def play_preview(self):
         print("playing 30-second perview of",self.title ,"by", self.artist, "in", self.duration)
        
songs = song("keshriya","arjit singh",5 )
songs.play_preview()
"""
# Task--4 append 


"""
class Foodorder:

    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_price = self.total_price + price


order1 = Foodorder("Zomato Restaurant")

order1.add_item("Pizza", 250)
order1.add_item("Burger", 150)

print("Restaurant:", order1.restaurant_name)
print("Items:", order1.items)
print("Total Price:", order1.total_price)"""

# Task--5  increment ka function
"""
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.play_count = 0

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")

    def increment_play_count(self):
        self.play_count += 1

song1 = Song("Kesariya", "Arijit Singh", 268)

print("Initial play count:", song1.play_count)

song1.increment_play_count()

song1.increment_play_count()

song1.increment_play_count()

print("Song:", song1.title)
print("Artist:", song1.artist)
print("Play count:", song1.play_count)"""
