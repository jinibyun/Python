# dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

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

# dictionary functions

# key list
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():
    print(k)
print(list(a.keys())) # a.keys() returns dict_keys object

# value list
print(a.values()) # a.values() returns dict_keys object

# get key, value pair
print(a.items())

a.clear()
print(a) # empty dictionary -->> { }

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('namew', 'xxx')) # second parameter is default value.

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a) # return true
print('email' in a) # return false

