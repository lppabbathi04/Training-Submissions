# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the Titanic dataset
df = pd.read_csv(r"C:\Users\pabba\OneDrive\Documents\GitHub\Titanic-Dataset.csv")


# Step 3: Select numeric columns to check for outliers
numeric_cols = ['Age', 'Fare']

# Step 4: Detect and visualize outliers using IQR and boxplots
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    # Show outlier values
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"\nOutliers in {col}:\n", outliers[[col]])
    
    # Visualize with boxplot
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()
    
    # Step 5: Handle outliers by replacing with median
    median = df[col].median()
    df[col] = df[col].apply(lambda x: median if x < lower or x > upper else x)

# Step 6: Confirm changes
print("\nAfter handling outliers:")
print(df[numeric_cols].describe())
