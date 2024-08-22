# don't do this

comments = ["cool", "awesome", "cool", "love it", "awesome", "cool"]
comment_counts = {}
for comment in comments:
    if comment in comment_counts:
        comment_counts[comment] += 1
    else:
        comment_counts[comment] = 1
print(comment_counts)

# do this

from collections import Counter

comments = ["cool", "awesome", "cool", "love it", "awesome", "cool"]
comment_counts = Counter(comments)
print(comment_counts)
