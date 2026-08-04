s = {2, 4, 2, 3, 4, 2,45, 2,34, 7 , "Harry"}

print(s , type(s))


s.add(566)

print(s, type(s))



# ============================================
# PYTHON SET METHODS
# ============================================

# Sample Set
fruits = {"apple", "banana", "mango"}

print("Original Set:")
print(fruits)


# ============================================
# 1. add()
# Adds one element to the set.
# ============================================

print("\n1. add()")

fruits.add("orange")

print(fruits)


# ============================================
# 2. update()
# Adds multiple elements from another iterable.
# ============================================

print("\n2. update()")

fruits.update(["grapes", "kiwi"])

print(fruits)


# ============================================
# 3. remove()
# Removes an element.
# Raises KeyError if element is not found.
# ============================================

print("\n3. remove()")

fruits.remove("banana")

print(fruits)


# ============================================
# 4. discard()
# Removes an element.
# Does NOT raise an error if element is absent.
# ============================================

print("\n4. discard()")

fruits.discard("pineapple")   # No error

print(fruits)


# ============================================
# 5. pop()
# Removes and returns a random element.
# ============================================

print("\n5. pop()")

item = fruits.pop()

print("Removed:", item)
print(fruits)


# ============================================
# 6. clear()
# Removes all elements.
# ============================================

print("\n6. clear()")

temp = fruits.copy()

temp.clear()

print(temp)


# ============================================
# 7. copy()
# Creates a copy of the set.
# ============================================

print("\n7. copy()")

new_set = fruits.copy()

print(new_set)


# ============================================
# 8. union()
# Combines two sets.
# ============================================

print("\n8. union()")

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))


# ============================================
# 9. intersection()
# Returns common elements.
# ============================================

print("\n9. intersection()")

print(set1.intersection(set2))


# ============================================
# 10. difference()
# Returns elements in first set only.
# ============================================

print("\n10. difference()")

print(set1.difference(set2))


# ============================================
# 11. symmetric_difference()
# Returns elements that are in either set,
# but NOT in both.
# ============================================

print("\n11. symmetric_difference()")

print(set1.symmetric_difference(set2))


# ============================================
# 12. issubset()
# Checks if one set is a subset of another.
# ============================================

print("\n12. issubset()")

A = {1,2}
B = {1,2,3,4}

print(A.issubset(B))


# ============================================
# 13. issuperset()
# Checks if one set contains another set.
# ============================================

print("\n13. issuperset()")

print(B.issuperset(A))


# ============================================
# 14. isdisjoint()
# Returns True if both sets have no common elements.
# ============================================

print("\n14. isdisjoint()")

X = {1,2}
Y = {3,4}

print(X.isdisjoint(Y))