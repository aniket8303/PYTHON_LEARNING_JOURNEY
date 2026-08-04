friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]

print(friends)

friends.append("Harry")

print(friends)

friends.reverse()
print(friends)


l1 = [1,2,32,45,344,64,6,77,22]

# l1.sort()
# l1.reverse()
# l1.insert(2,33333)
# print(l1.pop(2))
l1.remove(344)
print(l1)




# ============================================================
#               MOST-USED PYTHON LIST METHODS
# ============================================================


# Sample List
numbers = [10, 20, 30, 40, 50]


# 1. append()
# Purpose: Add an element to the end of the list

numbers.append(60)
print(numbers)

# Output:
# [10, 20, 30, 40, 50, 60]


# 2. insert()
# Purpose: Insert an element at a specific index

numbers.insert(2, 25)
print(numbers)

# Output:
# [10, 20, 25, 30, 40, 50, 60]


# 3. extend()
# Purpose: Add multiple elements to the end of the list

numbers.extend([70, 80, 90])
print(numbers)

# Output:
# [10, 20, 25, 30, 40, 50, 60, 70, 80, 90]


# 4. remove()
# Purpose: Remove the first occurrence of a value

numbers.remove(25)
print(numbers)

# Output:
# [10, 20, 30, 40, 50, 60, 70, 80, 90]


# 5. pop()
# Purpose: Remove and return an element

numbers.pop()
print(numbers)

# Output:
# [10, 20, 30, 40, 50, 60, 70, 80]


# Remove element at index 2
numbers.pop(2)
print(numbers)

# Output:
# [10, 20, 40, 50, 60, 70, 80]


# 6. clear()
# Purpose: Remove all elements from the list

temp = [1, 2, 3]
temp.clear()
print(temp)

# Output:
# []


# 7. index()
# Purpose: Find the index of an element

numbers = [10, 20, 30, 40, 50]
print(numbers.index(30))

# Output:
# 2


# 8. count()
# Purpose: Count occurrences of an element

numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))

# Output:
# 3


# 9. sort()
# Purpose: Sort the list in ascending order

numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)

# Output:
# [10, 20, 30, 40, 50]


# Sort in descending order
numbers.sort(reverse=True)
print(numbers)

# Output:
# [50, 40, 30, 20, 10]


# 10. reverse()
# Purpose: Reverse the order of elements

numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)

# Output:
# [40, 30, 20, 10]


# 11. copy()
# Purpose: Create a copy of a list

numbers = [10, 20, 30]
new_list = numbers.copy()

print(new_list)

# Output:
# [10, 20, 30]


# ============================================================
#                USEFUL BUILT-IN FUNCTIONS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(len(numbers))      # 5
print(max(numbers))      # 50
print(min(numbers))      # 10
print(sum(numbers))      # 150

# ============================================================
#               MOST IMPORTANT TO REMEMBER
# ============================================================

# append()   -> Add one element
# insert()   -> Insert at specific position
# extend()   -> Add multiple elements
# remove()   -> Remove by value
# pop()      -> Remove by index
# clear()    -> Remove all elements
# index()    -> Find index
# count()    -> Count occurrences
# sort()     -> Sort list
# reverse()  -> Reverse list
# copy()     -> Copy list