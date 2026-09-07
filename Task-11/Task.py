arr = [10, 20, 30, 40, 50]

for i in arr:
    print(i)


    arr = [10, 20, 30, 40, 50]

total = 0

for i in arr:
    total = total + i

print("Sum =", total)

arr = [10, 25, 5, 40, 15]

print("Maximum =", max(arr))
print("Minimum =", min(arr))


arr = [10, 20, 30, 40, 50]

position = int(input("Enter position: "))
element = int(input("Enter new element: "))

arr.insert(position, element)

print("Updated array:", arr)


arr = [10, 20, 30, 40, 50]

element = int(input("Enter element to delete: "))

if element in arr:
    arr.remove(element)
    print("Updated array:", arr)
else:
    print("Element not found")


    arr = [10, 20, 30, 40, 50]

index = int(input("Enter index: "))
element = int(input("Enter new element: "))

arr[index] = element

print("Updated array:", arr)


arr = [10, 20, 30, 40, 50]

element = int(input("Enter element to search: "))

if element in arr:
    print("Index =", arr.index(element))
else:
    print("Element not found")


    arr1 = [10, 20, 30]
arr2 = [40, 50, 60]

arr3 = arr1 + arr2

print("Concatenated array:", arr3)


arr = [50, 20, 40, 10, 30]

arr.sort()

print("Sorted list:", arr)