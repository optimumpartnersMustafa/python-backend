def remove_duplicates_with_sets(input_list):
    print(f"Original list: {input_list}")
    unique_elements = set(input_list)
    print(f"List after removing duplicates using a set: {list(unique_elements)}")
    return list(unique_elements)

def count_word_frequency(text):
    print(f"\nOriginal text: '{text}'")
    words = text.lower().split()
    word_counts = {}
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum())
        if cleaned_word:
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    print(f"Word frequencies: {word_counts}")
    return word_counts

def merge_dictionaries(dict1, dict2):
    print(f"\nDictionary 1: {dict1}")
    print(f"Dictionary 2: {dict2}")
    merged_dict = dict1.copy()
    print("\nMerging process (demonstrating walrus operator for conflict resolution):")
    for key, value in dict2.items():
        if (conflict_exists := key in merged_dict):
            print(f"  Conflict detected for key '{key}'. Original value: '{merged_dict[key]}', New value: '{value}'.")
            print(f"  Walrus operator assigned 'key in merged_dict' to 'conflict_exists': {conflict_exists}")
        merged_dict[key] = value
    print(f"Merged dictionary: {merged_dict}")
    return merged_dict

if __name__ == "__main__":
    print("--- Demonstration of Set for Duplicate Removal ---")
    my_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
    remove_duplicates_with_sets(my_list)
    print("\n" + "="*50 + "\n")
    print("--- Demonstration of Dictionary for Word Frequency Counting ---")
    my_text = "This is a sample text. This text is just a sample."
    count_word_frequency(my_text)
    print("\n" + "="*50 + "\n")
    print("--- Demonstration of Dictionary Merging with Walrus Operator ---")
    dict_a = {"name": "Alice", "age": 30, "city": "New York"}
    dict_b = {"age": 32, "occupation": "Engineer", "city": "San Francisco"}
    merge_dictionaries(dict_a, dict_b)
    print("\n--- Another example for merging dictionaries ---")
    dict_x = {"a": 1, "b": 2}
    dict_y = {"b": 3, "c": 4}
    merge_dictionaries(dict_x, dict_y)
