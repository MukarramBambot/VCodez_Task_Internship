# Task 12 - List and Tuple Operations

from collections import Counter

# ----------------- LIST OPERATIONS -----------------
print("### LIST OPERATIONS ###")

# Define one list for all operations
my_list = [10, 20, 30, 40, 20, 10, 50]
print("Original List:", my_list)

# 1. Sum all the items
print("1. Sum of items:", sum(my_list))

# 2. Multiply all the items
product = 1
for num in my_list:
    product *= num
print("2. Product of items:", product)

# 3. Largest number
print("3. Largest number:", max(my_list))

# 4. Smallest number
print("4. Smallest number:", min(my_list))

# 5. Remove duplicates
unique_list = list(set(my_list))
print("5. List without duplicates:", unique_list)

# 6. Check if list is empty
print("6. Is the list empty?:", "Yes" if not my_list else "No")

print("-" * 100)  # separator

# ----------------- TUPLE OPERATIONS -----------------
print("### TUPLE OPERATIONS ###")

# Define one tuple for all operations
my_tuple = (10, 20, 30, 40, 50, 20, "Hello", 3.14, True, 40)
print("Original Tuple:", my_tuple)

# 1. Tuple with different datatypes
print("1. Tuple with different datatypes:", my_tuple)

# 2. Print one item (3rd element)
print("2. 3rd element:", my_tuple[2])

# 3. Unpack first three items into variables
a, b, c = my_tuple[0:3]
print("3. Unpacked values:", a, b, c)

# 4. Add an item (tuples are immutable → convert to list → back to tuple)
temp_list = list(my_tuple)
temp_list.append("NewItem")
my_tuple = tuple(temp_list)
print("4. Tuple after adding an item:", my_tuple)

# 5. Get 5th element and 5th element from the last
print("5. 5th element:", my_tuple[4])
print("   5th element from last:", my_tuple[-5])

# 6. Find repeated elements in the tuple
count = Counter(my_tuple)
repeated = [item for item, freq in count.items() if freq > 1]
print("6. Repeated elements:", repeated)
