print(abs(3))
print(abs(-3))
print(abs(-1.2))

# parameter must be iterable (can be used with for loop) : list, type, string, dictionary and group
# then, check each item is true or false
print(all([1, 2, 3])) 
print(all([1, 2, 3, 0])) # must be all true, otherwise return false
print(any([1, 2, 3, 0])) # any one of true, then return true
print(any([0, ""]))

# ascii to char
print(chr(97))
print(chr(48))

# char to ascii
print(ord('a'))

# show object's variable and function
print(dir([1, 2, 3]))
print(dir({'1':'a'}))

# value and remain
print(divmod(7, 3))
print(divmod(1.3, 0.2))

# return index number of tuple, list and string
for i, name in enumerate(['body', 'foo', 'bar']):
    print (i, name)


# eval(expression): expression means executable string
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))


# positive function can be replaced with filter built-in functions
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))


def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# hex
print(hex(234))

# id : object reference memory address
a = 3
b = a
print(id(3))
print(id(a))
print(id(b))

# input
a = raw_input() #input()
print(a)

# int
print(int('3'))
print(int(3.4))

# isinstance
class Person: pass
a = Person()
b = 3

print(isinstance(a, Person))
print(isinstance(b, Person))

# lambda is same as "def" keyword. It is used to make simple function
sum = lambda a, b: a + b
print(sum(3, 4))

myList = [lambda a,b:a+b, lambda a,b:a*b] # in this case, even def cannot be used
print(myList)
print(myList[0](3,4))
print(myList[1](8,4))

# len
print(len("python"))
print(len([1,2,3]))

# list
print(list("python"))
print(list((1,2,3)))
a = [1, 2, 3]
b = list(a)
print(b)

# map
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

# -->> change using map
def two_times(x): return x*2
print(list(map(two_times, [1,2,3,4])))

# even simpler
print(list(map(lambda a: a*2, [1, 2, 3, 4])))

# max
print(max([1, 2, 3]))

# min
print(min("python"))

# oct
print(oct(12345))

#open : file open

#pow
print(pow(2, 4))

#range
print(list(range(5)))
print(list(range(4,7)))
print(list(range(1, 10, 2)))

# sorted
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))

a = [3, 1, 2]
result = a.sort() # NOTe: it does not return anything
print(result)

#str
print(str(3))
print(str('hi'.upper()))

#tuple
print(tuple("abc"))
print(tuple([1, 2, 3]))

#type
print(type("abc"))
print(type([ ]))
print(type(open("test", 'w')))

#zip
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))