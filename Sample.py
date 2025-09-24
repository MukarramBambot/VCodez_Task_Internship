# Task 13 - Set Programs in Python

print("### SET PROGRAMS ###")

# Define sets at the start
my_set = {10, 20, 30, 40}
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# 1. Create a set
print("1. Created Set:", my_set)
print("-" * 190)

# 2. Iterate over sets
print("2. Iterating over Set:")
for item in my_set:
    print(item)
print("-" * 190)

# 3. Add elements to a set
new_set = my_set.copy()   # keeping original safe
new_set.add(50)
print("3. After Adding 50:", new_set)
print("-" * 190)

# 4. Remove an item from a given set
removed_set = new_set.copy()
removed_set.remove(20)  # if 20 not present, error
print("4. After Removing 20:", removed_set)
print("-" * 190)

# 5. Remove an item if present
discarded_set = removed_set.copy()
discarded_set.discard(100)  # no error if not present
print("5. After Discarding 100 (no error if not present):", discarded_set)
print("-" * 190)

# 6. Create an intersection of sets
print("6. Intersection of set_a and set_b:", set_a.intersection(set_b))
print("-" * 190)

# 7. Create a union of sets
print("7. Union of set_a and set_b:", set_a.union(set_b))
print("-" * 190)
