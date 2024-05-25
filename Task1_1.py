# Lesson 1: Python Dictionaries
# 1. Real-World Python Dictionary Applications

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category "Beverages" with items
restaurant_menu["Beverages"] = {"Coffee": 2.50, "Soda": 1.99}

# Update the price of "Steak"
restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters"
del restaurant_menu["Starters"]["Bruschetta"]

# Print the updated menu
for category, items in restaurant_menu.items():
    print(f"{category}:\n{items}")
