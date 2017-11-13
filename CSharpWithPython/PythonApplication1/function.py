# def functionName(parameter):
#     execution


def sum(a, b):
    result = a + b
    return result

a = sum (1,4)
print(a)


# dynamic parmeter's count 
def sum_many(*args): # args would be tuple type
    sum = 0
    for i in args:
        sum += i
    return sum

result = sum_many(1,2,3)
print(result)

result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3, 4)
print(result) # return tuple type. NOTE: function always return only 1 value


def say_myself(name, old, man=True): 
    print("My name is %s" % name) 
    print("I am %d years old." % old) 
    if man: 
        print("Male")
    else: 
        print("Female")

say_myself("Jini", 27, False)

# global : not recommended

a = 1
def vartest():
    global a
    a += 1

vartest()
print(a)