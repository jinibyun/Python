
# basic
money = 1
if money:
    print("Get Taxi")
else:
    print("Walk")

# && --->> and  || --->> or

# in
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("taxi")
else:
    print("walk")

# pass
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("xxx")

# one line
if 'money' in pocket: pass
else: print("show card")


# elif
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
     print("taxi with pocket")
elif card: 
     print("taxi with card")
else:
     print("walk")