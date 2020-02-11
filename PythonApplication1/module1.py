print("=========== module =========== ")
# module
# a group of functions, variables and classes
# NOTE: their is NO keyword for module. It is conceptual thing.
# All files whole extension is .py is "module"

def sum(a, b):
    return a + b
def safe_sum(a, b): 
    if type(a) != type(b): 
        print("You cannot add")
        return 
    else: 
        result = sum(a, b) 
    return result

# It means that following statement will be only executed when it is called directly.
# e.g -->> python module1.py
# If this module is called externally (to import module), it will NOT be executed.
if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))

# way of test
# open console and move to directory of this file and type

# 1
# import module1
# print(module1.sum(3,4))

# 2
# from module1 import sum, safe_sum
# print(sum(3,4))
# print (safe_sum("a", 1))

# 3
# from module1 import *
