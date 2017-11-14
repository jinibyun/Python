# 1
# try:
#     ...
# except:
#     ...
# 
# 
# 2
# try:
#     ...
# except possible error:
#     ...
# 
# 3
# try:
#     ...
# except possible error as variable:
#     ...

print("----------1------------")
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

print("----------2------------")
#f = open('foo.txt', 'r')
#try:
#    pass
#except FileNotFoundError as e:
#    print(str(e))
#else: # if try statment is successful, then else statement will be implemented
#    data = f.read()
#finally: # always
#    f.close()    


print("----------3------------")
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

# except (ZeroDivisionError, IndexError) as e: is also possible


# raise : raise error on purpose
class Bird:
    def fly(self):
        raise NotImplementedError # Force child class to implement

class Eagle(Bird):
    def fly(self):
        print("very fast") # method overriding

eagle = Eagle()
eagle.fly()


# create exception: inherit exception class
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self): # __str__ method: showing error message
        return self.msg

def say_nick(nick):
    if nick == "stupid":
        raise MyError("This is not allowed")
    print(nick)

try:
    say_nick("clever")
    say_nick("stupid")
except MyError as e:
    print(e)
