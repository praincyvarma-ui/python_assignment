
#Task--1 w mode
"""
with open("my_playlist.txt", 'w') as f:
    f.write("ranjhana. \n")
    f.write("o meri laila. \n")
    f.write("kinna sona. \n")
    f.write("tum ho to. \n")
    f.write("jitni dafa. \n")

    f.close()
print("playlist file created succesfull")

#Task--2  r mode / uppercase

with open("my_playlist.txt", 'r') as f :

    for song in f :
         print(song.strip().upper())

    f.close()"""


#Task--3 w mode/ r mode / csv wining team

"""import csv

with open("ipl_match.csv",'w',newline="") as f:
     writer = csv.writer(f)

     writer.writerow(["match", "team1", "team2", "winner"])

     writer.writerow(["Match 1", "CSK", "MI", "CSK"])
     writer.writerow(["Match 2", "RCB", "KKR", "KKR"])
     writer.writerow(["Match 3", "GT", "RR", "GT"])
     writer.writerow(["Match 4", "DC", "SRH", "SRH"])

     
print("csv file created succesfully")

with open("ipl_match.csv",'r') as f:
      reader = csv.DictReader(f)

      print("winning team:")

      for row in reader:
          print(row["winner"])"""



#Task--4  json file 
'''
import json

user_data ={"user_name": "princy" , "followers": 1500, "bio": "python learner amd data analyst student"}

with open("user_profile.json",'w') as file:
     json.dump(user_data,file, indent=3)

print("user_profile","created succesfull")

with open("user_profile.json",'r') as file:
     user_profile = json.load(file)

print("\nUser_Profile:")
print("User_name:", user_profile["user_name"])
print("Followers:", user_profile["followers"])'''

#Task--5 check zomato order.json is exist or not exist

"""from pathlib import Path

file_path = Path("zomato_orders.json") 

if file_path.exists():
    print("zomato_order.json file is found")
else:
    print("zomato_order.json file is not found")"""