# Task 11 - Star Pattern Shapes

# Right Triangle
print("Right Triangle")
rows = int(input("Enter the number of rows for Right-Angled Triangle: "))
for i in range(1, rows + 1):
    print("* " * i)

print("----------------------------------------------------------------------------------------------------------------------------------------------")

# Inverted Right Triangle
print("Inverted Right Triangle")
rows = int(input("Enter the number of rows for Inverted Right-Angled Triangle: "))
for i in range(rows, 0, -1):
    print("* " * i)

print("----------------------------------------------------------------------------------------------------------------------------------------------")

# Full Pyramid
print("Full Pyramid")
rows = int(input("Enter the number of rows for Full Pyramid: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

print("----------------------------------------------------------------------------------------------------------------------------------------------")

# Inverted Full Pyramid
print("Inverted Full Pyramid")
rows = int(input("Enter the number of rows for Inverted Full Pyramid: "))
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)

print("----------------------------------------------------------------------------------------------------------------------------------------------")

# Parallelogram
print("Parallelogram")
rows = int(input("Enter the size of the Parallelogram: "))
for i in range(rows):
    print(" " * (rows - i) + "* " * rows)

print("----------------------------------------------------------------------------------------------------------------------------------------------")
