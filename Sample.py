print("### Task 15: Difference between map, filter, and reduce ###\n")

from functools import reduce

# Real-time Example: Online Shopping Prices
prices = [250, 450, 120, 999, 75, 300]

print("Original Prices:", prices)
print("-" * 120)

# 1. map() → Apply a function to each element
gst_prices = list(map(lambda p: p * 1.10, prices))
print("1. map() → Prices after adding 10% GST:", gst_prices)
print("-" * 120)

# 2. filter() → Select elements based on condition
premium_products = list(filter(lambda p: p > 300, prices))
print("2. filter() → Premium products (above 300):", premium_products)
print("-" * 120)

# 3. reduce() → Apply rolling computation
total_amount = reduce(lambda x, y: x + y, prices)
print("3. reduce() → Total amount of cart:", total_amount)
print("-" * 120)

# ✅ Key Difference Summary
print("""
map()    → Transforms each element (all elements included)
filter() → Selects elements based on condition
reduce() → Combines elements into a single result
""")
