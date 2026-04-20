import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('imdb_top_1000.csv')

df['Gross'] = df['Gross'].str.replace(',', '').astype(float)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('IMDb Director Analysis')

# Question 1 - Which director appears the most in the top 1000?
director_counts = df['Director'].value_counts()
top_directors = director_counts.head(10)

axes[0, 0].bar(top_directors.index, top_directors.values)
axes[0, 0].set_title('Directors with most films')
axes[0, 0].set_xlabel('Director')
axes[0, 0].set_ylabel('Number of films')
axes[0, 0].tick_params(axis='x', rotation=45)

# Question 2 - Which director has the highest average rating with at least 3 films in the top 1000?
avg_ratings = df.groupby('Director')['IMDB_Rating'].mean()
film_counts = df.groupby('Director')['IMDB_Rating'].count()
directors_3plus = film_counts[film_counts >= 3].index
avg_ratings_filtered = avg_ratings[directors_3plus]
top_ratings = avg_ratings_filtered.sort_values(ascending=False).head(10)

axes[0, 1].bar(top_ratings.index, top_ratings.values)
axes[0, 1].set_title('Highest average rating (min 3 films)')
axes[0, 1].set_xlabel('Director')
axes[0, 1].set_ylabel('Average rating')
axes[0, 1].set_ylim(8, top_ratings.values.max() + 0.1)
axes[0, 1].tick_params(axis='x', rotation=45)

# Question 3 - Which director has highest average revenue in the top 1000?
avg_revenue = df.groupby('Director')['Gross'].mean()
top_revenue = avg_revenue.sort_values(ascending=False).head(10)

axes[1, 0].bar(top_revenue.index, top_revenue / 1000000)
axes[1, 0].set_title('Highest average revenue')
axes[1, 0].set_xlabel('Director')
axes[1, 0].set_ylabel('Average gross (millions $)')
axes[1, 0].tick_params(axis='x', rotation=45)

# Question 4 - Which directors get higher ratings in the top 1000?
top5_directors = director_counts.head(5).index

for director in top5_directors:
    ratings = df[df['Director'] == director]['IMDB_Rating']
    axes[1, 1].scatter([director] * len(ratings), ratings)

axes[1, 1].set_title('Ratings per director')
axes[1, 1].set_xlabel('Director')
axes[1, 1].set_ylabel('IMDb Rating')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()