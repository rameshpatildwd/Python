#Defining a tuple
admins = ("Ram", "Shyam", "Anil", "Shankar", "Jayant")
print(f"List of Admins: {admins}")

#To print a specific element from a tuple use indexing
print(f"First admin in the list of tuple is: {admins[0]}")
print(f"Last admin in the list of tuple is: {admins[-1]}")

#To check number of elements within a tuple use `len`
print(f"Number of Admins in the tuple are = {len(admins)}")

#Cannot use `append` attribute in Tuples as they are immutable in nature
#admins.append("Sahana")     #throws an AttributeError
#print(admins)      

#Cannot use `remove` attribute in Tuples as they are immutable in nature
#admins.remove("Sahana")     #throws an AttributeError
#print(admins)

#To create a sub list from a tuple
main_admins = admins[0:3]       #called as slicing
print(f"Main admins are: {main_admins}")

#To view the Data type
print(f"The data type of admins variable is: {type(admins)}")

#To check if a element is present in Tuple
is_present = 'Ram'.lower() in [admin.lower() for admin in admins]
print(is_present)
