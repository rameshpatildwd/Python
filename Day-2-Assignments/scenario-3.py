movies = ("Casablanca", 9.5, "The Godfather", 9.2, "The Shawshank Redemption", 9.3)

# Extract ratings from the tuple
ratings = movies[1::2]

# Calculate the average rating
average_rating = sum(ratings) / len(ratings)

# Print the average rating
print(f"Average rating: {average_rating:.1f}")


# Pair each movie with its rating using zip and convert it to a dictionary
movie_ratings = dict(zip(movies[::2], movies[1::2]))

# Find the movie with the highest rating
highest_rated_movie = max(movie_ratings, key=movie_ratings.get)

print(f"Highest rated movie: {highest_rated_movie}")


#Create a new tuple with only the movie titles: 
movie_titles = tuple(movies[::2])

print("Movie titles:", movie_titles)
