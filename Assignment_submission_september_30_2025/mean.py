# Sample dataset
data = [10, 20, 20, 30, 40]

# 1) MEAN
mean = sum(data) / len(data)

# 2) MEDIAN
data_sorted = sorted(data)
n = len(data_sorted)
if n % 2 == 1:  # odd
    median = data_sorted[n//2]
else:           # even
    median = (data_sorted[n//2 - 1] + data_sorted[n//2]) / 2

# 3) MODE
# Count frequency of each number
frequency = {}
for num in data:
    frequency[num] = frequency.get(num, 0) + 1

# Find the number with max frequency
mode = max(frequency, key=frequency.get)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
