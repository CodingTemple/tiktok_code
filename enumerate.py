# don't do
video_ideas = ['dance challenge', 'day in the life', 'tutorial']
index = 0
for idea in video_ideas:
    print(f"Idea {index}: {idea}")
    index += 1

# do this
video_ideas = ['dance challenge', 'day in the life', 'tutorial']
for index, idea in enumerate(video_ideas):
    print(f"Idea {index}: {idea}")
