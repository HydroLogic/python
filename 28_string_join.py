# Join a sequence of strings into a single string
# Inverse operation of .split()
# Syntax: <separator string>.join(sequence of strings)

print ','.join(['Year', 'University Name'])

print ''.join(['Hello, ', 'world'])

print ', '.join(('Hello', 'world')) # Tuple instead of a list

# Won't work, because range(10) produces a list of numbers, not strings
# print ','.join(range(10))
print ','.join(str(i) for i in xrange(10)) # List comprehension

# Capitalize every word in a sentence
sentence = 'this is an uncapitalized sentence'
print ' '.join(word.capitalize() for word in sentence.split())

# Capitalize every other letter
word = 'longword'
print ''.join((c.upper()) if i % 2 == 0 else c
               for i, c in enumerate(word))
