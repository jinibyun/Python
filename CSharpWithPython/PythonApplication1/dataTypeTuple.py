# tuple format
# similar to list

# diffrences: 
# 1. use ( ) instead of []
# 2. cannot be modified like list

# e.g
# t1 = ()
# t2 = (1,)   -->> , must be followed if there is only one
# t3 = (1, 2, 3)
# t4 = 1, 2, 3  -->> even can skip ( )
# t5 = ('a', 'b', ('ab', 'cd'))

print("====== indexing =======")
t1 = (1, 2, 'a', 'b')
print(t1[0])

print("====== slicing =======")
print(t1[1:])

print("====== operation =======")
t2 = (3, 4)
print(t1 + t2)
print(t2 * 3)
