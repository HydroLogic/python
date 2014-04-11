# Split a string into a list of strings

# Split on commas
# Note that the separator is NOT included in the resulting strings.
print "Year,University Name,Student Classification,Resident Status,Headcount".split(',')

# Split on commas, maximum 2 splits i.e. the sequence will contain at most 3 elements
print "Year,University Name,Student Classification,Resident Status,Headcount".split(',', 2)
print "Year,University Name".split(',', 2) # Only one split possible

# Split on whitespace, separator = any amount of whitespace (\d+)
print "Hello, world".split()
print "Hello,  world".split()

# Split on multiple characters. Entire separator must match.
print "Hello, world".split(', ')