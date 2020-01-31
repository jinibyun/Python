print("=========== varialbe memory ===========")

a = [1,2,3]
id(a) #memory address

# memory address copy
b = a
id(b)

# same address check means if they point to same object
a is b

a[1] = 4
a

b

# how to point to another object keeping same value of a

# 1. First method
a = [1,2,3]
b = a[:]  #[:] means all of list values. NOTE: Here we are copying values (not memory address)

a[1] = 4 # just change

# check they are DIFFERENT
print (a)
print (b)

# 2. Second Method
from copy import copy  # from copy "module", import copy "function"
b = copy(a)

a is b

print("=========== ways to define variables ===========")
a, b = ('python', 'life')  # same as (a,b) = 'python', 'life'     a, b = 'python', 'life'      In tuple, ( ) can be always skipped
print(a)
print(b)

[a,b] = ['python','life']
print(a)
print(b)

a = b = 'python'
a is b

# value change
a = 3
b = 5
a, b = b, a
print(a)
print(b)


