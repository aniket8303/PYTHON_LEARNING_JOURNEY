# Q) Write a program to fill in a letter template given below with name and date.
letter ='''Dear <|Name|>,
You are selected!
<|Date|>'''



# letter = "Dear " + name + ",\nYou are selected!\n" + date

print(letter.replace("<|Name|>","Aniket").replace("<|Date|>","24 September 2050"))