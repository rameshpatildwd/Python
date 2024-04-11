# Input
shopping_list = ["apples", "bananas", 3, "milk", 2, "eggs"]

# Print the number of apples
apple_count = shopping_list.count("apples")
print("Number of apples:", apple_count)

# Extract the dairy items
dairy_items = [item for item in shopping_list if isinstance(item, str) and ("milk" in item.lower() or "eggs" in item.lower())]
print("Dairy items:", dairy_items)

# Create a new list with just the fruit names
fruit_names = [item for item in shopping_list if isinstance(item, str) and item.lower() not in ["milk", "eggs"]]
print("Fruits:", fruit_names)
