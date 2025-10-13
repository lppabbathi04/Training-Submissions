import pandas as pd

# Step 1: Create a messy dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', None],
    'Age': [25, None, 30, 25, 22],
    'City': ['New York', 'Los Angeles', None, 'New York', 'Chicago']
}

df = pd.DataFrame(data)

print("🔹 Original Data:")
print(df)

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Handle missing values
# Option 1: Fill missing values with default
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)  # replace missing ages with mean
df['City'].fillna('Unknown', inplace=True)

print("\n✅ Cleaned Data:")
print(df)

# Step 4: Get summary insights
print("\n📊 Data Summary:")
print(df.describe())   # summary for numeric columns
print("\nUnique Cities:", df['City'].unique())
print("Average Age:", df['Age'].mean())
print("Total Rows after cleaning:", len(df))
