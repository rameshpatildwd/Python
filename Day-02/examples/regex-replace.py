import re       #importing regex module

text = "Red is John's fav colour"
pattern = r"Red"                                    #The r before a string in Python (e.g., r"quick") makes it a raw string literal

replacement = "Yellow"

new_text = re.sub(pattern, replacement, text)       #substitutes the color
print(new_text)

#example2
name = "His name is John"
pattern1 = r"John"

replacement1 = "Dave"
new_name = re.sub(pattern1, replacement1, name)     #substitues name
print(new_name)

#example3 
city = "I am from Banglore"
pattern2 = r"Banglore"
replacement2 = "Delhi"
new_city = re.sub(pattern2, replacement2, city)
print(new_city)