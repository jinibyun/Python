"""
# Module can contain not only functions but also classes, constants, variables, etc.

PI = 3.1241592
class Math:
    def solv(self, r): # width of circle
        return PI * (r ** 2)

def sum (a, b):
    return a + b

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))

# How to use it from python console (external use)
# 1. print(module2.PI)
# 2. a = module2.Math()
#    print(a.solv(2))
# 3. print(module2.sum(module2.PI, 4.4))
"""