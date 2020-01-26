print("===== if statement =======")
# basic
money = 1
if money:
    print("Get Taxi")
else:
    print("Walk")

# && --->> and  || --->> or

# in
pocket = ['paper', 'cellphone', 'money'] #list
if 'money' in pocket:
    print("taxi")
else:
    print("walk")

# pass
pocket = ('paper', 'money', 'cellphone') #tuple
if 'money' in pocket:
    pass  # nothing will be done
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
elif card: # else if
     print("taxi with card")
else:
     print("walk")

# conditional expression
score = 61
message = "success" if score >= 60 else "failure"
print(message)