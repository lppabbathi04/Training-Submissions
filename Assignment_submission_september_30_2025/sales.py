import pandas as pd
df = pd.DataFrame({
    "product": ["Laptop", "Laptop", "Phone", "Phone"],
    "category": ["Electronics", "Electronics", "Electronics", "Electronics"],
    "month": ["Jan", "Jan", "Feb", "Feb"],
    "sales": [1000, 1200, 800, 900]
})

# Pivot table for summary
summary = df.pivot_table(
    values="sales",
    index="category",
    columns="month",
    aggfunc="sum"
)

print("\nSales Summary:")
print(summary)