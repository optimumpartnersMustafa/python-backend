
my_list = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print("Original List:", my_list)

my_list.sort()
print("Sorted List (ascending):", my_list)

my_list.sort(reverse=True)
print("Sorted List (descending):", my_list)

another_list = [10, 4, 12, 6, 8]
sorted_another_list = sorted(another_list)
print("Original another_list:", another_list)
print("Sorted another_list (new list):", sorted_another_list)

print("-" * 30)

filtered_list = [x for x in my_list if x > 5]
print("List filtered (numbers > 5):", filtered_list)

even_numbers = [x for x in my_list if x % 2 == 0]
print("List filtered (even numbers):", even_numbers)

print("-" * 30)

transformed_list = [x * 2 for x in my_list]
print("List transformed (each number doubled):", transformed_list)

string_list = [str(x) for x in my_list]
print("List transformed (numbers to strings):", string_list)

print("\n" + "=" * 40 + "\n")

#--------------------------------------------------------------------------------
my_tuple = (5, 2, 8, 1, 9, 3, 7, 4, 6)
print("Original Tuple:", my_tuple)

sorted_tuple_as_list = sorted(my_tuple)
print("Sorted Tuple (as a new list):", sorted_tuple_as_list)

sorted_tuple = tuple(sorted(my_tuple))
print("Sorted Tuple (as a new tuple):", sorted_tuple)

print("-" * 30)

filtered_tuple_as_list = [x for x in my_tuple if x < 5]
print("Tuple filtered (numbers < 5, as list):", filtered_tuple_as_list)

filtered_tuple = tuple(x for x in my_tuple if x < 5)
print("Tuple filtered (numbers < 5, as tuple):", filtered_tuple)

print("-" * 30)

transformed_tuple_as_list = [x + 10 for x in my_tuple]
print("Tuple transformed (each number + 10, as list):", transformed_tuple_as_list)

transformed_tuple = tuple(x + 10 for x in my_tuple)
print("Tuple transformed (each number + 10, as tuple):", transformed_tuple)
