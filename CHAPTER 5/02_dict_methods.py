marks = {
  "Harry": 100,
  "Shubham": 56,
  "Rohan": 23,
  0: "Harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry" : 99})
# print(marks)
# marks.update({"Renuka":88})
# print(marks)

# print(marks.get(0))

# print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"])# Returns an error



# ============================================
# PYTHON DICTIONARY METHODS
# ============================================

# Sample Dictionary
student = {
    "name": "Aniket",
    "age": 21,
    "city": "Pune"
}

print("Original Dictionary:")
print(student)

# ============================================
# 1. get()
# Returns the value of a key.
# If the key does not exist, it returns None
# (or a default value if provided).
# ============================================

print("\n1. get()")
print(student.get("name"))          # Aniket
print(student.get("marks"))         # None
print(student.get("marks", 0))      # 0


# ============================================
# 2. keys()
# Returns all keys in the dictionary.
# ============================================

print("\n2. keys()")
print(student.keys())


# ============================================
# 3. values()
# Returns all values in the dictionary.
# ============================================

print("\n3. values()")
print(student.values())


# ============================================
# 4. items()
# Returns key-value pairs as tuples.
# Useful in loops.
# ============================================

print("\n4. items()")
print(student.items())

for key, value in student.items():
    print(key, ":", value)


# ============================================
# 5. update()
# Adds new key-value pairs or updates existing ones.
# ============================================

print("\n5. update()")

student.update({"age": 22})
student.update({"country": "India"})

print(student)


# ============================================
# 6. pop()
# Removes a key and returns its value.
# ============================================

print("\n6. pop()")

city = student.pop("city")

print("Removed:", city)
print(student)


# ============================================
# 7. popitem()
# Removes the last inserted key-value pair.
# ============================================

print("\n7. popitem()")

item = student.popitem()

print("Removed:", item)
print(student)


# ============================================
# 8. copy()
# Creates a copy of the dictionary.
# ============================================

print("\n8. copy()")

new_student = student.copy()

print(new_student)


# ============================================
# 9. clear()
# Removes all elements from the dictionary.
# ============================================

print("\n9. clear()")

temp = student.copy()

temp.clear()

print(temp)


# ============================================
# 10. setdefault()
# Returns the value of the key.
# If the key doesn't exist, it inserts the key
# with the given default value.
# ============================================

print("\n10. setdefault()")

student.setdefault("marks", 90)

print(student)

student.setdefault("age", 25)   # age already exists

print(student)


# ============================================
# 11. fromkeys()
# Creates a new dictionary using given keys
# with the same default value.
# ============================================

print("\n11. fromkeys()")

subjects = ["Python", "Java", "SQL"]

marks = dict.fromkeys(subjects, 0)

print(marks)