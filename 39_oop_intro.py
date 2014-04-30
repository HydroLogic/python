class Person:
    # Method = function declared within a class block
    # First positional parameter is always the instance, traditionally named "self" (vs. "this" in Java or C++)
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return self.first_name + ' ' + self.last_name

me = Person('Minor', 'Gordon') # Create/"instantiate" Person
                               # Implicitly calls Person.__init__(me, 'Minor', 'Gordon')
# me is an "instance" of Person
print me.get_name() # ~ calling Person.get_name(me)
# The dot syntax just means "access a method or a data member on an instance"
print me.first_name
