# example

import numpy as np

print("Example provided in LMS:")
# Create a simple array
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)

# Perform operations
print("Array * 2:", my_array * 2)         # Multiply each element by 2
print("Mean:", np.mean(my_array))        # Average of the array
print("Square Roots:", np.sqrt(my_array))

# Practice task
print("Practice task")

# Create an array with numbers 10 to 50.

prac_list=[]

i = 10
while i <= 50:
    prac_list.append(i)
    i += 1


prac_array=np.array(prac_list)

print(f"The array: {prac_array}")

# Find the maximum and minimum values

print(f"The maximum number is: {np.max(prac_array)} and the minimum number is: {np.min(prac_array)}")

# Multiply all elements by 3.

print(f"When you multiply the array by 3, you get: {prac_array*3}")