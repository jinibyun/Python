# -*- coding: utf-8 -*-

# built in variable: when running python one.py. It sets as below
#
#if __name__ == "__main__"


def func():
    print ("func() in one.py")
    
print("top level in one.py")

if __name__ == "__main__":
    print("One.py is being run directly!")
else:
    print("One.py has been imported")