import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# ====================== loads + cleans ======================

df = pd.read_csv("imdb_top_1000.csv")

# Clean Runtime
df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)

# Clean Gross
df['Gross'] = pd.to_numeric(
    df['Gross'].str.replace(',', '', regex=True), 
    errors='coerce'
)

df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df['IMDB_Rating'] = df['IMDB_Rating'].astype(float)

print("Data loaded:", len(df), "movies\n")

# Helper function to format y-axis as currency
def currency_formatter(x, pos):
    return f'${x:,.0f}'

# ====================== Revenue vs Rating correlation ======================

df_clean = df.dropna(subset=['Gross'])
corr_rating = df_clean['IMDB_Rating'].corr(df_clean['Gross'])
print("Rating–Revenue correlation:", round(corr_rating, 3))

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_clean, x='IMDB_Rating', y='Gross', alpha=0.6)
plt.title(f'Gross Revenue vs IMDB Rating (corr = {round(corr_rating, 3)})')
plt.xlabel('IMDB Rating')
plt.ylabel('Gross Revenue')
plt.gca().yaxis.set_major_formatter(FuncFormatter(currency_formatter))
plt.tight_layout()

# ====================== Top 10 highest revenue movies ======================

top10_rev = df.nlargest(10, 'Gross')[['Series_Title', 'Gross']]
print("Highest revenue movie:", top10_rev.iloc[0]['Series_Title'])

plt.figure(figsize=(12, 8))
sns.barplot(data=top10_rev, x='Gross', y='Series_Title')
plt.title('Top 10 Highest Gross Revenue Movies')
plt.xlabel('Gross Revenue')
plt.gca().xaxis.set_major_formatter(FuncFormatter(currency_formatter))
plt.tight_layout()

# ====================== Longer movies & revenue ======================

corr_runtime = df_clean['Runtime'].corr(df_clean['Gross'])
print("Runtime–Revenue correlation:", round(corr_runtime, 3))

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_clean, x='Runtime', y='Gross', alpha=0.6)
plt.title(f'Runtime vs Gross Revenue (corr = {round(corr_runtime, 3)})')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Gross Revenue')
plt.gca().yaxis.set_major_formatter(FuncFormatter(currency_formatter))
plt.tight_layout()

plt.show()