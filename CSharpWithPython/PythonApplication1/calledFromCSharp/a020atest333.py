# .NET DLL
import System

import clr
clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)

from System.Collections.Generic import *
from System.Linq import *

# Python
import CustomError

class receiptParser:
    def preParse(self, parseDefinitionData, receiptString):    
        try:
            # filtering
            if parseDefinitionData.ExclusiveReceiptPhrases and parseDefinitionData.ExclusiveReceiptPhrases.Count > 0:
                for member in parseDefinitionData.ExclusiveReceiptPhrases:
                    if member:
                        if receiptString.Contains(member):
                            receiptString = receiptString.Replace(member.Trim(), "")

            # remove
            if parseDefinitionData.RemovedList and parseDefinitionData.RemovedList.Count > 0:
                for member in parseDefinitionData.RemovedList:
                    if member:
                        receiptString = receiptString.Replace(member.Trim(), "")

            # replace
            if  parseDefinitionData.ReceiptReplaceList and parseDefinitionData.ReceiptReplaceList.Count > 0:
                for member in parseDefinitionData.ReceiptReplaceList:
                    if member:
                        receiptString.Replace(member.Key, member.Value)
                                    
            return receiptString;
        except CustomError as e:
            return e
    

