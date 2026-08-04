
# 8. If languages of two friends are same; what will happen to the program in problem
# 6?

d = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")

d.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")

d.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")

d.update({name:lang})

print(d)

#Nothing will be happens the value can be change