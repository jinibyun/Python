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