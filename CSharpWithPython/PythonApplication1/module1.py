# module 
# a group of functions, variables and classes
# NOTE: their is NO keyword for module. It is conceptual thing.

def sum(a, b):
    return a + b
def safe_sum(a, b): 
    if type(a) != type(b): 
        print("You cannot add")
        return 
    else: 
        result = sum(a, b) 
    return result

if __name__ == "__main__": # It means that following statement will be only executed when it is called directly. If this module is called externally, it will NOT be executed.
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))

# way of test
# open console and move to directory of this file and type
# import module1
# print(module1.sum(3,4))

