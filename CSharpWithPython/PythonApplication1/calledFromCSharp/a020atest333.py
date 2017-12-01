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
from baseClass import *
# from Queue import *

class receiptParser(baseParser):

    def __init__(self):
        self.__parseDefinitionData = None
        self.__receiptString = ""
    
    @property
    def parseDefinitionData(self):
        return self.__parseDefinitionData

    @parseDefinitionData.setter
    def parseDefinitionData(self,clr):
        self.__parseDefinitionData = clr

    @property
    def receiptString(self):
        return self.__receiptString

    @receiptString.setter
    def receiptString(self,clr):
        self.__receiptString = clr

    

    def preParse(self):    
        try:
            # filtering
            if self.parseDefinitionData.ExclusiveReceiptPhrases and self.parseDefinitionData.ExclusiveReceiptPhrases.Count > 0:
                for member in self.parseDefinitionData.ExclusiveReceiptPhrases:
                    if member:
                        if self.receiptString.Contains(member) > -1:
                            self.receiptString = self.receiptString.Replace(member.strip(), "")

            # remove
            if self.parseDefinitionData.RemovedList and self.parseDefinitionData.RemovedList.Count > 0:
                for member in self.parseDefinitionData.RemovedList:
                    if member:
                        self.receiptString = self.receiptString.Replace(member.strip(), "")

            # replace
            if  self.parseDefinitionData.ReceiptReplaceList and self.parseDefinitionData.ReceiptReplaceList.Count > 0:
                for member in self.parseDefinitionData.ReceiptReplaceList:
                    if member:
                        self.receiptString.Replace(member.Key, member.Value)
                                    
            return self.receiptString
        except CustomError as e:
            return e
    
    def GetAllDetailSummary(self):
        lines = List[System.String]()
        startLineNo = 0
        try:
            if self.parseDefinitionData.ItemStartLineNo:
                startLineNo = int(self.parseDefinitionData.ItemStartLineNo)

            if (startLineNo > 0):
                # 1. using ItemStartLineNo & ItemEndLineText
                skipCount = startLineNo

                # ref: https://stackoverflow.com/questions/4998629/python-split-string-with-multiple-delimiters
                lines = re.split('\n|\r\n|\r',self.receiptString).ToList[System.String]()                                        
                itemEndLine = lines.FindIndex(lambda x: x.Contains(self.parseDefinitionData.ItemEndLineText))

                if (itemEndLine == 0):
                    itemEndLine = lines.Count

                itemEndLine = itemEndLine - skipCount
                lines = lines.Skip(skipCount).Take(itemEndLine).ToList[System.String]()                

            if (lines and lines.Count > 0):
                # 2. exclusive
                if (self.parseDefinitionData.ExclusivePhrases and self.parseDefinitionData.ExclusivePhrases.Count > 0 and self.parseDefinitionData.ExclusivePhrases.Where(lambda x: x).Any()):
                    lines = lines.TakeWhile(lambda x: not self.parseDefinitionData.ExclusivePhrases.Where(lambda y: x.Contains(y)).Any()).ToList<string>()

                # 3. inclusive
                if (self.parseDefinitionData.InclusivePhrases and self.parseDefinitionData.InclusivePhrases.Count > 0 and self.parseDefinitionData.InclusivePhrases.Where(lambda x: x).Any()):
                    lines = lines.TakeWhile(lambda x: self.parseDefinitionData.InclusivePhrases.Where(lambda y : x.Contains(y)).Any()).ToList<string>()
                
        except CustomError as e:
            return e
        return lines

    def GetSplitDetailSumary(self, allDetailSummary, parseDefinitionData):
        try:
            allDetailSummary = allDetailSummary.Where(lambda x: x).ToList[System.String]()    
            # 1. using ItemStartLineNo & ItemEndLineText
            skipCount = 0
            iSummaryDataStart = 0
            iSummaryDataEnd = 0
            if (parseDefinitionData.SummaryDataStart and parseDefinitionData.SummaryDataStart.Count > 0):
                iSummaryDataStart = allDetailSummary.FindIndex(lambda x : parseDefinitionData.SummaryDataStart.Where(lambda y: x.ToLower().strip().StartsWith(y.ToLower().strip())).Any())

            if (parseDefinitionData.SummaryDataEnd and parseDefinitionData.SummaryDataEnd.Count > 0):
                iSummaryDataEnd = allDetailSummary.FindIndex(lambda x : parseDefinitionData.SummaryDataEnd.Where(lambda y : x.ToLower().strip().StartsWith(y.ToLower().strip())).Any()) + 1

            itemEndLine = iSummaryDataStart
            itemEndLine = itemEndLine - skipCount
            detail = allDetailSummary.Skip(skipCount).Take(itemEndLine).ToList[System.String]()

            skipCount = itemEndLine
            itemEndLine = iSummaryDataEnd - iSummaryDataStart
            summary = allDetailSummary.Skip(skipCount).Take(itemEndLine).ToList[System.String]()

            SplitDetailSummary = List[List[System.String]]()

            SplitDetailSummary.Add(detail)
            SplitDetailSummary.Add(summary)

            return SplitDetailSummary
        except CustomError as e:
                return e

    def CleanDetailItem(self, Itemlines, parseDefinitionData):
        try:
            # remove empty line
            Itemlines = Itemlines.Where(lambda x : x).ToList[System.String]()

            # remove DetailDataExclusivePhrases
            if (parseDefinitionData.DetailDataExclusivePhrases and parseDefinitionData.DetailDataExclusivePhrases.Count > 0 and parseDefinitionData.DetailDataExclusivePhrases.Where(lambda x : x).Any()):
                Itemlines = Itemlines.TakeWhile(lambda x : not parseDefinitionData.DetailDataExclusivePhrases.Where(lambda y : x.Contains(y)).Any()).ToList[System.String]>()
            
            return Itemlines
        except CustomError as e:
            return e
            
    def GetReceiptMassage(self, parseDefinitionData, items, parseType):
        try:
            parameter = parseDefinitionData.DetailParameter
            # Validation
            if (not parameter.customDelimeter):
                return None
            if (parameter.isExistItemCode):
                if (not parameter.itemCodepattern):
                    return None

            if (parameter.IgnoreStartPoistion == 0):
                parameter.IgnoreStartPoistion = -1

            # MassageParameter param = new MassageParameter()
            if parseType == "detail":
                massagedDetailItems = self.MassageDetail(items, parameter)
                return massagedDetailItems
                               
            #elif parseType == parseType.Summary:
            #    param.SummaryReplaceList = parseDefinitionData.SummaryParameter.ReplaceList;
            #    parameter = param;
            #    var massagedSummaryItems = MassageSummary(items);
            #    return massagedSummaryItems;
            
            return None
        except CustomError as e:
            return e
    def MassageDetail(self, items, parameter):
        try:
            result = List[System.String]()
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
                if ( not parameter.isExistItemCode):
                    lastDoubleString = self.GetLastDoubleString(modifiedSentence)
                else:
                    if (parameter.itemCodepattern):
                        itemCode = self.GetItemCode(modifiedSentence, parameter.itemCodepattern)

                        # itemCode should be excluded from GetLastDoubleString(modifiedSentence)     
                        codeIndex = modifiedSentence.index(itemCode) 
                                                
                        lastDoubleString = modifiedSentence[0:codeIndex] + modifiedSentence[codeIndex + len(itemCode):]
                        lastDoubleString = self.GetLastDoubleString(lastDoubleString)

                if (lastDoubleString):
                    isSalePrice = self.IsSalePrice(modifiedSentence, lastDoubleString)
                    if (isSalePrice): # main item line
                        current = current + " " + modifiedSentence if current else current + modifiedSentence
                        result.Add(current)
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
            if (result.Count > 0):
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
            afterDoublstring = lineString[lineString.rindex(doubleString) + len(doubleString): ].strip()
            if (not afterDoublstring):
                return True

            return parameter.SalePriceSuffix.Where(lambda x : x == afterDoublstring).Any()
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
            newList = List[System.String]()
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
                    if (parameter.RemovedList.Count > 0):
                        for member in parameter.RemovedList:
                            if (member):
                                modifiedSentence = modifiedSentence.Replace(member, "")

                    # 4. ignore start character
                    if (parameter.IgnoreStartPoistion > -1):
                        locationOfFirstSpace = modifiedSentence[parameter.IgnoreStartPoistion: ].index(' ')
                        length = locationOfFirstSpace - parameter.IgnoreStartPoistion
                        shouldBeIgnored = modifiedSentence[parameter.IgnoreStartPoistion: length + 1]
                        modifiedSentence = modifiedSentence.Replace(shouldBeIgnored, "")

                    # 6. Replace
                    if (parameter.ReplaceList.Count > 0):
                        # tempList = modifiedSentence.Split(new char[] { ' ' }).ToList<string>();
                        tempList = re.split(' ',modifiedSentence).ToList[System.String]()  

                        # TODO
                        #tempList = tempList.Select(lambda x :
                        #    for member in parameter.ReplaceList:                            
                        #        if (member.Key.Equals(x, StringComparison.InvariantCultureIgnoreCase)):
                        #            x = member.Value;
                        #    return x
                        #).ToList[System.String]();
                        modifiedSentence = string.Join(" ", tempList.ToArray());

                    # 7. add custom delimeter
                    modifiedSentence = AddCustomDelimeter(modifiedSentence, lastDecimal)
                    newList.Add(modifiedSentence)

            return newList;
        except CustomError as e:
            return e
    
    def AddAtSign(self, sentence):
        try:
            if (sentence.index("@") < 0):
                lastDoubleString = self.GetLastDoubleString(sentence);
                front = sentence[ :sentence.index(lastDoubleString) + 1];
                back = sentence[sentence.index(lastDoubleString): ];
                atSign = string.Format("1@{0} ", lastDoubleString);
                sentence = front + atSign + back;
            return sentence.strip();
        except CustomError as e:
            return e
    def GetLastDoubleString(self, sentence):
        try:
            lines = re.split(r"[^0-9\.]+",sentence)
            doubleArray = lines.Where(lambda c : c != "." and c.strip())
            return doubleArray.LastOrDefault[System.String]()
        except CustomError as e:
            return e
    def AddCustomDelimeter(sentence, lastDecimal):
        try:
            splitted = sentence.Split(['@'])
            count = self.GetLastDoubleString(splitted[0]).strip() # count
            itemCode = self.GetItemCode(sentence, parameter.itemCodepattern)
            if (string.IsNullOrEmpty(itemCode)): # no item code
                splitted[0] = splitted[0].strip()[0: splitted[0].strip().rindex(count) + 1] + parameter.customDelimeter + count;            
            else: # item code exist
                splitted[0] = splitted[0].strip()[splitted[0].strip().index(itemCode): itemCode.Length + 1] + \
                    parameter.customDelimeter + splitted[0].strip()[itemCode.Length: (splitted[0].strip().rindex(count) - itemCode.Length) + 1] + \
                    parameter.customDelimeter + count

            salePrice = ""
            suffixSaleFound = False
            if (parameter.SalePriceSuffix and parameter.SalePriceSuffix.Count > 0):
                for member in parameter.SalePriceSuffix:
                    if (member):
                        if (splitted[1].strip().index(member, StringComparison.InvariantCultureIgnoreCase) > -1): # sale price + salePriceSuffix
                            salePrice = self.GetLastDoubleString(splitted[1]).strip() # sale price
                            extra = splitted[1].strip()[splitted[1].strip().rindex(member): member.Length + 1].strip()
                            splitted[1] = splitted[1].strip()[0 : splitted[1].strip().rindex(salePrice) + 1] + parameter.customDelimeter + salePrice + parameter.customDelimeter + extra

                            suffixSaleFound = True
                            break;

                if (not suffixSaleFound): # just sale price
                    salePrice = self.GetLastDoubleString(splitted[1]).strip() # unit price                
                    splitted[1] = splitted[1].strip()[0 : splitted[1].strip().rindex(salePrice) + 1] + parameter.customDelimeter + salePrice + parameter.customDelimeter + "N/A"

            else: # just sale price
                salePrice = self.GetLastDoubleString(splitted[1]).strip() # unit price                
                splitted[1] = splitted[1].strip()[0 : splitted[1].strip().rindex(salePrice) + 1] + parameter.customDelimeter + salePrice;

            unitPrice = ""
            suffixFound = False
            if (parameter.UnitPriceSuffix and parameter.UnitPriceSuffix.Count > 0):
                for member in parameter.UnitPriceSuffix:
                    if (member):
                        if (splitted[1].strip().index(member, StringComparison.InvariantCultureIgnoreCase) > -1): # unit price + priceSuffix
                            unitPrice = self.GetFirstDoubleString(splitted[1]).strip(); # unit price
                            extra = splitted[1].strip()[splitted[1].strip().index(member) : member.Length + 1].strip()
                            splitted[1] = parameter.customDelimeter + unitPrice + parameter.customDelimeter + extra + \
                                          splitted[1].strip()[unitPrice.Length + extra.Length + 1].strip()
                            suffixFound = True;
                            break;

                if (not suffixFound): # just unit price
                    unitPrice = self.GetFirstDoubleString(splitted[1]).strip() # unit price                
                    splitted[1] = parameter.customDelimeter + unitPrice + parameter.customDelimeter + "N/A" + splitted[1].strip()[unitPrice.Length: ]
            else: # just unit price
                unitPrice = self.GetFirstDoubleString(splitted[1]).strip() # unit price                
                splitted[1] = parameter.customDelimeter + unitPrice + splitted[1].strip()[unitPrice.Length: ]

            sentence = string.Format("{0}{1}", splitted[0].strip(), splitted[1].strip())

            return sentence;
        except CustomError as e:
            return e
# custom error handling
class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self): # __str__ method: showing error message
        return self.msg

class ParserReturnQueue:
    def __init__(self):
        self.__Name = ""
        self.__Value = ""
        self.__Type = ""
        self.__Empty = ""
        self.__Order = ""
        self.__IsDelimeterValue = ""
    
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self,clr):
        self.__Name = clr

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self,clr):
        self.__Value = clr

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self,clr):
        self.__Type = clr

    @property
    def Empty(self):
        return self.__Empty

    @Empty.setter
    def Empty(self,clr):
        self.__Empty = clr

    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self,clr):
        self.__Order = clr
    
    @property
    def IsDelimeterValue(self):
        return self.__IsDelimeterValue

    @IsDelimeterValue.setter
    def IsDelimeterValue(self,clr):
        self.__IsDelimeterValue = clr