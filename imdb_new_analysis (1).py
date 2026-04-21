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

# numeric columns
data['IMDB_Rating'] = pd.to_numeric(data['IMDB_Rating'], errors='coerce').replace([np.inf, -np.inf], np.nan)
data['No_of_Votes'] = pd.to_numeric(data['No_of_Votes'], errors='coerce').replace([np.inf, -np.inf], np.nan)
data = data.dropna(subset=['IMDB_Rating', 'No_of_Votes'])

# creates base of graph figures
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('IMDB Top 1000 — Movie Analysis', fontsize=16, fontweight='bold')

# Plot 1: Top 10 rated movies
top10 = data.nlargest(10, 'IMDB_Rating')[['Series_Title', 'IMDB_Rating']].reset_index(drop=True)
axes[0, 0].barh(top10['Series_Title'][::-1], top10['IMDB_Rating'][::-1], color='green', edgecolor='black')
axes[0, 0].set_xlabel('IMDB Rating')
axes[0, 0].set_title('Top 10 Rated Movies')
axes[0, 0].set_xlim(8, 9.5)
axes[0, 0].grid(axis='x', alpha=0.3)

# Plot 2: Correlation between IMDB ratings and votes
axes[0, 1].scatter(data['IMDB_Rating'], data['No_of_Votes'] / 1e6,
                   color='green', edgecolors='black', alpha=0.6, s=20)
# OLS trend line
m, b = np.polyfit(data['IMDB_Rating'], data['No_of_Votes'] / 1e6, 1)
x_line = np.linspace(data['IMDB_Rating'].min(), data['IMDB_Rating'].max(), 200)
axes[0, 1].plot(x_line, m * x_line + b, color='black', linewidth=1.5, label='Trend line')
corr = data['IMDB_Rating'].corr(data['No_of_Votes'])
axes[0, 1].set_xlabel('IMDB Rating')
axes[0, 1].set_ylabel('Votes (millions)')
axes[0, 1].set_title('Correlation: IMDB Rating vs Votes')
axes[0, 1].legend(fontsize=9)
axes[0, 1].text(0.03, 0.93, f'r = {corr:.3f}', transform=axes[0, 1].transAxes, fontsize=10)
axes[0, 1].grid(alpha=0.3)

# Plot 3: Do higher rated movies receive more votes? (average votes per rating band)
bins = [7.5, 7.9, 8.3, 8.7, 9.4]
labels = ['7.6–7.9', '8.0–8.3', '8.4–8.7', '8.8–9.3']
data['rating_band'] = pd.cut(data['IMDB_Rating'], bins=bins, labels=labels)
avg_votes = data.groupby('rating_band', observed=True)['No_of_Votes'].mean() / 1e6
axes[1, 0].bar(avg_votes.index, avg_votes.values, color='green', edgecolor='black')
axes[1, 0].set_xlabel('Rating Band')
axes[1, 0].set_ylabel('Average Votes (millions)')
axes[1, 0].set_title('Do Higher Rated Movies Get More Votes?')
axes[1, 0].grid(axis='y', alpha=0.3)
for i, v in enumerate(avg_votes.values):
    axes[1, 0].text(i, v + 0.01, f'{v:.2f}M', ha='center', fontsize=9)

# Plot 4: Distribution of ratings
axes[1, 1].hist(data['IMDB_Rating'], bins=20, color='green', edgecolor='black', alpha=0.9)
axes[1, 1].axvline(data['IMDB_Rating'].mean(), color='black', linestyle='--',
                   linewidth=1.5, label=f"Mean: {data['IMDB_Rating'].mean():.2f}")
axes[1, 1].axvline(data['IMDB_Rating'].median(), color='grey', linestyle=':',
                   linewidth=1.5, label=f"Median: {data['IMDB_Rating'].median():.2f}")
axes[1, 1].set_xlabel('IMDB Rating')
axes[1, 1].set_ylabel('Number of Films')
axes[1, 1].set_title('Distribution of Ratings')
axes[1, 1].legend(fontsize=9)
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('imdb_new_analysis.png', dpi=150, bbox_inches='tight')
print("Saved → imdb_new_analysis.png")
plt.show()
