import System
from System.Collections.Generic import *
from System.Collections import *

import datetime

class Convert(object):
    dict = { }
    list = [ ]
    @staticmethod
    def toDict(netDictionary):        
        for item in netDictionary:     
            key = item.Key
            value = item.Value
            Convert.dict[key] = value

        return Convert.dict

    @staticmethod
    def toList(netList):        
        for item in netList:                 
            Convert.list.append(item)

        return Convert.list

class TryParse(object):
    
    @staticmethod
    def toInt(value):
        try:
            return int(value), True
        except ValueError:
            return value, False

    @staticmethod
    def toFloat(value):
        try:
            return float(value), True
        except ValueError:
            return value, False

    @staticmethod
    def toBool(value):
        try:
            return True if value.lower() == "true" else False
        except ValueError:
            return False

    @staticmethod
    def toDateTime(value, format):
        try:
            date = datetime.datetime.strptime(value, format)
            return True
        except ValueError:
            return False
#result = TryParse.toInt(3)
#print(result[0])
#print(result[1])

#print(TryParse.toBool("ddd"))
#print(TryParse.toDateTime("qwyhgre", "df"))