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
# from Queue import *

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
                                    
            return receiptString
        except CustomError as e:
            return e
    
    def GetAllDetailSummary(self, parseDefinitionData, receiptString):
            lines = List[System.String]()
            startLineNo = 0
            try:
                if parseDefinitionData.ItemStartLineNo:
                    startLineNo = int(parseDefinitionData.ItemStartLineNo)

                if (startLineNo > 0):
                    # 1. using ItemStartLineNo & ItemEndLineText
                    skipCount = startLineNo

                    # ref: https://stackoverflow.com/questions/4998629/python-split-string-with-multiple-delimiters
                    lines = re.split('\n|\r\n|\r',receiptString).ToList[System.String]()                                        
                    itemEndLine = lines.FindIndex(lambda x: x.Contains(parseDefinitionData.ItemEndLineText))

                    if (itemEndLine == 0):
                        itemEndLine = lines.Count

                    itemEndLine = itemEndLine - skipCount
                    lines = lines.Skip(skipCount).Take(itemEndLine).ToList[System.String]()                

                if (lines and lines.Count > 0):
                    # 2. exclusive
                    if (parseDefinitionData.ExclusivePhrases and parseDefinitionData.ExclusivePhrases.Count > 0 and parseDefinitionData.ExclusivePhrases.Where(lambda x: x).Any()):
                        lines = lines.TakeWhile(lambda x: not parseDefinitionData.ExclusivePhrases.Where(lambda y: x.Contains(y)).Any()).ToList<string>()

                    # 3. inclusive
                    if (parseDefinitionData.InclusivePhrases and parseDefinitionData.InclusivePhrases.Count > 0 and parseDefinitionData.InclusivePhrases.Where(lambda x: x).Any()):
                        lines = lines.TakeWhile(lambda x: parseDefinitionData.InclusivePhrases.Where(lambda y : x.Contains(y)).Any()).ToList<string>()
                
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
                iSummaryDataStart = allDetailSummary.FindIndex(lambda x : parseDefinitionData.SummaryDataStart.Where(lambda y: x.ToLower().Trim().StartsWith(y.ToLower().Trim())).Any())

            if (parseDefinitionData.SummaryDataEnd and parseDefinitionData.SummaryDataEnd.Count > 0):
                iSummaryDataEnd = allDetailSummary.FindIndex(lambda x : parseDefinitionData.SummaryDataEnd.Where(lambda y : x.ToLower().Trim().StartsWith(y.ToLower().Trim())).Any()) + 1

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
    def MassageDetail(self, items,  parameter):
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
                    lastDoubleString = GetLastDoubleString(modifiedSentence)
                    if (parameter.itemCodepattern):
                        itemCode = GetItemCode(modifiedSentence, parameter.itemCodepattern)

                        # itemCode should be excluded from GetLastDoubleString(modifiedSentence)                        
                        lastDoubleString = GetLastDoubleString(modifiedSentence.Substring(0, modifiedSentence.IndexOf(itemCode)) + modifiedSentence.Substring(modifiedSentence.IndexOf(itemCode) + itemCode.Length))

                if (lastDoubleString):
                    isSalePrice = IsSalePrice(modifiedSentence, lastDoubleString)
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
                return AdjustLineItem(result);
            
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
            afterDoublstring = lineString.Substring(lineString.LastIndexOf(doubleString) + doubleString.Length).Trim()
            if (not afterDoublstring):
                return true

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
                # currentLine = Itemlines[i].Trim().Split([customeDelimeter], StringSplitOptions.RemoveEmptyEntries)
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
                lastDoubleString = GetLastDoubleString(sentence)
                lastDecimal = decimal.Parse(lastDoubleString)
                # 1. exclude if sale price is 0 or 0.00 
                if lastDecimal == 0 or lastDecimal == 0:
                    continue
                else:
                    # 2. add at sign if there is no sign
                    modifiedSentence = AddAtSign(sentence)

                    # 3. Remove 
                    if (parameter.RemovedList.Count > 0):
                        for member in parameter.RemovedList:
                            if (member):
                                modifiedSentence = modifiedSentence.Replace(member, "")

                    # 4. ignore start character
                    if (parameter.IgnoreStartPoistion > -1):
                        locationOfFirstSpace = modifiedSentence.Substring(parameter.IgnoreStartPoistion).IndexOf(' ')
                        length = locationOfFirstSpace - parameter.IgnoreStartPoistion
                        shouldBeIgnored = modifiedSentence.Substring(parameter.IgnoreStartPoistion, length)
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
            if (sentence.IndexOf("@") < 0):
                lastDoubleString = GetLastDoubleString(sentence);
                front = sentence.Substring(0, sentence.IndexOf(lastDoubleString));
                back = sentence.Substring(sentence.IndexOf(lastDoubleString));
                atSign = string.Format("1@{0} ", lastDoubleString);
                sentence = front + atSign + back;
            return sentence.Trim();
        except CustomError as e:
            return e
    def GetLastDoubleString(self, sentence):
        try:
            lines = re.split(r"[^0-9\.]+",sentence)
            doubleArray = lines.Where(lambda c : c != "." and c.Trim())
            return doubleArray.LastOrDefault[System.String]()
        except CustomError as e:
            return e
    def AddCustomDelimeter(sentence, lastDecimal):
        try:
            splitted = sentence.Split(['@'])
            count = GetLastDoubleString(splitted[0]).Trim() # count
            itemCode = GetItemCode(sentence, parameter.itemCodepattern)
            if (string.IsNullOrEmpty(itemCode)): # no item code
                splitted[0] = splitted[0].Trim().Substring(0, splitted[0].Trim().LastIndexOf(count)) + parameter.customDelimeter + count;            
            else: # item code exist
                splitted[0] = splitted[0].Trim().Substring(splitted[0].Trim().IndexOf(itemCode), itemCode.Length) + \
                    parameter.customDelimeter + splitted[0].Trim().Substring(itemCode.Length, splitted[0].Trim().LastIndexOf(count) - itemCode.Length) + \
                    parameter.customDelimeter + count

            salePrice = ""
            suffixSaleFound = False
            if (parameter.SalePriceSuffix and parameter.SalePriceSuffix.Count > 0):
                for member in parameter.SalePriceSuffix:
                    if (member):
                        if (splitted[1].Trim().IndexOf(member, StringComparison.InvariantCultureIgnoreCase) > -1): # sale price + salePriceSuffix
                            salePrice = GetLastDoubleString(splitted[1]).Trim() # sale price
                            extra = splitted[1].Trim().Substring(splitted[1].Trim().LastIndexOf(member), member.Length).Trim()
                            splitted[1] = splitted[1].Trim().Substring(0, splitted[1].Trim().LastIndexOf(salePrice)) + parameter.customDelimeter + salePrice + parameter.customDelimeter + extra

                            suffixSaleFound = True
                            break;

                if (not suffixSaleFound): # just sale price
                    salePrice = GetLastDoubleString(splitted[1]).Trim() # unit price                
                    splitted[1] = splitted[1].Trim().Substring(0, splitted[1].Trim().LastIndexOf(salePrice)) + parameter.customDelimeter + salePrice + parameter.customDelimeter + "N/A"

            else: # just sale price
                salePrice = GetLastDoubleString(splitted[1]).Trim() # unit price                
                splitted[1] = splitted[1].Trim().Substring(0, splitted[1].Trim().LastIndexOf(salePrice)) + parameter.customDelimeter + salePrice;

            unitPrice = ""
            suffixFound = False
            if (parameter.UnitPriceSuffix and parameter.UnitPriceSuffix.Count > 0):
                for member in parameter.UnitPriceSuffix:
                    if (member):
                        if (splitted[1].Trim().IndexOf(member, StringComparison.InvariantCultureIgnoreCase) > -1): # unit price + priceSuffix
                            unitPrice = GetFirstDoubleString(splitted[1]).Trim(); # unit price
                            extra = splitted[1].Trim().Substring(splitted[1].Trim().IndexOf(member), member.Length).Trim()
                            splitted[1] = parameter.customDelimeter + unitPrice + parameter.customDelimeter + extra + \
                                          splitted[1].Trim().Substring(unitPrice.Length + extra.Length + 1).Trim()
                            suffixFound = True;
                            break;

                if (not suffixFound): # just unit price
                    unitPrice = GetFirstDoubleString(splitted[1]).Trim() # unit price                
                    splitted[1] = parameter.customDelimeter + unitPrice + parameter.customDelimeter + "N/A" + splitted[1].Trim().Substring(unitPrice.Length)
            else: # just unit price
                unitPrice = GetFirstDoubleString(splitted[1]).Trim() # unit price                
                splitted[1] = parameter.customDelimeter + unitPrice + splitted[1].Trim().Substring(unitPrice.Length)

            sentence = string.Format("{0}{1}", splitted[0].Trim(), splitted[1].Trim())

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