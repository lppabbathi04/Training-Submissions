# Step 1: Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Step 2: Prepare the data
# X should be 2D (feature), y should be 1D (target/output)
X = np.array([[1], [2], [3], [4], [5]])  # Input data (e.g., hours studied)
y = np.array([2, 4, 5, 4, 5])           # Output data (e.g., exam scores)

# Step 3: Create the model
model = LinearRegression()

# Step 4: Train (fit) the model
model.fit(X, y)

# Step 5: Make predictions
predictions = model.predict(X)

# Step 6: Display results
print("Predicted values:", predictions)
print("Slope (m):", model.coef_)
print("Intercept (b):", model.intercept_)
