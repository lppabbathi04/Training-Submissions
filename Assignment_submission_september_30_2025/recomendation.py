import numpy as np

# Rows = Users, Columns = Movies
ratings = np.array([
    [5, 4, 0, 3],   # User 1
    [4, 0, 4, 2],   # User 2
    [0, 5, 4, 0]    # User 3
])

# Replace 0s (missing ratings) with user averages
user_avg = np.mean(np.where(ratings != 0, ratings, np.nan), axis=1)
filled = np.where(ratings == 0, user_avg[:, None], ratings)

print(" Original Ratings:\n", ratings)
print("\n Filled Ratings (missing replaced with user avg):\n", np.round(filled, 2))

# Recommend top-rated movie for each user
recommend = np.argmax(filled, axis=1)
print("\n Recommended Movie Index for each user:", recommend)
