import numpy as np

# Product data
items = np.array(["Pen", "Notebook", "Marker", "Eraser"])
price = np.array([1.5, 3.0, 2.0, 0.5])
quantity = np.array([100, 50, 30, 10])

# Total value per item
total_value = price * quantity

print("📦 Inventory Summary")
print("----------------------")
for i in range(len(items)):
    print(f"{items[i]} - Price: ${price[i]}, Quantity: {quantity[i]}, Value: ${total_value[i]:.2f}")

print("\nTotal Inventory Value: $", np.sum(total_value))
print(" Low Stock Items:", items[quantity < 20])
