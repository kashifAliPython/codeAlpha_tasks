# Task 2: Exploratory Data Analysis (EDA)
import pandas as pd
df = pd.read_csv("data_lec12.csv")

# Step 1: Dataset Shape
print("Rows and Columns:", df.shape)


# Step 2: Column Names
# ====================================
print("\nColumns:")
print(df.columns)

# Step 3: Dataset Information
# ====================================
print("\nDataset Info:")
print(df.info())


# Step 4: Missing Values Check
# ====================================
print("\nMissing Values:")
print(df.isnull().sum())


# ====================================
# Step 5: Top 10 Best Selling Games
# ====================================
print("\nTop 10 Best Selling Games:")
print(df[['Name', 'Global_Sales']].sort_values(by='Global_Sales', ascending=False).head(10))


# ====================================
# Step 6: Top Game Genres
# ====================================
print("\nTop Game Genres:")
print(df['Genre'].value_counts())


# ====================================
# Step 7: Top Gaming Platforms
# ====================================
print("\nTop Gaming Platforms:")
print(df['Platform'].value_counts())


# ====================================
# Step 8: Total Global Sales
# ====================================
print("\nTotal Global Sales:")
print(df['Global_Sales'].sum())


# ====================================
# Step 9: Average Global Sales
# ====================================
print("\nAverage Global Sales:")
print(df['Global_Sales'].mean())


# ====================================
# Step 10: Top Publishers
# ====================================
print("\nTop Publishers:")
print(df['Publisher'].value_counts().head(10))



