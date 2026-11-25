import numpy as np

arr = np.arange(1, 11)

print("Original Array:", arr)

print("First Element:", arr[0])
print("Last Element:", arr[-1])

print("First Five Elements:", arr[:5])
print("Elements from index 5 to 9:", arr[5:])

print("Addition:", arr + 2)
print("Subtraction:", arr - 2)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)

print("Sum of Array:", np.sum(arr))
print("Mean of Array:", np.mean(arr))
