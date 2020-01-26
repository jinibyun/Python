# NOTE: how to execut following
# In command prompt, python sys1.py life is too short, you need python
import sys

args = sys.argv[1:] # argv[] : parameters from command prompt / argv[0] means file name.
for i in args:
    print(i.upper(), end = " ")

