name = "harry are"

print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))
print(name.capitalize())




# ============================================================
#                MOST-USED PYTHON STRING METHODS
# ============================================================


# 1. upper()
# Purpose: Convert string to uppercase
text = "hello"
print(text.upper())          # HELLO


# 2. lower()
# Purpose: Convert string to lowercase
text = "HELLO"
print(text.lower())          # hello


# 3. strip()
# Purpose: Remove spaces from both ends
text = " hello "
print(text.strip())          # hello


# 4. replace()
# Purpose: Replace part of a string
text = "hello"
print(text.replace("h", "H"))    # Hello


# 5. split()
# Purpose: Split a string into a list
text = "a,b,c"
print(text.split(","))       # ['a', 'b', 'c']


# 6. join()
# Purpose: Join multiple strings together
items = ["a", "b", "c"]
print("-".join(items))       # a-b-c


# 7. find()
# Purpose: Find the index of the first occurrence of a substring
text = "hello"
print(text.find("l"))        # 2


# 8. count()
# Purpose: Count occurrences of a substring
text = "banana"
print(text.count("a"))       # 3


# 9. startswith()
# Purpose: Check whether a string starts with specified text
text = "hello"
print(text.startswith("he"))     # True


# 10. endswith()
# Purpose: Check whether a string ends with specified text
text = "file.py"
print(text.endswith(".py"))      # True


# 11. capitalize()
# Purpose: Capitalize the first character of the string
text = "hello world"
print(text.capitalize())     # Hello world


# 12. title()
# Purpose: Capitalize the first character of each word
text = "hello world"
print(text.title())          # Hello World


# 13. isdigit()
# Purpose: Check whether all characters are digits
text = "123"
print(text.isdigit())        # True


# 14. isalpha()
# Purpose: Check whether all characters are alphabetic
text = "hello"
print(text.isalpha())        # True


# 15. isalnum()
# Purpose: Check whether all characters are letters or numbers
text = "abc123"
print(text.isalnum())        # True


# 16. isspace()
# Purpose: Check whether all characters are whitespace
text = " "
print(text.isspace())        # True


# ============================================================
# BONUS: len()
# len() is a built-in Python function, NOT a string method.
# Purpose: Find the number of characters in a string
# ============================================================

text = "Aniket"
print(len(text))             # 6