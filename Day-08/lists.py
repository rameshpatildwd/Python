#Defining a list
fruits = ["Banana", "Apple", "Pineapple", "Strawberry", "Orange"]
print(f"List of Fruits: {fruits}")

#To print a specific element from a list use indexing
print(f"First fruit in the list: {fruits[0]}")    #prints 1st element
print(f"Last fruit in the list: {fruits[-1]}")    #prints last element

#To check number of elements within a list use `len`
print(f"Number of fruits/elements within Fruits list = {len(fruits)}")

#To add new element to a list use `append`
fruits.append("Cherry")
print(fruits)

#To remove an element from a list use `remove`
fruits.remove("Cherry")
print(fruits)

#To create a sub list from a list
sub_fruits = fruits[0:2]        #called as slicing
print(f"This is a sub list from main fruit list: {sub_fruits}")

#To view the Data type
print(f"The data type of fruits variable is {type(fruits)}")

#To check if an element is present in a list
is_present = 'banana' in [fruit.lower() for fruit in fruits]    #`lower` to make case insensitive   
print(f"Banana is present in list: {is_present}")