# list format
# a = [ ]   same as a = list()
# b = [1, 2, 3]
# c = ['Life', 'is', 'too', 'short']
# d = [1, 2, 'Life', 'is']
# e = [1, 2, ['Life', 'is']]
print("====== list basic =======")
a = [1, 2, 3]
print(a)
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3])
print(a[-1][0])

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

print("====== list slicing =======")
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[:2])
print(a[2:])

print("====== list operation =======")
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(a * 3)

#NB
print(str(a[2]) + "hi")

print("====== list modification =======")
a= [1,2,3]
a[2] = 4
a[1:2] = ['a', 'b', 'c'] #NB: it is different from a[1] = ['a', 'b', 'c']
print(a)

a = [1, 'c', 4]
del a[1]
print(a)

print("====== list function =======")
a = [1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

a = [1,4,3,2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.reverse()
print(a)

a = [1,2,3]
print(a.index(3))

a = [1, 2, 3]
a.insert(0, 4)
print(a)

a = [1,2,3]
a.pop() # get last item out
print(a)

a = [1,2,3,1]
print(a.count(1))

a = [1,2,3]
a.extend([4,5,6]) # NB: not like append, it only allows list
print(a)

print("====== 3 ways to remove item =====")
a = [1, 2, 3, 'a', 'b', 'c']
a.remove('a') # only value
print(a)

a = [1, 2, 3, 'a', 'b', 'c']
a.pop(4) # only index
print(a)

a = [1, 2, 3, 'a', 'b', 'c']
del a[4]  # only index
print(a)