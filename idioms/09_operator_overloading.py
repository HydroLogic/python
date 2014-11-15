# See the operator module for the list of available operators
# https://docs.python.org/2/library/operator.html

class MyTypeWithEqOperator(object):
    def __init__(self, x):
        if not isinstance(x, int):
            raise TypeError(type(x))
        self.x = x

    def __eq__(self, other):
        '''
        Override the == comparison operator
        '''
        if not isinstance(other, MyTypeWithEqOperator):
            return False
        return self.x == other.x

class MyTypeWithoutEqOperator(object):
    def __init__(self, x):
        self.x = x

# The classic use case is complex numbers.

# The default == compares object ids
print 'Equals with overloaded operator', MyTypeWithEqOperator(1) == MyTypeWithEqOperator(1)
print 'Equals without overloaded operator', MyTypeWithoutEqOperator(1) == MyTypeWithoutEqOperator(1)
# because
left = MyTypeWithoutEqOperator(1)
right = MyTypeWithoutEqOperator(1)
print "%s != %s is %s" % (id(left), id(right), id(left) != id(right))


class MyTypeWithAddOperator(object):
    def __init__(self, x):
        if not isinstance(x, int):
            raise TypeError(type(x))
        self.x = x

    def __add__(self, other):
        if isinstance(other, MyTypeWithAddOperator):
            return self.x + other.x
        elif isinstance(other, int):
            return MyTypeWithAddOperator(self.x + other)
        else:
            raise TypeError(type(other))

    def __repr__(self):
        '''
        Return a string containing a printable representation of an object.
        For many types, this function makes an attempt to return a string
        that would yield an object with the same value when passed to eval(),
        '''
        return "%s(%s)" % (self.__class__.__name__, self.x)

print 'Result', MyTypeWithAddOperator(1) + 2
# Why doesn't this work? And how can we make it work?
# print 2 + MyTypeWithAddOperator(1)
