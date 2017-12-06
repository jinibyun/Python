# .NET DLL
import System

import clr
clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)

from System.Collections.Generic import *
from System.Collections import *
from System.Linq import *

# Python
import re
import sys
sys.path.append("C:/Python27/Lib/site-packages")
from asq import *

from error import *
from modelData import *
from util import *

class Massage(object):

    def __init__(self, detailParameter, summaryParameter):
        self.__detailParameter = detailParameter
        self.__summaryParameter = summaryParameter

    @property
    def detailParameter(self):
        return self.__detailParameter

    @detailParameter.setter
    def detailParameter(self,clr):
        self.__detailParameter = clr

    @property
    def summaryParameter(self):
        return self.__summaryParameter

    @summaryParameter.setter
    def summaryParameter(self,clr):
        self.__summaryParameter = clr

    def MassageDetail(self, items):
        try:
            result = []
            previous = ""
            current = ""
            for sentence in items: # make one line            
                if (not sentence):
                    continue

                modifiedSentence = sentence
                # All dollar value such as $ should be replace with empty
                unnecessarySymbols = ["$"];
                for member in unnecessarySymbols:                
                    modifiedSentence = modifiedSentence.Replace(member, "")        

                lastDoubleString = ""
                if ( not self.detailParameter.isExistItemCode):
                    lastDoubleString = self.GetLastDoubleString(modifiedSentence)
                else:
                    if (self.detailParameter.itemCodepattern):
                        itemCode = self.GetItemCode(modifiedSentence, self.detailParameter.itemCodepattern)

                        # itemCode should be excluded from GetLastDoubleString(modifiedSentence)     
                        codeIndex = modifiedSentence.find(itemCode) 
                                                
                        lastDoubleString = modifiedSentence[0:codeIndex] + modifiedSentence[codeIndex + len(itemCode):]
                        lastDoubleString = self.GetLastDoubleString(lastDoubleString)

                if (lastDoubleString):
                    isSalePrice = self.IsSalePrice(modifiedSentence, lastDoubleString)
                    if (isSalePrice): # main item line
                        current = current + " " + modifiedSentence if current else current + modifiedSentence
                        result.append(current)
                        current = ""
                    else: # sub item line
                        current = current + " " + modifiedSentence
                else: # sub item line
                    current = current + " " + modifiedSentence

            # 1. exclude if sale price is 0 or 0.00 
            # 2. add @ sign if there is no such sign
            # 3. remove
            # 4. ignore start character
            # 5. Replace
            # 6. add customer delimeter
            # 7. pattern ??
            if (len(result) > 0):
                return self.AdjustLineItem(result);
            
            return result;
            
        except CustomError as e:
            return e
    
    def GetItemCode(self, line, pattern):
        try:
            regex = re.compile(pattern)
            match = regex.match(line)
            if (match):
                return match.group()
            return ""
        except CustomError as e:
            return e

    def IsSalePrice(self, lineString, doubleString):
        try:
            afterDoublstring = lineString[lineString.rfind(doubleString) + len(doubleString): ].strip()
            if (not afterDoublstring):
                return True

            return self.detailParameter.SalePriceSuffix.Where(lambda x : x == afterDoublstring).Any()
        except CustomError as e:
            return e

    def GetParseResultDetail(Itemlines, parseDefinitionData, customeDelimeter):
        try:
            detailLineParser = parseDefinitionData.DetailLines
            queue = Queue[ParserReturnQueue](maxsize=0)
            
            #parse ItemLines every n times
            parserLineCount = detailLineParser.Lines.Count

            # detail only
            for i in range(0,Itemlines.Count): 
                # currentLine = Itemlines[i].strip().Split([customeDelimeter], StringSplitOptions.RemoveEmptyEntries)
                currentLine = re.split(customeDelimeter,Itemlines[i]) 
                
                parserLine = detailLineParser.Lines[0]
                for member in parserLine.Items:                
                    attrOrder = int(member.Attribute.order)
                    currentLineItemValue = currentLine[attrOrder]
                    parserReturnQ = ParserReturnQueue()
                    parserReturnQ.Name = member.Value
                    parserReturnQ.Value = member.currentLineItemValue
                    parserReturnQ.Empty = member.Attribute.empty
                    parserReturnQ.Order = member.Attribute.order
                    parserReturnQ.Type = member.Attribute.type

                    queue.enqueue(parserReturnQ)                                    
            
            return queue
        except CustomError as e:
            return e

    def AdjustLineItem(self, items):
        try:
            newList = []
            for sentence in items:            
                lastDoubleString = self.GetLastDoubleString(sentence)
                lastDecimal = float(lastDoubleString)
                # 1. exclude if sale price is 0 or 0.00 
                if lastDecimal == 0 or lastDecimal == 0:
                    continue
                else:
                    # 2. add at sign if there is no sign
                    modifiedSentence = self.AddAtSign(sentence)

                    # 3. Remove 
                    if (self.detailParameter.RemovedList and self.detailParameter.RemovedList.Count > 0):
                        for member in self.detailParameter.RemovedList:
                            if (member):
                                modifiedSentence = modifiedSentence.Replace(member, "")

                    # 4. ignore start character
                    if (self.detailParameter.IgnoreStartPoistion and self.detailParameter.IgnoreStartPoistion > -1):
                        locationOfFirstSpace = modifiedSentence[self.detailParameter.IgnoreStartPoistion: ].find(' ')
                        length = locationOfFirstSpace - self.detailParameter.IgnoreStartPoistion
                        shouldBeIgnored = modifiedSentence[self.detailParameter.IgnoreStartPoistion: length + 1]
                        modifiedSentence = modifiedSentence.Replace(shouldBeIgnored, "")

                    # 6. Replace
                    if (self.detailParameter.ReplaceList and self.detailParameter.ReplaceList.Count > 0):
                        # tempList = modifiedSentence.Split(new char[] { ' ' }).ToList<string>();
                        tempList = re.split(' ',modifiedSentence) 
                       
                        #tempList = tempList.Select(lambda x :
                        #    for member in parameter.ReplaceList:                            
                        #        if (member.Key.Equals(x, StringComparison.InvariantCultureIgnoreCase)):
                        #            x = member.Value;
                        #    return x
                        #).ToList[System.String]();
                        tempList2 = []
                        for member in parameter.ReplaceList: 
                            for temp in tempList:
                                if(member.Key.lower() == temp.lower()):
                                    tempList2.append(member.Value)
                                else:
                                    tempList2.append(temp)
                        
                        # list to array
                        list_array = []
                        for item in tempList2:
                            list_array.append(item)
                        
                        modifiedSentence = string.Join(" ", list_array);

                    # 7. add custom delimeter
                    modifiedSentence = self.AddCustomDelimeter(modifiedSentence, lastDecimal)
                    newList.append(modifiedSentence)

            return newList;
        except CustomError as e:
            return e
    
    def AddAtSign(self, sentence):
        try:
            if (sentence.find("@") < 0):
                lastDoubleString = self.GetLastDoubleString(sentence);
                front = sentence[ :sentence.find(lastDoubleString) + 1];
                back = sentence[sentence.find(lastDoubleString): ];
                atSign = "1@{0} ".format(lastDoubleString);
                sentence = front + atSign + back;
            return sentence.strip();
        except CustomError as e:
            return e    

    def AddCustomDelimeter(self, sentence, lastDecimal):
        try:
            splitted = sentence.split('@')
            count = self.GetLastDoubleString(splitted[0]).strip() # count
            itemCode = self.GetItemCode(sentence, self.detailParameter.itemCodepattern)
            if (not itemCode): # no item code
                splitted[0] = splitted[0].strip()[0: splitted[0].strip().rfind(count) + 1] + self.detailParameter.customDelimeter + count;            
            else: # item code exist
                splitted[0] = splitted[0].strip()[splitted[0].strip().find(itemCode): itemCode.Length + 1] + \
                    self.detailParameter.customDelimeter + splitted[0].strip()[itemCode.Length: (splitted[0].strip().rfind(count) - itemCode.Length) + 1] + \
                    self.detailParameter.customDelimeter + count

            salePrice = ""
            suffixSaleFound = False
            if (self.detailParameter.SalePriceSuffix and self.detailParameter.SalePriceSuffix.Count > 0):
                for member in self.detailParameter.SalePriceSuffix:
                    if (member):
                        if (splitted[1].strip().lower().find(member.lower()) > -1): # sale price + salePriceSuffix
                            salePrice = self.GetLastDoubleString(splitted[1]).strip() # sale price
                            extra = splitted[1].strip()[splitted[1].strip().rfind(member): member.Length + 1].strip()
                            splitted[1] = splitted[1].strip()[0 : splitted[1].strip().rfind(salePrice) + 1] + self.detailParameter.customDelimeter + salePrice + self.detailParameter.customDelimeter + extra

                            suffixSaleFound = True
                            break;

                if (not suffixSaleFound): # just sale price
                    salePrice = self.GetLastDoubleString(splitted[1]).strip() # unit price                
                    splitted[1] = splitted[1].strip()[0 : splitted[1].strip().rfind(salePrice) + 1] + self.detailParameter.customDelimeter + salePrice + self.detailParameter.customDelimeter + "N/A"

            else: # just sale price
                salePrice = self.GetLastDoubleString(splitted[1]).strip() # unit price                
                splitted[1] = splitted[1].strip()[0 : splitted[1].strip().rfind(salePrice) + 1] + self.detailParameter.customDelimeter + salePrice;

            unitPrice = ""
            suffixFound = False
            if (self.detailParameter.UnitPriceSuffix and self.detailParameter.UnitPriceSuffix.Count > 0):
                for member in self.detailParameter.UnitPriceSuffix:
                    if (member):
                        if (splitted[1].strip().lower().find(member) > -1): # unit price + priceSuffix
                            unitPrice = self.GetFirstDoubleString(splitted[1]).strip(); # unit price
                            extra = splitted[1].strip()[splitted[1].strip().find(member) : member.Length + 1].strip()
                            splitted[1] = self.detailParameter.customDelimeter + unitPrice + self.detailParameter.customDelimeter + extra + \
                                          splitted[1].strip()[unitPrice.Length + extra.Length + 1].strip()
                            suffixFound = True;
                            break;

                if (not suffixFound): # just unit price
                    unitPrice = self.GetFirstDoubleString(splitted[1]).strip() # unit price                
                    splitted[1] = self.detailParameter.customDelimeter + unitPrice + self.detailParameter.customDelimeter + "N/A" + splitted[1].strip()[unitPrice.Length: ]
            else: # just unit price
                unitPrice = self.GetFirstDoubleString(splitted[1]).strip() # unit price                
                splitted[1] = self.detailParameter.customDelimeter + unitPrice + splitted[1].strip()[unitPrice.Length: ]

            sentence = "{0}{1}".format(splitted[0].strip(), splitted[1].strip())

            return sentence;
        except CustomError as e:
            return e

    def GetLastDoubleString(self, sentence):
        try:
            lines = re.split(r"[^0-9\.]+",sentence)
            doubleArray = lines.Where(lambda c : c != "." and c.strip())
            return doubleArray.LastOrDefault[System.String]()
        except CustomError as e:
            return e

    def GetFirstDoubleString(self, sentence):        
        try:
            lines = re.split(r"[^0-9\.]+",sentence)
            doubleArray = lines.Where(lambda c : c != "." and c.strip())
            return doubleArray.FirstOrDefault[System.String]()
        except CustomError as e:
            return e

    def MassageSummary(self, items):
        try:
            list = Convert.toList(items);
            newItems =[]
            tempList = []
            # replace
            if (self.summaryParameter.ReplaceList and len(self.summaryParameter.ReplaceList) > 0):      
                dict = Convert.toDict(self.summaryParameter.ReplaceList)
                for item in list:    
                    for key, value in dict.iteritems():             
                        if(item.lower().find(key.lower())):
                            newItems.append(item.replace(key, value))
                            break
                        #else:
                        #    newItems.append(x)          
            
            #summary last line: e.g. PAID CASH 4.48      
                  
            tempList = query(newItems).where(lambda x : x.strip().startswith("PAID")).to_list()
            list = query(newItems).where(lambda x : not x.strip().startswith("PAID")).to_list()

            if (tempList and len(tempList) == 1):
                newList = tempList[0].split(' ')
                index = 0;

                del tempList[:]

                for member in newList:                
                    if (member):                    
                        if (index == 0):
                            tempList.append("{0} {1}".format( "PAID", member))
                        elif (index == 1):
                            tempList.append("{0} {1}".format( "PayMethod", member))         
                        elif (index == 2):             
                            tempList.append("{0} {1}".format( "PayAmount", member))                
                        index = index + 1
                # merge
                if (len(list)> 0):
                    list.extend(tempList);

            return list;
        except CustomError as e:
            return e        