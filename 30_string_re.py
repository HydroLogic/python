# Regular expressions
# https://docs.python.org/2/library/re.html

import re

print re.match("\d", "ab1def") # No match, since it must be the whole string
print re.match("\w+\d\w{3}", "ab1def")
print re.match("\w+(\d)\w{3}", "ab1def").groups()
print re.search("\d", "ab1def").start()
print re.split("\d", "abc1def")
print re.sub("\d", "2", "abc1def")
# Multi-line matches, raw strings to avoid \ escaping, etc.