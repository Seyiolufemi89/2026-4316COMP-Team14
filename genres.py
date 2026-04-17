import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

# read file with error handling
try:
      data = pd.read_csv('imdb_top_1000.csv')
except FileNotFoundError:
    print("Error: imdb_top_1000.csv not found in this folder!")
    exit()

print("Dataset info: ")
print(data.info())
print("\nFirst 5 rows of dataset:")
print(data.head())

#numeric columns 
data['IMDB_Rating'] = pd.to_numeric(data['IMDB_Rating'], errors='coerce').replace([np.inf, -np.inf], np.nan)
data['Meta_score'] = pd.to_numeric(data['Meta_score'], errors='coerce').replace([np.inf, -np.inf], np.nan)
data['Gross'] = data['Gross'].astype(str).replace(r'[\$,]', '', regex=True)
data['Gross'] = pd.to_numeric(data['Gross'], errors='coerce').replace([np.inf, -np.inf], np.nan)

# creates base of graph figures 
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

#Plot 1: which genres have the highest average rating (top 10)
avg_rating = data.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(10)
axes[0, 0].bar(avg_rating.index, avg_rating.values, color='pink', edgecolor='black')
axes[0, 0].set_ylabel('Average IMDB rating')
axes[0, 0].set_title('Top 10 Genres by average rating')
axes[0, 0].tick_params(axis='x', rotation=45) 

# Plot 2: which genres consistently perform better (top 10)
avg_meta = data.groupby('Genre')['Meta_score'].mean().sort_values(ascending=False).head(10)
axes[0, 1].bar(avg_meta.index, avg_meta.values, color='pink', edgecolor='black')
axes[0, 1].set_ylabel('Average Meta Score')
axes[0, 1].set_title('Top 10 Genres by Average Metascore')
axes[0, 1].tick_params(axis='x', rotation=45)

# Plot 3: which genres have the highest average revenue (top 10) 
avg_revenue = data.groupby('Genre')['Gross'].mean().sort_values(ascending=False).head(10)
axes[1, 0].bar(avg_revenue.index, avg_revenue.values, color='pink', edgecolor='black')
axes[1, 0].set_ylabel('Average Gross Revenue ($)')
axes[1, 0].set_title('Top 10 Genres by Average Revenue')
axes[1, 0].tick_params(axis='x', rotation=45)

#Plot 4: most frequent genres (top 10)
genres = data['Genre'].value_counts().head(10)
axes[1, 1].barh(genres.index, genres.values, color='pink', edgecolor = 'black', alpha=0.9)
axes[1, 1].set_xlabel('Count')
axes[1, 1].set_title('Top 10 movie Genres')
axes[1, 1].grid(axis='x', alpha=0.3)

plt.tight_layout()

plt.show()

