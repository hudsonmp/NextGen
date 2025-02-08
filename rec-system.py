import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the ratings data
tags = pd.read_csv('tags.csv')
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
pd.set_option('display.max_columns', None, 'display.max_rows', None)
# Create a histogram of ratings
plt.figure(figsize=(10,6))
sns.histplot(data=ratings, x='rating', bins=10)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
#plt.show()
# Here's a guide to create a dataframe with individual genres:

# 1. First, let's get all unique genres from the movies dataframe
genres = []
for value in movies['genres']:
    # Split each movie's genres and extend the list
    genres.extend(value.split('|'))
    
# 2. Get unique genres to remove duplicates
unique_genres = list(set(genres))
print("Unique genres found:", unique_genres)

# 3. Now you can:
# - Create a new dataframe with columns for each genre
# - Use pd.get_dummies() on the genres column
# - Or count genre frequencies using value_counts()

# First split the genres into separate rows
# Then use get_dummies and join back to original dataframe
genre_dummies = movies['genres'].str.get_dummies(sep='|')
movies = movies.join(genre_dummies)
print(movies.head(10))
# Optional: drop the original genres column if you don't need it anymore
# movies = movies.drop('genres', axis=1)

# Example of counting genre frequencies:
genre_counts = pd.Series(genres).value_counts()
print("\nGenre frequencies:")
print(genre_counts)

# Now you can create visualizations using genre_counts
plt.figure(figsize=(12, 8))
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
plt.title('Genre Frequencies')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.tight_layout()
#plt.show()