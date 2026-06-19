import pandas as pd
import numpy as np

# Local dataset load karein
df = pd.read_csv("data_lec12.csv")

# First 5 rows dekhein
print(df.head())


# ====================================
# Task 1: Data Cleaning
# ====================================

# Step 1: Dataset Information
print("Dataset Information")
print(df.info())

# Step 2: Check Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Step 3: Fill Missing Values in Age
df['Age'] = df['Age'].fillna(df['Age'].median())

# Step 4: Fill Missing Values in Embarked
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Step 5: Drop Cabin Column
df = df.drop(columns=['Cabin'])

# Step 6: Check Duplicate Rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Step 7: Remove Duplicate Rows
df = df.drop_duplicates()

# Step 8: Final Check
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape:")
print(df.shape)

# Step 9: Save Cleaned Dataset
df.to_csv("titanic_cleaned.csv", index=False)
print("\nCleaned dataset saved successfully!")