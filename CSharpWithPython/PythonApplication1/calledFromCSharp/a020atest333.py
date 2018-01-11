## .NET DLL
#import System

#import clr
#clr.AddReference("System.Core")
#clr.ImportExtensions(System.Linq)

#from System.Collections.Generic import *
#from System.Collections import *
#from System.Linq import *

## Python
#import re
from baseClass import *
from error import *
# from Queue import *

class receiptParser(baseParser):
    def __init__(self):
        baseParser.__init__(self)    
    
    # override
    def Parse(self):
        try:
            baseParser.Parse(self)
            marks = [90, 25, 67, 45, 80]
            number = 0 
            
        except CustomError as e:
            return e   
    