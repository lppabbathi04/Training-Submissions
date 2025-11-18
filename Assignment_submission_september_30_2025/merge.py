

import pandas as pd

# ---- Challenge 1 ----
# Create customer data
customer_data = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["Ram", "Sita", "Raja"]
})

# Create order data
order_data = pd.DataFrame({
    "order_id": [101, 102, 103],
    "customer_id": [1, 2, 1],
    "amount": [500, 700, 300]
})

# Merge both tables
merged = customer_data.merge(order_data, on="customer_id", how="inner")
print("Merged Data:")