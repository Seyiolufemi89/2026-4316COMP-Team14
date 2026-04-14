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

#plot 4 : top 10 genres (Bar chart)
# shows which genres appear most frequently in the top 1000
genres = data['Genre'].value_counts().head(10)
axes[1, 1].barh(genres.index, genres.values, color='purple', alpha=0.7)
axes[1, 1].set_xlabel('Count')
axes[1, 1].set_title('Top 10 movie Genres')
axes[1, 1].grid(axis='x', alpha=0.3)

plt.show()

