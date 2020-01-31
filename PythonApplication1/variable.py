print(type(3))

a = 3
b = 3
print(a is b)

import sys
print(sys.getrefcount(3))

# way to define variables

a, b = ('python', 'life') # same as (a, b) = 'python', 'life'

print(a)
print(b)

[a,b] = ['python2', 'life2']
print(a)

# change
a = 3
b = 5
a, b = b, a
print(a)
print(b)

# garbage collection: automatic, but if need to delete by manual
a = 3
b = 3
del(a)
del(b)

# list copy

a = [1, 2 ,3]
b = a
a[1] = 4
print(a)
print(b)

from copy import copy
b = copy(a) # same as b = a[:]

print(b is a)