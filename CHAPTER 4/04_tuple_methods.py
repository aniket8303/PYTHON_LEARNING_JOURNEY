a = (1, 45, 342, 3434, 45, False, "Ram", "Shivam")
print(a)

no = a.count(45)
print(no)

i = a.index(45)
print(i)



# ============================================================
#              MOST-USED PYTHON TUPLE METHODS
# ============================================================


# Sample Tuple
numbers = (10, 20, 30, 20, 40, 20, 50)


# 1. count()
# Purpose: Count the number of occurrences of a value

print(numbers.count(20))

# Output:
# 3


# 2. index()
# Purpose: Find the index of the first occurrence of a value

print(numbers.index(30))

# Output:
# 2


# ============================================================
#            IMPORTANT TUPLE OPERATIONS (NOT METHODS)
# ============================================================

numbers = (10, 20, 30, 40, 50)

# Length
print(len(numbers))          # 5

# Maximum value
print(max(numbers))          # 50

# Minimum value
print(min(numbers))          # 10

# Sum of all elements
print(sum(numbers))          # 150

# Membership
print(20 in numbers)         # True
print(100 in numbers)        # False

# Slicing
print(numbers[1:4])          # (20, 30, 40)

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple1 + tuple2)

# Output:
# (1, 2, 3, 4, 5, 6)

# Repetition
print(tuple1 * 3)

# Output:
# (1, 2, 3, 1, 2, 3, 1, 2, 3)


# ============================================================
#             TUPLE PACKING AND UNPACKING
# ============================================================

# Packing
student = ("Aniket", 21, "Pune")

# Unpacking
name, age, city = student

print(name)
print(age)
print(city)

# Output:
# Aniket
# 21
# Pune


# ============================================================
#              MOST IMPORTANT TO REMEMBER
# ============================================================

# Tuple Methods:
# count()  -> Count occurrences of a value
# index()  -> Find index of first occurrence

# Useful Built-in Functions:
# len()
# max()
# min()
# sum()

# Operators:
# +
# *
# in
# not in
# Slicing [:]