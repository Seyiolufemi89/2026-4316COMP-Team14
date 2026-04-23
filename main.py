import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


while True:
    print("1. Load dataset")
    print("2. Visualisations")

    choice = input("\nEnter your choice 1-2: ")

    if choice == "1":
        df = pd.read_csv('imdb_top_1000.csv')
        print("Dataset loaded successfully!")
    
    elif choice == "2":
        if 'df' not in locals():
            print("\nPlease load the dataset first!\n")
            continue

        while True:
            print("1. Thomas Ellerton")
            print("2. Ellie Harris")
            print("3. Mackenzie Scrivener")
            print("4. Oluwaseyi Olufemi")
            print("5. Paddy Monaghan")
            print("6. Kodi Dean")
            print("7. Tom McAdam")
            print("8. Back to main menu")

            choice = input("\nEnter your choice 1-8: ")

            if choice == "1":
                # Thomas Ellerton code
                print("Code \n")
            
            elif choice == "2":
                # Ellie Harris code
                data = df.copy()

                # numeric columns
                data['IMDB_Rating'] = pd.to_numeric(data['IMDB_Rating'], errors='coerce').replace([np.inf, -np.inf], np.nan)
                data['Meta_score'] = pd.to_numeric(data['Meta_score'], errors='coerce').replace([np.inf, -np.inf], np.nan)
                data['Gross'] = data['Gross'].astype(str).replace(r'[\$,]', '', regex=True)
                data['Gross'] = pd.to_numeric(data['Gross'], errors='coerce').replace([np.inf, -np.inf], np.nan)

                print("Dataset info: ")
                print(data.info())
                print("\nFirst 5 rows of dataset:")
                print(data.head())

                # creates base of graph figures
                fig, axes = plt.subplots(2, 2, figsize=(14, 10))

                # Plot 1: which genres have the highest average rating (top 10)
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

                # Plot 4: most frequent genres (top 10)
                genres = data['Genre'].value_counts().head(10)
                axes[1, 1].barh(genres.index, genres.values, color='pink', edgecolor='black', alpha=0.9)
                axes[1, 1].set_xlabel('Count')
                axes[1, 1].set_title('Top 10 movie Genres')
                axes[1, 1].grid(axis='x', alpha=0.3)

                plt.tight_layout()
                plt.show()

                print("Code \n")

            elif choice == "3":
                # Mackenzie Scrivener code
                print("Code \n")

            elif choice == "4":
                # Loads the dataset and reads the CSV file into a pandas
                df = pd.read_csv("imdb_top_1000.csv")

                # Data cleaning
                # Convert Runtime to numeric (remove or replace ' min')
                df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)

                # Convert Gross to numeric (remove commas and missing values)
                df['Gross'] = df['Gross'].str.replace(',', '').astype(float)

                # rows with missing values in columns
                df = df.dropna(subset=['Runtime', 'IMDB_Rating', 'Gross', 'Meta_score'])

                # Display basic information about the dataset
                print("Dataset Information:")
                print(df.info())
                print("\nFirst 5 rows of the dataset:")
                print(df.head())

                # Create a figure with multiple subplots for different visualizations
                fig, axes = plt.subplots(2, 3, figsize=(18, 10))

                # Plot 1: Runtime vs IMDB Rating (Scatter Plot)
                axes[0, 0].scatter(df['Runtime'], df['IMDB_Rating'], alpha=0.6, color='blue')
                axes[0, 0].set_xlabel('Runtime (minutes)')
                axes[0, 0].set_ylabel('IMDB Rating')
                axes[0, 0].set_title('Runtime vs IMDB Rating')
                axes[0, 0].grid(True)

                # Add linear line correlation for Runtime vs IMDB_Rating
                corr_rating = df['Runtime'].corr(df['IMDB_Rating'])
                m, b = np.polyfit(df['Runtime'], df['IMDB_Rating'], 1)
                xs = np.linspace(df['Runtime'].min(), df['Runtime'].max(), 100)
                axes[0, 0].plot(xs, m * xs + b, color='red', linewidth=1.5, label=f'fit (r={corr_rating:.2f})')
                axes[0, 0].legend(loc='best')
                axes[0, 0].text(0.02, 0.95, f"r = {corr_rating:.2f}", transform=axes[0, 0].transAxes,
                                fontsize=10, verticalalignment='top')

                # Plot 2: Runtime vs Gross Revenue (Scatter Plot)
                axes[0, 1].scatter(df['Runtime'], df['Gross'], alpha=0.6, color='green')
                axes[0, 1].set_xlabel('Runtime (minutes)')
                axes[0, 1].set_ylabel('Gross Revenue ($)')
                axes[0, 1].set_title('Runtime vs Gross Revenue')
                axes[0, 1].grid(True)

                # Add linear line correlation for Runtime vs Gross
                corr_gross = df['Runtime'].corr(df['Gross'])
                m2, b2 = np.polyfit(df['Runtime'], df['Gross'], 1)
                xs2 = np.linspace(df['Runtime'].min(), df['Runtime'].max(), 100)
                axes[0, 1].plot(xs2, m2 * xs2 + b2, color='red', linewidth=1.5, label=f'fit (r={corr_gross:.2f})')
                axes[0, 1].legend(loc='best')
                axes[0, 1].text(0.02, 0.95, f"r = {corr_gross:.2f}", transform=axes[0, 1].transAxes,
                                fontsize=10, verticalalignment='top')

                # Plot 3: Meta Score vs IMDB Rating (Scatter Plot)
                axes[0, 2].scatter(df['Meta_score'], df['IMDB_Rating'], alpha=0.6, color='purple')
                axes[0, 2].set_xlabel('Meta Score')
                axes[0, 2].set_ylabel('IMDB Rating')
                axes[0, 2].set_title('Meta Score vs IMDB Rating')
                axes[0, 2].grid(True)

                # Add linear line correlation for Meta Score vs IMDB Rating
                corr_meta_rating = df['Meta_score'].corr(df['IMDB_Rating'])
                m3, b3 = np.polyfit(df['Meta_score'], df['IMDB_Rating'], 1)
                xs3 = np.linspace(df['Meta_score'].min(), df['Meta_score'].max(), 100)
                axes[0, 2].plot(xs3, m3 * xs3 + b3, color='red', linewidth=1.5, label=f'fit (r={corr_meta_rating:.2f})')
                axes[0, 2].legend(loc='best')
                axes[0, 2].text(0.02, 0.95, f"r = {corr_meta_rating:.2f}", transform=axes[0, 2].transAxes,
                                fontsize=10, verticalalignment='top')

                # Plot 4: Meta Score vs Gross Revenue (Scatter Plot)
                axes[1, 0].scatter(df['Meta_score'], df['Gross'], alpha=0.6, color='orange')
                axes[1, 0].set_xlabel('Meta Score')
                axes[1, 0].set_ylabel('Gross Revenue ($)')
                axes[1, 0].set_title('Meta Score vs Gross Revenue')
                axes[1, 0].grid(True)

                # Add linear line correlation for Meta Score vs Gross
                corr_meta_gross = df['Meta_score'].corr(df['Gross'])
                m4, b4 = np.polyfit(df['Meta_score'], df['Gross'], 1)
                xs4 = np.linspace(df['Meta_score'].min(), df['Meta_score'].max(), 100)
                axes[1, 0].plot(xs4, m4 * xs4 + b4, color='red', linewidth=1.5, label=f'fit (r={corr_meta_gross:.2f})')
                axes[1, 0].legend(loc='best')
                axes[1, 0].text(0.02, 0.95, f"r = {corr_meta_gross:.2f}", transform=axes[1, 0].transAxes,
                                fontsize=10, verticalalignment='top')

                # Hide the extra subplots
                axes[1, 1].axis('off')
                axes[1, 2].axis('off')

                plt.tight_layout()
                plt.show()

                print("Code \n")

            elif choice == "5":
                # Paddy Monaghan code
                print("Code \n")

            elif choice == "6":
                # Kodi Dean code
                print("Code \n")

            elif choice == "7":
                # Tom McAdam code
                print("Code \n")

            elif choice == "8":
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.\n")