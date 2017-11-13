# module 
# a group of functions, variables and classes

def sum(a, b):
    return a + b
def safe_sum(a, b): 
    if type(a) != type(b): 
        print("You cannot add")
        return 
    else: 
        result = sum(a, b) 
    return result

print(safe_sum(2,"3"))

# way of test
# open console and move to directory of this file and type
# import module1
# print(module1.sum(3,4))

