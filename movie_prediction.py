import pandas as pd

# Load datasets
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Merge datasets
data = pd.merge(movies, ratings, on="movieId")

print("Movie Data:")
print(data)

print("\nAverage Rating:", data["rating"].mean())
print("Average Box Office:", data["boxOffice"].mean())