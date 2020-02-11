# tuple format
# similar to list

# diffrences: 
# 1. use ( ) instead of []
# 2. cannot be modified like list on runtime -->> biggest difference

# e.g
# t1 = ()
# t2 = (1,)   -->> , must be followed if there is only one
# t3 = (1, 2, 3)
# t4 = 1, 2, 3  -->> even can skip ( )
# t5 = ('a', 'b', ('ab', 'cd'))

print("===== when deleting or updating tuple index =======")
t1 = (1,2, 'a', 'b')
del t1[0] #error
t1[0] = 'c' #error


print("====== indexing =======")
t1 = (1, 2, 'a', 'b')
print(t1[0]) # for getting data, it is same as list

print("====== slicing =======")
print(t1[1:])

print("====== operation =======")
t2 = (3, 4)
print(t1 + t2)
print(t2 * 3)
print(len(t2))