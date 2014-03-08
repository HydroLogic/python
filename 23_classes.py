# A very brief overview

class SomeClass(object): # Inherit the root class, object
    # Method = function declared within a class block
    # First positional parameter is always the instance, traditionally named "self" (vs. "this" in Java or C++)
    def __init__(self, someparam):
        self.CONSTANT = 3.14
        self.public = 'test'
        self.someparam = someparam

    def get_someparam_plus_1(self):
        return self.someparam + 1

x = SomeClass(1) # Create/"instantiate" SomeClass
                 # Implicitly calls the methods __init__(x, 1)
# x is an "instance" of SomeClass
x.get_someparam_plus_1() # Conceptually like calling SomeClass.get_someparam_plus_1(x)
# The dot syntax just means "access a method or a data member on an instance"
x.CONSTANT # Not a method, just a variable attached to the instance
x.public

# So when you see 'class datetime' here:
# http://docs.python.org/2/library/datetime
# Calling datetime.now() creates an instance of the datetime class
# Then you access it with some_datetime.year, etc., just like x. above
