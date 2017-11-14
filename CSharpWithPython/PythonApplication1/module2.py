# Module can contain class, variable, etc.

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
