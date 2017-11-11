# for variable in list(or Tuple, string):

test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a: # similar to (first, last) = (1, 2)
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d's student passed" % number)
    else: 
        print("%d's student failed" % number)

# range function with for
a = range(10)
print(a)

a = range(1,11)
print(a)

# sum of 1 to 10
sum = 0 
for i in range(1, 11): 
    sum = sum + i 

print(sum)

# len and range
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d's student passed" % (number+1))

# 2 * 

for i in range(2,10): 
    for j in range(1, 10): 
        print(i * j), # , means show result in same line
    print('')

# List comprehension 
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

# change above with list comprehension
result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)