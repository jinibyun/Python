print("===== function =======")
# def functionName(parameter):      # note: no parameter type in C# or Java
#     execution

def sum(a, b):
    result = a + b
    return result

a = sum (1,4)
print(a)

# dynamic parmeter's count
# 1.
def sum_many(*args): # args would be tuple type  #args is NOT keyword. It could be any.
    sum = 0
    for i in args:
        sum += i
    return sum

result = sum_many(1,2,3,5,7,9,11)
print(result)

result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)

# 2.
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul("mul", 3,4,5,6))

# ** parameter would return type of "dictionary"
def print_kwargs(**kwargs):  # note: ktargs is NOT keyword
    print(kwargs)

print(print_kwargs(a=1))
print(print_kwargs(a=1, name="Jason", balance=99.99))


# NOTE: function always return only 1 value
def sum_and_mul(a,b):
    return a+b, a*b  #note: this returns "ONE" tuple value

result = sum_and_mul(3, 4)
print(result) # return tuple type.

# if you want to get a result as if there are two.
result1, result2 = sum_and_mul(5,11)
print(result1)
print(result2)

# default value: It must be set very end of parameters
def say_myself(name, old, man=True):
    print("My name is %s" % name) 
    print("I am %d years old." % old) 
    if man: 
        print("Male")
    else: 
        print("Female")

say_myself("Jini", 27, False)
say_myself("James", 27)

# global : not recommended
a = 1
def vartest():
    global a
    a += 1

vartest()
print(a)

# lambda : It is likd function pointer
add = lambda a, b: a + b   #note: in lambda, it will automatically return result of expression
print(add(4,8))
