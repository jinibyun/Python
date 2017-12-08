########################
# BASIC
########################

import sys
sys.path.insert(0, 'C:\Program Files (x86)\IronPython 2.7\Tutorial') # to import another module from another directory
import first

print("========version=========")
print(sys.version)

print("========contents of sys module=========")
print(dir(sys))

print("========contents of sys module attribute========")
print(sys.path)
print(sys.executable)


print("==========Explorer first module=======")
print(dir(first))

print("====using __doc__ attribute, print function ")
print(first.add.__doc__)
print(first.factorial.__doc__)

print("====call external module's function ")
print(first.add(1,2))
print(first.hi)
print(first.factorial(5))