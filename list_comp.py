# Making a new List from an old list?

followers = ["@bellapoarch","Brittany Broski","Noah Beck","@charlidamelio","JoJo Siwa", "@spencerx","@addisonre", "Avani Gregg"]

# Don't do this

# Find Valid followers and add to new list

valid_tiktok_usernames=[]
for follower in followers:
    if "@" in follower:
        valid_tiktok_usernames.append(follower)

print(valid_tiktok_usernames)

# Do This
# Saves Time
valid_tiktok_usernames=[follower for follower in followers if "@" in follower]
print(valid_tiktok_usernames)
