def find_second_largest(numbers):
    if not isinstance(numbers, list):
        print("Error: Input must be a list.")
        return None

    unique_numbers = sorted(list(set(numbers)))

    if len(unique_numbers) < 2:
        print("The list must contain at least two unique numbers.")
        return None
    else:
        return unique_numbers[-2]

def merge_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        print("Error: Both inputs must be dictionaries.")
        return None

    merged_dict = dict1 | dict2
    return merged_dict

print("--- Finding the Second-Largest Number ---")
my_list1 = [10, 5, 20, 15, 25, 20]
second_largest1 = find_second_largest(my_list1)
if second_largest1 is not None:
    print(f"Original list: {my_list1}")
    print(f"The second-largest number is: {second_largest1}")
print("-" * 30)

my_list2 = [7, 7, 7, 7]
second_largest2 = find_second_largest(my_list2)
if second_largest2 is not None:
    print(f"Original list: {my_list2}")
    print(f"The second-largest number is: {second_largest2}")
print("-" * 30)

my_list3 = [42]
second_largest3 = find_second_largest(my_list3)
if second_largest3 is not None:
    print(f"Original list: {my_list3}")
    print(f"The second-largest number is: {second_largest3}")
print("-" * 30)

my_list4 = []
second_largest4 = find_second_largest(my_list4)
if second_largest4 is not None:
    print(f"Original list: {my_list4}")
    print(f"The second-largest number is: {second_largest4}")
print("-" * 30)

print("\n--- Merging Dictionaries ---")
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'c': 4, 'd': 5, 'e': 6}

merged_result = merge_dictionaries(dict_a, dict_b)
if merged_result is not None:
    print(f"Dictionary A: {dict_a}")
    print(f"Dictionary B: {dict_b}")
    print(f"Merged Dictionary (A | B): {merged_result}")
print("-" * 30)

dict_x = {'name': 'Alice', 'age': 30}
dict_y = {'city': 'New York', 'age': 31, 'occupation': 'Engineer'}

merged_result2 = merge_dictionaries(dict_x, dict_y)
if merged_result2 is not None:
    print(f"Dictionary X: {dict_x}")
    print(f"Dictionary Y: {dict_y}")
    print(f"Merged Dictionary (X | Y): {merged_result2}")
print("-" * 30)
