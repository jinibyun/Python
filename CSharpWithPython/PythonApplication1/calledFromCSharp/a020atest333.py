# .NET DLL
import System

import clr
clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)

from System.Collections.Generic import *
from System.Collections import *
from System.Linq import *

# Python

class receiptParser:
    def preParse(self, parseDefinitionData, receiptString):    
        try:
            # filtering
            if parseDefinitionData.ExclusiveReceiptPhrases and parseDefinitionData.ExclusiveReceiptPhrases.Count > 0:
                for member in parseDefinitionData.ExclusiveReceiptPhrases:
                    if member:
                        if receiptString.Contains(member) > -1:
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
    
    def GetAllDetailSummary(self, parseDefinitionData, receiptString):
            lines = List[System.String]()
            startLineNo = 0
            try:
                if parseDefinitionData.ItemStartLineNo:
                    startLineNo = int.Parse(parseDefinitionData.ItemStartLineNo)

                if (startLineNo > 0):
                    # 1. using ItemStartLineNo & ItemEndLineText
                    skipCount = startLineNo
                    words=[]
                    words.append(r"\r\n")
                    words.append(r"\r")
                    words.append(r"\n")
                    lines = receiptString.Split(words, StringSplitOptions.None).ToList<System.String>()
                    
                    itemEndLine = lines.FindIndex(lambda x: x.Contains(parseDefinitionData.ItemEndLineText))

                    if (itemEndLine == 0):
                        itemEndLine = lines.Count;

                    itemEndLine = itemEndLine - skipCount
                    lines = lines.Skip(skipCount).Take(itemEndLine).ToList<System.String>()                

                if (lines and lines.Count > 0):
                    # 2. exclusive
                    if (parseDefinitionData.ExclusivePhrases and parseDefinitionData.ExclusivePhrases.Count() > 0 and parseDefinitionData.ExclusivePhrases.Where(lambda x: x).Any()):
                        lines = lines.TakeWhile(lambda x: not parseDefinitionData.ExclusivePhrases.Where(lambda y: x.Contains(y)).Any()).ToList<string>()

                    # 3. inclusive
                    if (parseDefinitionData.InclusivePhrases and parseDefinitionData.InclusivePhrases.Count() > 0 and parseDefinitionData.InclusivePhrases.Where(lambda x: x).Any()):
                        lines = lines.TakeWhile(lambda x: parseDefinitionData.InclusivePhrases.Where(lambda y : x.Contains(y)).Any()).ToList<string>()
                
            except CustomError as e:
                return e
            return lines;


# custom error handling
class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self): # __str__ method: showing error message
        return self.msg

