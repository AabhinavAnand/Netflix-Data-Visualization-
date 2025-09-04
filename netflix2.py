import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\abhi6\Desktop\netflix_titles.csv")

df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'], inplace=True)

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration'] = movie_df['duration'].str.replace('min', '', regex=False)
movie_df['duration_int'] = movie_df['duration'].astype(int)

type_counts = df['type'].value_counts()
rating_counts = df['rating'].value_counts()
release_count = df['release_year'].value_counts().sort_index()
country_counts = df['country'].value_counts().head(10)
content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

fig, axes = plt.subplots(3, 2, figsize=(16, 18))
fig.suptitle('Netflix Data Visualizations', fontsize=16)

axes[0, 0].bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
axes[0, 0].set_title('Number of Movies vs TV Shows')
axes[0, 0].set_xlabel('Type')
axes[0, 0].set_ylabel('Count')

axes[0, 1].pie(rating_counts.head(6), labels=rating_counts.head(6).index, autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Top 6 Rating Categories')

axes[1, 0].hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')
axes[1, 0].set_title('Distribution of Movie Duration')
axes[1, 0].set_xlabel('Duration (minutes)')
axes[1, 0].set_ylabel('Number of Movies')

axes[1, 1].scatter(release_count.index, release_count.values, color='red')
axes[1, 1].set_title('Content Released by Year')
axes[1, 1].set_xlabel('Release Year')
axes[1, 1].set_ylabel('Count')

axes[2, 0].barh(country_counts.index, country_counts.values, color='teal')
axes[2, 0].set_title('Top 10 Countries by Number of Shows')
axes[2, 0].set_xlabel('Number of Shows')
axes[2, 0].set_ylabel('Country')

axes[2, 1].plot(content_by_year.index, content_by_year['Movie'], color='blue', label='Movie')
axes[2, 1].plot(content_by_year.index, content_by_year['TV Show'], color='orange', label='TV Show')
axes[2, 1].set_title('Movies vs TV Shows Over the Years')
axes[2, 1].set_xlabel('Year')
axes[2, 1].set_ylabel('Number of Releases')
axes[2, 1].legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  
plt.savefig("netflix_all_graphs.png")
plt.show()
