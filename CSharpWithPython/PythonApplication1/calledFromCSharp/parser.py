import clr
import System

clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)

from System.Collections.Generic import *
from System.Collections.Generic import List, Dictionary
from System.Linq import *

def preParse(parseDefinitionData, receiptString):    
    try:
        # filtering
        if parseDefinitionData.ExclusiveReceiptPhrases and parseDefinitionData.ExclusiveReceiptPhrases.Count > 0:
            isFound = parseDefinitionData.ExclusiveReceiptPhrases.Where(lambda x: x and receiptString.Contains(x.Trim())).Any();
            if isFound:
                return "";


        # remove
        if parseDefinitionData.RemovedList and parseDefinitionData.RemovedList.Count > 0:
            for member in parseDefinitionData.RemovedList:
                if member != "":
                    receiptString = receiptString.Replace(member.Trim(), "");

        # replace
        if  parseDefinitionData.ReceiptReplaceList and parseDefinitionData.ReceiptReplaceList.Count > 0:
            for member in parseDefinitionData.ReceiptReplaceList:
                receiptString.Replace(member.Key, member.Value);
                                    
        return receiptString;
    except CustomError as e:
        return e
    
# custom error handling
class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self): # __str__ method: showing error message
        return self.msg
    
