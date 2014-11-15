i = 1
print 'Integer class', i.__class__
print 'Integer class name', i.__class__.__name__
print 'Integer class module', i.__class__.__module__
class MyType(object):
    pass
print 'MyType module', MyType().__class__.__module__
print 'MyType module name (not the module object!)', MyType.__module__
import sys
print 'MyType file', sys.modules[MyType.__module__]
print 'MyType methods:'
for method_name in dir(MyType()):
    print method_name