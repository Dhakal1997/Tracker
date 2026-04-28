import random, os

name = ["Prince", "Alex", "Robin"]
name_ac = ["crakked a joke", "played with baloons", "joined circus"]
place = [" in kathmandu", "in pokhara", "in bhaktapur"]

print(f"{random.choice(name)} {random.choice(name_ac)} {random.choice(place)}")

with open ("analyis.txt","a") as f:
    f.write(f"{random.choice(name)} {random.choice(name_ac)} {random.choice(place)} \n")
f.close()