
# Task .1 append() se  playlist id add karna

playlist_ids = [101,102,103,104,105]

playlist_ids.append(106)

print(playlist_ids)

# Task .2  extend() se  shopping card mai items add karna

cart_items = ['t-shirt','shoes']

cart_items.extend(['jeans','cap'])

print(cart_items)

# Task .3 function + pop() se last item remove karna

def remove_last_item(order_list):
    return order_list.pop()

order_list = ['pizza','burger','coke']

remove_items = remove_last_item(order_list)

print("remove_items:",remove_items)
print("update_items:",order_list)

# Task .4 tuple ko update karna.
"""
insta_filters = ("Clarendon", "Juno", "Lark", "Gingham")

insta_filters[1] = 'velencia'

print(insta_filters)"""

# tuple immutable hai isiliye usme update nahi ho sakta hai

# Task . 5  list ya tuple chose karna.

favorite_genres = ["Comedy", "Action", "Romance"]

train_classes = ("Sleeper", "AC 3 Tier", "AC 2 Tier")

print(favorite_genres)
print(train_classes) 