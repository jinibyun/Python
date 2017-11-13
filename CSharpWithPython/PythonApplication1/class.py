
class Service:
    secret = "This is screet"    
    def sum(self, a, b):      # "self" is cannot be skip in class method          
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


# class inheritance
# class className(base className)

class MoreFourCal(fourCal):
    def pow(self):
        result = self.first ** self.second
        return result

print("------object c -------")
c = MoreFourCal()
c.setData(2, 4)
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