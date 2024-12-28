"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""
import random
words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they',"π","µ","∑","ß"]

story =[]
for i in range(1000000):
    x = random.randint(0,23)
    story.append(words[x])
# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))