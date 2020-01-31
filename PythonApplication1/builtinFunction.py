print("====== abs ======")
print(abs(3))
print(abs(-3))
print(abs(-1.2))

print("====== all or any ======")
# parameter must be iterable (can be used with for loop) : list, type, string, dictionary and group
# then, check each item is true or false
print(all([1, 2, 3])) 
print(all([1, 2, 3, 0])) # must be all true, otherwise return false
print(any([1, 2, 3, 0])) # any one of true, then return true
print(any([0, ""]))

print("====== chr ======")
# ascii to char
print(chr(97))
print(chr(48))

print("====== ord ======")
# char to ascii
print(ord('a'))

print("====== dir ======")
# show object's variable and function
print(dir([1, 2, 3]))
print(dir({'1':'a'}))

print("====== divmod ======")
# value and remain: return type of tuple
print(divmod(7, 3))
print(divmod(1.3, 0.2))

print("====== enumerate ======")
# return index number of tuple, list and string : even "index number"
for i, name in enumerate(['body', 'foo', 'bar']):
    print (i, name)

print("====== eval ======")
# eval(expression): "expression" means "executable string"
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

print("====== filter ======")
# positive function can be replaced with filter built-in functions
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))

# above positive function can be replaced with ...
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print("====== hex ======")
# hex
print(hex(234))

print("====== id ======")
# id : object reference memory address
a = 3
b = a
print(id(3))
print(id(a))
print(id(b))

print("====== input ======")
# input
a = input() #input()
print(a)

print("====== int ======")
# int
print(int('3'))
print(int(3.4))

print("======== isinstance ========")
# isinstance
class Person: pass
a = Person()
b = 3

print(isinstance(a, Person))
print(isinstance(b, Person))

print("======== lambda ========")
# lambda is same as "def" keyword. It is used to make simple function
sum = lambda a, b: a + b
print(sum(3, 4))

myList = [lambda a,b:a+b, lambda a,b:a*b] # in this case, even def cannot be used
print(myList)
print(myList[0](3,4))
print(myList[1](8,4))

print("======== len ========")
# len
print(len("python"))
print(len([1,2,3]))

print("======== list ========")
# list
print(list("python"))
print(list((1,2,3)))
a = [1, 2, 3]
b = list(a)
print(b)

print("======== map ========")
# map
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

# -->> change using map -->> in terms of processing parameters, it is very similar to "filter"
def two_times(x): return x*2
print(list(map(two_times, [1,2,3,4])))

# even simpler
print(list(map(lambda a: a*2, [1, 2, 3, 4])))

print("======== max ========")
# max
print(max([1, 2, 3]))

print("======== min ========")
# min
print(min("python"))

print("======== oct ========")
# oct
print(oct(12345))

print("======== open ========")
#open : file open : refer to "fileHandling.py"

print("======== pow ========")
#pow
print(pow(2, 4))
print(2 ** 4) # same as pow

print("======== range ========")
#range: make iterable object NOTE: very last number is excluded
print(list(range(5)))
print(list(range(4,7)))
print(list(range(1, 10, 2)))  # 3rd parameter is distance between numbers

print("======== round ========")
# round
print(round(4.5464678,6))
print(round(4.5464674,6))
print(round(54.6))
print(round(54.1))

print("======== sorted ========")
# sorted
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))

print("======== sort ========")
a = [3, 1, 2]
result = a.sort() # NOTE: it does not return anything
print(result)
print(a) # By doing this, we can know

print("======== str ========")
#str
print(str(3))
print(str('hi'.upper()))

print("======== sum ========")
print(sum(12,23))
print(sum([12,23],[45]))

print("======== tuple ========")
#tuple
print(tuple("abc"))
print(tuple([1, 2, 3]))

print("======== type ========")
#type
print(type("abc"))
print(type([ ]))
print(type(open("test", 'w')))

print("======== zip ========")
#zip : same index value of each list (or iterable value type) would be combined.
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))

# NOTE: if index does not match, it is ignored
print(list(zip([1, 2, 3], [4, 5, 6, 11])))