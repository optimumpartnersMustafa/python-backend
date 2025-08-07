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
# Define the dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
# Create a copy of dict1 to start the merge
merged_dict = dict1.copy()
# Iterate through dict2 to handle conflicts
for key, value in dict2.items():
    # Use a conditional check for the walrus operator
    if key in merged_dict:
        # Conflict: get the existing value and sum it with the new value
        if (existing_value := merged_dict.get(key)) is not None:
            merged_dict["b_resolved"] = existing_value + value
            # Remove the old, conflicting key
            del merged_dict[key]
    else:
        # No conflict, simply add the new key-value pair
        merged_dict[key] = value
# Print the final merged dictionary
print(merged_dict)