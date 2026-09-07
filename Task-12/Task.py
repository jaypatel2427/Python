# Q.1 Find and print the index of the maximum and minimum values.

my_list = [34, 47, 89, 3, 23, 15, 4]

max_val = max(my_list)
min_val = min(my_list)

max_index = my_list.index(max_val)
min_index = my_list.index(min_val)

print("List:", my_list)
print("Index of maximum value (", max_val, ") is:", max_index)
print("Index of minimum value (", min_val, ") is:", min_index)


# Q.2 Compute and print the cumulative sum of the array

my_Arr = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

my_Arr_copy = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

for i in range(0, len(my_Arr)):
    for j in range(0, len(my_Arr[i])):
        if i == 0:
            my_Arr_copy[i][j] = my_Arr[i][j]
        else:
            my_Arr_copy[i][j] = my_Arr[i][j] + my_Arr_copy[i-1][j]

print("Cumulative Sum Array:")
for element in my_Arr_copy:
    print(element)

print("\n# " + "="*73)


# Q.3 Find the unique elements and their frequency count in an array

my_list = [34, 47, 89, 34, 3, 23, 15, 47, 3, 4]
my_set = set(my_list)

print("Frequency count:")
for element in my_set:
    print(element, "->", my_list.count(element))

print("\n# " + "="*73)


# Q.4 Extract all numbers that are divisible by 3 from the array

print("Numbers divisible by 3:")
for element in my_list:
    if element % 3 == 0:
        print(element)

print("\n# " + "="*73)


# Q.5 Generate the first N Fibonacci numbers and create an array of that. Where, N=User Input

a = 0
b = 1

num = int(input("Enter the Value of N : "))

for i in range(0, num):
    print(a, end=", ")
    c = a + b
    a = b
    b = c
print()