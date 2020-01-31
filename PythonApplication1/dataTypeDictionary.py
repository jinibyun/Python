print("===== Data Type Dictionary =======")
# dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}  -->> format is same as JSON

a = {1: "hi"}
print(a)

a = {1: [1,2,3]}
print(a)


# dictionary add
a = {1 : 'a'}
a[2] = 'b' # key and value is added
a[3] = [4,5,6]
print(a)

# dictionary remove
del a[1]
print(a)

# get value
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic['name'])
# NOTE: key CANNOT be duplicated. If so, one of them would be ignored. DO NOT DUPLICATE KEY

# NOTE: tuple can be used as key, but not list because tuple is a kind of constant (not varied) but list can be varied
# Compare below two cases
a = {[1,2] : 'hi'} #error
print(a)

a = {(1,2) : 'hi'} # no error
print(a)

# dictionary functions
# key list
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():  # a.keys() returns dict_keys object
    print(k)

print(list(a.keys())) # list returns object as "list" format

# value list
print(a.values()) # a.values() returns dict_keys object

# get key, value pair
print(a.items())

a.clear()
print(a) # empty dictionary -->> { }

# NOTE
# Empty List : []
# Empty Tuple: ( )
# Empty Dicitonary: { }

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('namew', 'xxx')) # second parameter is default value.

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a) # return true
print('email' in a) # return false

