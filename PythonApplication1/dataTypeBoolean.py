print("======== boolean type =======")

a = True
type(a) #python built-in function

a = [1, 2, 3, 4]
while a:
    print(a.pop())

if [ ]:
    print("True")  #note: case-sensitive. always T and F is upper case
else:
    print("False")


# value -->>	True of False
'''
"python"	True
""	        False
[1, 2, 3]	True
[]	        False
()	        False
{}	        False
1	        True
0	        False
None	    False
'''
bool('python')
bool('')
bool([1, 2, 3])
bool([])
bool(0)
bool(3)