import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("Original Array:")
print(arr)

print("\nSlicing: arr[1:5] => Elements from index 1 to 4")
print(arr[1:5])

print("\nSlicing: arr[:3] => First three elements")
print(arr[:3])

print("\nSlicing: arr[::2] => Every second element")
print(arr[::2])

indices = [0, 2, 4]
print("\nInteger Indexing: arr[[0, 2, 4]] => Specific indices")
print(arr[indices])

print("arr + 10 => Add 10 to each element")
print(arr + 10)

print("arr * 2 => Multiply each element by 2")
print(arr * 2)

print("arr ** 2 => Square of each element")
print(arr ** 2)

print("\nStatistical Operations:")
print("Sum of elements:", arr.sum())
print("Maximum value:", arr.max())
print("Mean value:", arr.mean())
