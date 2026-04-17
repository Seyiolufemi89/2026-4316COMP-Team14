import matplotlib.pyplot as plt 
import pandas as pd 
#Importing Panda and Matplotlib to Read, organise and maipulate data

#read from the file 
data = pd.read_csv('imdb_top_1000.csv')

#print all columns from the dataset 
print("Dataset Information: ")
print(data.info())
#print the first 5 rows from the data set 
print("\nFirst 5 rows of dataset:")
print(data.head())

#creates the graph figure 
fig, axes = plt.subplots (2, 2, figsize=(14, 10))

#plot 4 : most frequent genres (top 10)
# shows which genres appear most frequently in the top 1000
genres = data['Genre'].value_counts().head(10)
axes[1, 1].barh(genres.index, genres.values, color='purple', alpha=0.7)
axes[1, 1].set_xlabel('Count')
axes[1, 1].set_title('Top 10 movie Genres')
axes[1, 1].grid(axis='x', alpha=0.3)

# plot 1: which genres have the highest average rating (top 10)
avg_rating = data.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(10)
axes[0, 0].bar(avg_rating.index, avg_rating.values, color='skyblue', edgecolor='black')
axes[0, 0].set_ylabel('Average IMDB rating')
axes[0, 0].set_title('Top 10 Genres by average rating')
axes[0, 0].tick_params(axis='x', rotation=45) 

#plot 2: which genres consistently perform better (top 10)
avg_meta = data.groupby('Genre')['Meta_score'].mean().sort_values(ascending=False).head(10)
axes[0, 1].bar(avg_meta.index, avg_meta.values, color='lightgreen', edgecolor='black')
axes[0, 1].set_ylabel('Average Meta Score')
axes[0, 1].set_title('Top 10 Genres by Average Metascore')
axes[0, 1].tick_params(axis='x', rotation=45)

#plot 3: which genres have the highest average revenue (top 10) 
avg_revenue = data.groupby('Genre')['Gross'].mean().sort_values(ascending=False).head(10)
axes[1, 0].bar(avg_revenue.index, avg_revenue.values, color='gold', edgecolor='black')
axes[1, 0].set_ylabel('Average Gross Revenue ($)')
axes[1, 0].set_title('Top 10 Genres by Average Revenue')
axes[1, 0].tick_params(axis='x', rotation=45)


plt.tight_layout()



plt.show()

