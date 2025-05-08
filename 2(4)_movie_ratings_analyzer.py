"""
✅ Mini Project 1: 🎥 Movie Ratings Analyzer
🎯 Goal:
Process a list of movie ratings (1–5 stars)


Filter out low ratings


Calculate the average of high ratings


🧠 Real-Life Analogy:
Like taking only the best customer reviews and averaging them to decide if a movie is worth watching.

"""

from functools import reduce

ratings = [1, 4, 5, 2, 3, 5, 4]

high_ratings = list(filter(lambda x: x>=4, ratings))
print("High Ratings:", high_ratings)

average = reduce(lambda x,y: x+y, high_ratings)/ len(high_ratings)
print("Average of high ratings:", average)

# Average of high ratings: 4.5
