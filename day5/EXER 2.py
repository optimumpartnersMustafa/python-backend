my_list = [3, 5, 7, 5, 9, 3]
unique_values_set = set(my_list)
unique_values_list = list(unique_values_set)
print(unique_values_list)
#-----------------------------------------------------------------------------------------------
# Define the two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Compute the set operations
union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)
symmetric_difference_set = A.symmetric_difference(B)
# Print the results
print(f"Union (A ∪ B): {union_set}")
print(f"Intersection (A ∩ B): {intersection_set}")
print(f"Difference (A - B): {difference_set}")
print(f"Symmetric Difference (A ∆ B): {symmetric_difference_set}")
#-----------------------------------------------------------------------------------------------
# Given string
text = "apple banana apple cherry banana"
# Split the string into words
words = text.split()
# Convert the list of words to a set to find unique words
unique_words = set(words)
# Count the number of unique words
unique_word_count = len(unique_words)
# Print the result
print(f"The number of unique words is: {unique_word_count}")
#-----------------------------------------------------------------------------------------------
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics", "History"]
}
print(student)
#-----------------------------------------------------------------------------------------------
# Given string
text = "hello world hello"
# Initialize an empty dictionary to store word frequencies
word_frequency = {}
# Split the string into words
words = text.split()
# Iterate through the words and count their frequency
for word in words:
    # If the word is already in the dictionary, increment its count
    if word in word_frequency:
        word_frequency[word] += 1
    # If the word is not in the dictionary, add it with a count of 1
    else:
        word_frequency[word] = 1
# Print the resulting dictionary
print(word_frequency)
#-----------------------------------------------------------------------------------------------
squares_dict = {x: x**2 for x in range(1, 6)}
# Print the resulting dictionary
print(squares_dict)
#-----------------------------------------------------------------------------------------------
while (n := int(input("Enter a number greater than 10: "))) <= 10:
    print(f"You entered {n}. Please try again.")
print(f"Thank you! You entered {n}, which is greater than 10.")
#-----------------------------------------------------------------------------------------------
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = dict1.copy()
for key, value in dict2.items():
    if key in merged_dict:
        if (existing_value := merged_dict.get(key)) is not None:
            merged_dict["b_resolved"] = existing_value + value
            del merged_dict[key]
    else:
        merged_dict[key] = value

print(merged_dict)
#-----------------------------------------------------------------------------------------------
inventory = {
    "apple": {"price": 1.5, "category": "fruit"},
    "banana": {"price": 0.75, "category": "fruit"},
    "milk": {"price": 2.99, "category": "dairy"},
    "bread": {"price": 3.25, "category": "bakery"},
    "cheese": {"price": 4.5, "category": "dairy"},
    "chocolate": {"price": 2.25, "category": "snacks"}
}
shopping_cart = ["apple", "milk", "banana", "cheese", "apple", "bread", "chocolate", "milk"]

print("Analyzing your shopping cart...\n")

total_price = 0.0

item_quantities = {}

for item_name in shopping_cart:
    if item_name in inventory:
        total_price += inventory[item_name]["price"]
        item_quantities[item_name] = item_quantities.get(item_name, 0) + 1
    else:
        print(f"Warning: '{item_name}' not found in inventory and will not be included in the total.")

unique_categories = set()
for item_name in shopping_cart:
    if item_name in inventory:
        unique_categories.add(inventory[item_name]["category"])

most_expensive_item_name = None
max_price = -1.0 

for item_name in shopping_cart:
    if item_name in inventory:

        if (current_item_price := inventory[item_name]["price"]) > max_price:
            max_price = current_item_price
            most_expensive_item_name = item_name

print("🛒🛍️ Your Detailed Shopping Receipt 🧾")
print("---------------------------------------")

for item_name, quantity in item_quantities.items():
    price_per_unit = inventory[item_name]["price"]
    item_total = price_per_unit * quantity
    print(f"{item_name.capitalize()} (x{quantity}): ${price_per_unit:.2f} each = ${item_total:.2f}")

print("---------------------------------------")

print(f"💰 Total Price: ${total_price:.2f}")

print(f"🏷️ Unique Categories: {', '.join(sorted(list(unique_categories)))}")

if most_expensive_item_name:
    print(f"💎 Most Expensive Item: {most_expensive_item_name.capitalize()} (${max_price:.2f})")
else:
    print("No items found in the cart to determine the most expensive.")
print("---------------------------------------")
print("Thank you for shopping with us! 😊")