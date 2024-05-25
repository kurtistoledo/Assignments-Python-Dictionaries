# Lesson 1: Python Dictionaries
# 4. Python Essentials for Business Analytics

import copy

# Given sales data
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

# Create a deep copy of weekly_sales
copied_sales = copy.deepcopy(weekly_sales)

# Update the sales figure for "Electronics" in "Week 2"
copied_sales["Week 2"]["Electronics"] = 18000

# Display the updated sales data
print("Original Sales Data:")
print(weekly_sales)
print("\nCopied Sales Data with Updated Electronics Sales:")
print(copied_sales)
