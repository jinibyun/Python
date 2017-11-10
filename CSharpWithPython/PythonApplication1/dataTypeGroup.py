# group datatype : set keyword
# 1. do not allow duplication
# 2. unordered

s1 = set([1,2,3,3,3])
print(s1)

s2 = set("Hello")
print(s2)

# convert to list. then it can be get using index
li = list(s1)
print(li) 
print(li[0])

# convert to list. then it can be get using index
t1 = tuple(s1)
print(t1)
print(t1[0])

# group datatype usage
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2) # same as s1.intersection(s2)
print(s1 | s2) # s2.union(s1)
print(s1- s2)
print(s2- s1)

# function

# add
s1 = set([1,2,3])
s1.add(4)
print(s1)

# update: multiple addition
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

# remove
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)