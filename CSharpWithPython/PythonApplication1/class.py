print("=========== python class =========== ")

# basic structure
class FourCal:
    pass # it means it does not do anything

a = FourCal() # NOTE: when creating object instance and object we do not use "new" keyword as in C# or Java
print(type(a))


class Service:
    secret = "This is screet"    
    def sum(self, a, b):      # NOTE: "self" cannot be skip in class method
        result = a + b
        print("%s + %s = %s" % (a, b, result))


pey = Service()
pey.sum(2,3)

# self keyword: 
# first parameter incidate object itself when it is called via object. Keyword "self" is used

# below is not usual
pey = Service()
Service.sum(pey, 3, 4) # call from service requires explicit object

class Service2:
    secret = "This is a secree" # class variable will be shared
    def setname(self, name):
        self.name = name # member variable (instance variable) cannot be shared
    def sum(self, a, b):
        result = a + b
        print("%s %s + %s = %s" %(self.name, a, b, result ))

pey = Service2()
pey.setname("John")
pey.sum(1, 1)

# constructor
class Service3:
    secret = "This is a secreet"
    def __init__(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s  %s + %s = %s" % (self.name, a, b, result))

pey = Service3("Doe")
pey.sum(1, 1)


# fourCal() class
class fourCal():
    def setData(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

print("------object a -------")
a = fourCal()
print(type(a))

a.setData(4,2)
print(a.first)
print(a.second)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())

print("------object b -------")
b = fourCal()
b.setData(3,7)
print(b.first)
print(b.second)
print(b.sum())
print(b.mul())
print(b.sub())
print(b.div())

# memory address are different
print(id(a.first))
print(id(b.first))



# class inheritance
# class className(base className)  NOTE: use parenthesis  -->> ( )

class MoreFourCal(fourCal):
    def pow(self):
        result = self.first ** self.second
        return result

print("------object c -------")
c = MoreFourCal()
c.setData(2, 4)
print(c.sum())
print(c.mul())
print(c.sub())
print(c.div())
print(c.pow())

# overriding
class SafeFourCal(fourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

print("------object d -------")
d = SafeFourCal()
d.setData(4, 0)
print(d.div())

# object variable -->> It is like non-static variable (It has already been explained such as "first", "second" variable)
# class variable -->> It is like static variable in C#, Java
class Family:
    lastName = "Byun"

# How to use it
# 1.
print(Family.lastName)

# 2
f = Family()
f2 = Family()

print (f.lastName)
print (f2.lastName)

# check if lastName is shared
print(id(Family.lastName))
print(id(f.lastName))
print(id(f2.lastName))