text = "Python is a programming language"

def length():
    length = len(text)
    print(length)

def substitutes():
    new_text = text.replace("programming", "Dynamically typed") 
    print(new_text)
    
def case_sensitive():
    upper = text.upper()
    lower = text.lower()
    print("Upper case:", upper)
    print("Lower case:", lower)

def concat():
    text1 = "Hello,"         #Local vars
    text2 = "How are you?"  #Local vars
    concat = text1 + " " + text2
    print(concat)

def splitting():
    divided_words = text.split()
    print(divided_words)

def sub_string():
    sub_string = "Python"
    if sub_string in text:
        print(sub_string, "is present in", text)
    else:
        print(sub_string, "not found in", text)

length()
substitutes()
case_sensitive()
concat()
splitting()
sub_string()
