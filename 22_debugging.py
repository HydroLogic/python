import random

def f(a_list):
    element_i = random.randint(0, len(a_list))
    #print element_i
    element = a_list[element_i]
    #print element_i, element

a_list = 'ya see i go by the code of the doctor of the mix'.split()
for i in xrange(100):
    f(a_list)
