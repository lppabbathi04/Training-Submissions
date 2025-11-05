import numpy as np

A = np.array([[2, 3],
              [1, 4]])

B = np.array([[5, 2],
              [3, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("\n➕ Addition:\n", A + B)
print("➖ Subtraction:\n", A - B)
print("✖️ Multiplication:\n", np.dot(A, B))
print("🔁 Inverse of A:\n", np.linalg.inv(A))
print("📏 Transpose of B:\n", B.T)
