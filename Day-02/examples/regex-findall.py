import re

name = "RameshPatil"
parts = re.findall('[A-Z][a-z]*', name)
print(parts)
print(parts[0])
print(parts[1])


# re.findall() → Finds all matches in the string.

# '[A-Z]' → Matches one uppercase letter (A-Z). 

# '[a-z]*' → Matches zero or more lowercase letters (a-z).

# * means zero or more repetitions.