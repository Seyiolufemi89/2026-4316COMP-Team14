import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
# (2 rows, 3 columns) = 6 plots total
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Plot 1: Runtime vs IMDB Rating (Scatter Plot)
# Do longer movies have higher ratings?
axes[0, 0].scatter(df['Runtime'], df['IMDB_Rating'], alpha=0.6, color='blue') # Scatter plot with some transparency (alpha) for better visibility
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
# Do longer movies generate more revenue?
axes[0, 1].scatter(df['Runtime'], df['Gross'], alpha=0.6, color='green')
axes[0, 1].set_xlabel('Runtime (minutes)')
axes[0, 1].set_ylabel('Gross Revenue ($)')
axes[0, 1].set_title('Runtime vs Gross Revenue')
axes[0, 1].grid(True)

# Add linear line correlation for Runtime vs Gross
corr_gross = df['Runtime'].corr(df['Gross'])
m2, b2 = np.polyfit(df['Runtime'], df['Gross'], 1)
xs2 = np.linspace(df['Runtime'].min(), df['Runtime'].max(), 100)
axes[0, 1].plot(xs2, m2 * xs2 + b2, color='red', linewidth=1.5, label=f'fit (r={corr_gross:.2f})')# Add linear line correlation for Runtime vs Gross
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

# Changes layout to prevent overlapping and show all plots
plt.tight_layout()
plt.show()