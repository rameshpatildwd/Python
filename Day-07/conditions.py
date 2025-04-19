import sys      #to read command line args

#instance_type = sys.argv[1]     #takes input as command line arg

# Prompt user input on a new line
instance_type = input("Enter the type of instance:\n").lower()    #asks for input from user, .lower will make input case insensitive

if instance_type == "t2.micro":                 
    print(f"{instance_type} will cost you 2$/day")

elif instance_type == "t2.medium":
    print(f"{instance_type} will cost you 4$/Day")

elif instance_type == "t2.large":
    print(f"{instance_type} will cost you 6$/Day")

elif instance_type == "t2.xlarge":
    print(f"{instance_type} will cost you 10$/Day")

else:
    print(f"{instance_type} is not a valid type")

