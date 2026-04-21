import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('imdb_top_1000.csv')

df['Gross'] = df['Gross'].str.replace(',', '').astype(float)

while True:
    print("\nWhich question would you like to analyse?")
    print("1. Which director appears the most in the top 1000?")
    print("2. Which director has the highest average rating (min 3 films)?")
    print("3. Which director has the highest average revenue?")
    print("4. Which directors get higher ratings in the top 1000?")
    print("5. Quit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("Exiting...")
        break

    fig, ax = plt.subplots(figsize=(10, 6))

    if choice == "1":
        director_counts = df['Director'].value_counts()
        top_directors = director_counts.head(10)

        ax.bar(top_directors.index, top_directors.values)
        ax.set_title('Directors with most films')
        ax.set_xlabel('Director')
        ax.set_ylabel('Number of films')
        ax.tick_params(axis='x', rotation=45)

    elif choice == "2":
        avg_ratings = df.groupby('Director')['IMDB_Rating'].mean()
        film_counts = df.groupby('Director')['IMDB_Rating'].count()
        directors_3plus = film_counts[film_counts >= 3].index
        avg_ratings_filtered = avg_ratings[directors_3plus]
        top_ratings = avg_ratings_filtered.sort_values(ascending=False).head(10)

        ax.bar(top_ratings.index, top_ratings.values)
        ax.set_title('Highest average rating (min 3 films)')
        ax.set_xlabel('Director')
        ax.set_ylabel('Average rating')
        ax.set_ylim(8, top_ratings.values.max() + 0.1)
        ax.tick_params(axis='x', rotation=45)

    elif choice == "3":
        avg_revenue = df.groupby('Director')['Gross'].mean()
        top_revenue = avg_revenue.sort_values(ascending=False).head(10)

        ax.bar(top_revenue.index, top_revenue / 1000000)
        ax.set_title('Highest average revenue')
        ax.set_xlabel('Director')
        ax.set_ylabel('Average gross (millions $)')
        ax.tick_params(axis='x', rotation=45)

    elif choice == "4":
        director_counts = df['Director'].value_counts()
        top5_directors = director_counts.head(5).index

        for director in top5_directors:
            ratings = df[df['Director'] == director]['IMDB_Rating']
            ax.scatter([director] * len(ratings), ratings)

        ax.set_title('Ratings per director')
        ax.set_xlabel('Director')
        ax.set_ylabel('IMDb Rating')
        ax.tick_params(axis='x', rotation=45)

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        plt.close()
        continue

    plt.tight_layout()
    plt.show()