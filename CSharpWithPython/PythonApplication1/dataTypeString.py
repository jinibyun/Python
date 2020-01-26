print("======  4 ways to make string =======")
print("Hello World")
print("""Hello World""")
print('Hello World')
print('''Hello World''')

print("======  Escape character or python's string manupulation (it is simpler) can be used ======")
multiline = "Life is too short\nYou need python"
print(multiline)

multiline = '''
Life is too short
You need python
'''
print (multiline)

print("======  string multiply =====")
a = "python"
print(a * 2)

print("*" * 50)
print("My Program")
print("*" * 50 )

print("======  length =======")
a = "Life is too short"
print(len(a))

print("======  indexing =======")
a = "Life is too short, You need Python"
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[0])

print("======  slicing =======")
a = "Life is too short, You need Python"
print(a[0:4]) # start and end  NOTE: 0 <= a < 4
print(a[:17])

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
dateWeather = a[:]

print(date)
print(weather)
print(dateWeather)

a = 'Life is too short, You need Python'
print(a[19:-7]) # note: 19 to a[-8]. a[-7] is excluded

print("======  formatting ======")
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")

number = 3
print("I eat %d apples." % number)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day)) # multiple

# format code
# %s	 (String)  -->> it automatically change any value to "string"
# %c	(character)
# %d	(Integer)
# %f	(floating-point)
# %o	Oct
# %x	Hex
# %%	Literal % (character #)
print("Error is %d%%." % 98)  #Note

# align with space
print("%10s" % "hi") # right align
print("%-10sjane." % 'hi') # left align

#float
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234) #right align, float and only show 4 decimal


# formatting using string function
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)) # by name

print("{0:<10}".format("hi")) # left align and no more than 10
print("{0:>10}".format("hi")) # right align and no more than 10
print("{0:^10}".format("hi")) # middle align and no more than 10

print("{0:!<10}".format("hi")) # left align and no more than 10 and space fillup
print("{0:=^10}".format("hi")) # middle align and no more than 10  and space fillup

y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{{ and }}".format())


print("======  string function  =====")
a = "hobby"
print(a.count('b'))

# compare
print("Python is best choice".find('b')) # first occurrence location. if not found, return -1
print("Life is too short".index('t')) # if not found, return expection

# join
a = ","
b = a.join('abcd')
print(b)

# case
print("hi".upper())
print("hi".lower())

# trim
a = "    hi   "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# replace
a = "Life is too short"
print(a.replace("Life", "Your leg"))


# split
print("Life is too short".split()) # empty means space



