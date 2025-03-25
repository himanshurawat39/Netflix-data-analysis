import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Dataset
df = pd.read_csv("data/netflix_titles.csv")

# Display basic info
print("Dataset Overview:")
print(df.info())
print(df.head())

# Handle missing values
df.dropna(inplace=True)  # Removing rows with missing values

# Count of Movies vs TV Shows
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='type', palette='coolwarm')
plt.title("Count of Movies vs TV Shows")
plt.show()

# Trend of Content Release Over the Years
plt.figure(figsize=(10, 5))
df['release_year'].value_counts().sort_index().plot(kind='line', color='red')
plt.title("Trend of Netflix Content Release Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Releases")
plt.show()

# Most Common Genres
genres = ', '.join(df['listed_in'].dropna()).split(', ')
genre_counts = pd.Series(genres).value_counts().nlargest(10)
plt.figure(figsize=(8, 4))
genre_counts.plot(kind='bar', color='green')
plt.title("Top 10 Most Common Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Country-wise Distribution of Content
plt.figure(figsize=(10, 5))
df['country'].value_counts().nlargest(10).plot(kind='bar', color='purple')
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Save cleaned dataset
df.to_csv("data/netflix_cleaned.csv", index=False)

print("\nAnalysis Completed! The cleaned dataset is saved in 'data/netflix_cleaned.csv'")
