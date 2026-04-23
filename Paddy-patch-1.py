import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv("imdb_top_1000.csv")
 
# Clean up columns 
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
 

df["Runtime"] = df["Runtime"].str.replace(" min", "").str.strip()
df["Runtime"] = pd.to_numeric(df["Runtime"], errors="coerce")
 
# Remove commas and convert to numeric
df["Gross"] = df["Gross"].str.replace(",", "").str.strip()
df["Gross"] = pd.to_numeric(df["Gross"], errors="coerce")
 
# Drop rows where Released_Year is missing
df = df.dropna(subset=["Released_Year"])
df["Released_Year"] = df["Released_Year"].astype(int)
 
# Add a Decade column
df["Decade"] = (df["Released_Year"] // 10) * 10
 
# Create a grid of charts 
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("IMDb Top 1000 Movies – Data Analysis", fontsize=16, fontweight="bold")
 
# Movies released per year
movies_per_year = df.groupby("Released_Year").size()
 
axes[0, 0].bar(movies_per_year.index, movies_per_year.values, color="blue", edgecolor="white")
axes[0, 0].set_title("Movies Released Per Year")
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Number of Movies")
axes[0, 0].tick_params(axis="x", rotation=45)
 
# Average IMDb rating over time 
avg_rating = df.groupby("Released_Year")["IMDB_Rating"].mean()
 
axes[0, 1].plot(avg_rating.index, avg_rating.values, color="blue", linewidth=2, marker="o", markersize=3)
axes[0, 1].set_title("Average IMDb Rating Over Time")
axes[0, 1].set_xlabel("Year")
axes[0, 1].set_ylabel("Average Rating")
axes[0, 1].set_ylim(6, 10)
axes[0, 1].tick_params(axis="x", rotation=45)
 
# Average runtime per decade 
avg_runtime = df.groupby("Decade")["Runtime"].mean().dropna()
 
axes[1, 0].bar(avg_runtime.index.astype(str), avg_runtime.values, color="blue", edgecolor="white", width=0.6)
axes[1, 0].set_title("Average Runtime Per Decade")
axes[1, 0].set_xlabel("Decade")
axes[1, 0].set_ylabel("Average Runtime (minutes)")
axes[1, 0].tick_params(axis="x", rotation=45)
 
# Average revenue (gross) per decade
avg_gross = df.groupby("Decade")["Gross"].mean().dropna()
 
# Convert to millions for readable labels
avg_gross_millions = avg_gross / 1_000_000
 
axes[1, 1].bar(avg_gross_millions.index.astype(str), avg_gross_millions.values, color="blue", edgecolor="white", width=0.6)
axes[1, 1].set_title("Average Box-Office Revenue Per Decade")
axes[1, 1].set_xlabel("Decade")
axes[1, 1].set_ylabel("Average Gross ($ millions)")
axes[1, 1].tick_params(axis="x", rotation=45)
 
# Final layout & save
plt.tight_layout()
plt.show()