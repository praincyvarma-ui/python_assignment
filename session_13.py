#Task--1 recursive function reverse string()

"""def reverse_string(n):
    return str(n)[::-1]
print(reverse_string("hello"))"""

#Task--2 playlist total duration using recursion
"""
def sum_playlist_durations(durations):
    if len(durations)==0:
        return 0
    return durations[0] + sum_playlist_durations(durations[1:])

durations = [120,180,200,150]

print("total durations:",sum_playlist_durations(durations),"second)"""

#Task--3 identify the local and globle function 

"""
count = 10
def update_count():
  count = 5
  print('Inside:', count) # inside :5 ye function ke ander hai isiliye ye local variable hai

update_count()
print('Outside:', count)  # outside:10 ye function ke bahar hai isiliye ye globle variable hai
"""


#Task--4 instagrame post ke total likes using recursion
"""
def count_likes(posts):
    total = posts.get("likes", 0)

    for reply in posts.get("replies", []):
        total += count_likes(reply)

    return total


posts = {
    "likes": 100,
    "replies": [
        {
            "likes": 20,
            "replies": [
                {"likes": 5, "replies": []},
                {"likes": 10, "replies": []}
            ]
        },
        {
            "likes": 30,
            "replies": []
        }
    ]
}

print("Total likes:", count_likes(posts))"""

#Task--5  local variable and globle variable.
"""
app_status ="offline"

def change_status():
    user_status = "online"

    print("inside function:")
    print("user_status:", user_status)
    print("app_status:",app_status)

print("before function call:")
print("app_status:",app_status)

change_status()
print("after function call:")
print("app_status:",app_status)"""