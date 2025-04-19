text = "  Some spaces around  "
stripped_text = text.strip()            #strip function will remove spaces at start and end only
print("Stripped text:", stripped_text)

text2 = "______Hello___"
stripped_text2 = text2.strip("_")       #removes the ___ at start and end
print(stripped_text2)