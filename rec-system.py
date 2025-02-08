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
plt.show()

print(movies.head(10))