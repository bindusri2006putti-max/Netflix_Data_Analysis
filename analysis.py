import pandas as pd

df = pd.read_csv("netflix_titles.csv/netflix_titles.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

print("\nMovies and TV Shows Count:")
print(df['type'].value_counts())

import matplotlib.pyplot as plt

df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

print("\nTop 10 Countries:")
print(df['country'].value_counts().head(10))

top_countries = df['country'].value_counts().head(10)

top_countries.plot(kind='bar')
plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()
