
# Task 3: Data Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset load 
df = pd.read_csv("data_lec12.csv")


# Step 1: Top 10 Best Selling Games
# ====================================
top_games = df.sort_values(by='Global_Sales', ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.bar(top_games['Name'], top_games['Global_Sales'])
plt.title("Top 10 Best Selling Games")
plt.xlabel("Game Name")
plt.ylabel("Global Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Step 2: Top Game Genres
# ====================================
genre_counts = df['Genre'].value_counts()

plt.figure(figsize=(8,5))
plt.bar(genre_counts.index, genre_counts.values)
plt.title("Top Game Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Step 3: Top Gaming Platforms
# ====================================
platform_counts = df['Platform'].value_counts().head(10)

plt.figure(figsize=(8,5))
plt.bar(platform_counts.index, platform_counts.values)
plt.title("Top Gaming Platforms")
plt.xlabel("Platform")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Step 4: Global Sales Distribution
# ====================================
plt.figure(figsize=(8,5))
plt.hist(df['Global_Sales'], bins=20)
plt.title("Global Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# Step 5: Sales Share by Genre (Pie Chart)
# ====================================
genre_sales = df.groupby('Genre')['Global_Sales'].sum()

plt.figure(figsize=(7,7))
plt.pie(genre_sales, labels=genre_sales.index, autopct='%1.1f%%')
plt.title("Sales Share by Genre")
plt.show()