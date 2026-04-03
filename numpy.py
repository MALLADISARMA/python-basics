import numpy as np

# -------------------------------
# 1. Creating Arrays
# -------------------------------
print("Creating Arrays:")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2], [3, 4]])
print(arr1)
print(arr2)

# Special arrays
zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
identity = np.eye(3)

print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Identity:\n", identity)

# -------------------------------
# 2. Array Properties
# -------------------------------
print("\nArray Properties:")
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)

# -------------------------------
# 3. Indexing & Slicing
# -------------------------------
print("\nIndexing & Slicing:")
arr = np.array([10, 20, 30, 40, 50])
print("Element:", arr[2])
print("Slice:", arr[1:4])

# -------------------------------
# 4. Arithmetic Operations
# -------------------------------
print("\nArithmetic Operations:")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)

# -------------------------------
# 5. Matrix Operations
# -------------------------------
print("\nMatrix Operations:")
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Matrix Multiplication:\n", np.dot(m1, m2))
print("Transpose:\n", m1.T)

# -------------------------------
# 6. Statistical Functions
# -------------------------------
print("\nStatistics:")
data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))

# -------------------------------
# 7. Reshaping Arrays
# -------------------------------
print("\nReshaping:")
arr = np.arange(6)
reshaped = arr.reshape(2, 3)
print(reshaped)

# -------------------------------
# 8. Random Numbers
# -------------------------------
print("\nRandom Numbers:")
rand_arr = np.random.rand(2, 2)
rand_int = np.random.randint(1, 10, (2, 3))

print("Random Float:\n", rand_arr)
print("Random Int:\n", rand_int)

# -------------------------------
# 9. Filtering / Conditions
# -------------------------------
print("\nFiltering:")
arr = np.array([1, 2, 3, 4, 5, 6])
filtered = arr[arr > 3]
print(filtered)

# -------------------------------
# 10. Broadcasting
# -------------------------------
print("\nBroadcasting:")
arr = np.array([1, 2, 3])
print(arr + 10)

# -------------------------------
# 11. Sorting
# -------------------------------
print("\nSorting:")
arr = np.array([5, 2, 9, 1])
print(np.sort(arr))

# -------------------------------
# 12. Stacking Arrays
# -------------------------------
print("\nStacking:")
a = np.array([1, 2])
b = np.array([3, 4])

print("Vertical Stack:\n", np.vstack((a, b)))
print("Horizontal Stack:\n", np.hstack((a, b)))

# -------------------------------
# 13. Saving & Loading Data
# -------------------------------
print("\nSaving & Loading:")
np.save("data.npy", arr)
loaded = np.load("data.npy")
print("Loaded:", loaded)

# -------------------------------
# 14. Linear Algebra
# -------------------------------
print("\nLinear Algebra:")
matrix = np.array([[1, 2], [3, 4]])

print("Determinant:", np.linalg.det(matrix))
print("Inverse:\n", np.linalg.inv(matrix))
print("Eigenvalues:", np.linalg.eig(matrix)[0])

# -------------------------------
# END
# -------------------------------
print("\nAll NumPy operations executed successfully!")
