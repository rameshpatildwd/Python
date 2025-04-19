#Use cases of inbuilt string handling functions 

arn = "arn:aws:iam::123456789012:user/johndoe"
print(arn.split("/")[1])    #prints only user name from arn


name = "Ramesh Patil"
print(name.split(" ")[0])   #splitting to print 1st name
print(name.split(" ")[1])   #splitting to print 2nd name
print(name.upper())         #convert to upper case
print(name.lower())         #convert to lower case
print(len(name))            #to print length of a string
