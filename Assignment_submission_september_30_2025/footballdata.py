import pandas as pd

# 🧠 Step 1: Load your dataset (change the file name & username if needed)
df = pd.read_csv(r"C:\\Users\\pabba\\OneDrive\\Desktop\\Career_Stats_Defensive.csv")

# 👀 Step 2: Look at first few rows
print("📋 First 5 Rows:")
print(df.head())

# 🧩 Step 3: Check data types
print("\n🧠 Data Info:")
print(df.info())

# 🕳️ Step 4: Count missing values per column
print("\n❓ Missing Values per Column:")
print(df.isnull().sum())

# 🧮 Step 5: Total missing values in dataset
print("\n🔢 Total Missing Values in Dataset:")
print(df.isnull().sum().sum())

# 🧬 Step 6: Unique values for each column (replace 'ColumnName' with one of your real columns)
print("\n✨ Unique Values Example (replace 'ColumnName' with one from your data):")
print(df['Longest Int Return'].unique())

# 📊 Step 7: Value counts for a column (replace 'ColumnName')
print("\n📈 Value Counts Example:")
print(df['Total Tackles'].value_counts())

# 🧾 Step 8: Average of numeric columns
print("\n📏 Average of Numeric Columns:")
print(df.mean(numeric_only=True))

# 📚 Step 9: Grouping example (replace 'CategoryColumn' and 'NumericColumn')
print("\n🏙️ Example of Grouping (Average of a numeric column by a category):")
print(df.groupby('Team')['Yards Per Int'].mean())
