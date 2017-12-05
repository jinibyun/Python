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
sys.path.append("C:/users/jini byun/anaconda3/lib/site-packages")

from error import *
from receiptMassage import *
from modelData import *

class baseParser(object):    
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

    __receiptStrings = List[System.String]()

    def Parse(self):
        try:
            # 1. preParse
            self.__receiptString = self.preParse()
            
            # 2. Get all detail summary
            self.__receiptStrings = self.GetAllDetailSummary()
            
            #if self.__receiptStrings and self.__receiptStrings.Count > 0:
            #    for member in self.__receiptStrings:
            #        print(member)
            
            # 3. get only detail & summary
            splitdetailsummary = self.GetSplitDetailSumary(self.__receiptStrings)
            detailitem = splitdetailsummary[0];
            summaryitem = splitdetailsummary[1];
            
            #for member in detailitem:
            #    print(member)   
                     
            #4. clean detail item
            detailitem = self.CleanDetailItem(detailitem);
            #for member in detailitem:
            #    print(member)   
            
            #5. get receipt message
            massagedreceiptdetail = self.GetReceiptMassage(detailitem, "detail");


            ParseResultDetail = self.GetParseResultDetail(massagedreceiptdetail);
            
            # massage receipt summary & parse
            massagedReceiptSummary = self.GetReceiptMassage(summaryitem, "summary");
            '''
            // var summaryParseDefinitionData = GetDynamicParseDefinition(summaryItem, parseDefinitionData, parseXml);
            ParseResultSummary = GetParseResultSummary(massagedReceiptSummary, parseDefinitionData);

            // 3. evaluate
            EvaluateResult(ParseResultDetail, ParseResultSummary);
            '''


        except CustomError as e:
            return e

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
    
    def GetSplitDetailSumary(self, allDetailSummary):
        try:
            allDetailSummary = allDetailSummary.Where(lambda x: x).ToList[System.String]()    
            # 1. using ItemStartLineNo & ItemEndLineText
            skipCount = 0
            iSummaryDataStart = 0
            iSummaryDataEnd = 0
            if (self.parseDefinitionData.SummaryDataStart and self.parseDefinitionData.SummaryDataStart.Count > 0):
                iSummaryDataStart = allDetailSummary.FindIndex(lambda x : self.parseDefinitionData.SummaryDataStart.Where(lambda y: x.ToLower().strip().StartsWith(y.ToLower().strip())).Any())

            if (self.parseDefinitionData.SummaryDataEnd and self.parseDefinitionData.SummaryDataEnd.Count > 0):
                iSummaryDataEnd = allDetailSummary.FindIndex(lambda x : self.parseDefinitionData.SummaryDataEnd.Where(lambda y : x.ToLower().strip().StartsWith(y.ToLower().strip())).Any()) + 1

            itemEndLine = iSummaryDataStart
            itemEndLine = itemEndLine - skipCount
            detail = allDetailSummary.Skip(skipCount).Take(itemEndLine).ToList[System.String]()

            skipCount = itemEndLine
            itemEndLine = iSummaryDataEnd - iSummaryDataStart
            summary = allDetailSummary.Skip(skipCount).Take(itemEndLine).ToList[System.String]()

            SplitDetailSummary = List[List[System.String]]() #[]



            SplitDetailSummary.Add(detail)
            SplitDetailSummary.Add(summary)

            return SplitDetailSummary
        except CustomError as e:
                return e

    def CleanDetailItem(self, Itemlines):
        try:
            # remove empty line
            Itemlines = Itemlines.Where(lambda x : x).ToList[System.String]()

            # remove DetailDataExclusivePhrases
            if (self.parseDefinitionData.DetailDataExclusivePhrases and self.parseDefinitionData.DetailDataExclusivePhrases.Count > 0 and self.parseDefinitionData.DetailDataExclusivePhrases.Where(lambda x : x).Any()):
                Itemlines = Itemlines.TakeWhile(lambda x : not self.parseDefinitionData.DetailDataExclusivePhrases.Where(lambda y : x.Contains(y)).Any()).ToList[System.String]>()
            
            return Itemlines
        except CustomError as e:
            return e

    def GetReceiptMassage(self, items, parseType):
        try:           
            if parseType == "detail":
                parameter = self.parseDefinitionData.DetailParameter
                # Validation
                if (not parameter.customDelimeter):
                    return None
                if (parameter.isExistItemCode):
                    if (not parameter.itemCodepattern):
                        return None

                if (parameter.IgnoreStartPoistion == 0):
                    parameter.IgnoreStartPoistion = -1
                
                md = Massage(parameter, None)
                massagedDetailItems = md.MassageDetail(items)
                return massagedDetailItems
                               
            elif parseType == "summary":
                parameter = self.parseDefinitionData.SummaryParameter
                md = Massage(None, parameter)
                massagedSummaryItems = md.MassageSummary(items)
                return massagedSummaryItems;
            
            return None
        except CustomError as e:
            return e

    def GetParseResultDetail(self, Itemlines):
        try:
            detailLineParser = self.parseDefinitionData.DetailLines
            lst = [] #System.Collections.Queue<ParserReturnQueue>()

            # parse ItemLines every n times
            parserLineCount = detailLineParser.Lines.Count;

            # detail only
            for i, item in enumerate(Itemlines):            
                currentLine = Itemlines[i].strip().split(self.parseDefinitionData.DetailParameter.customDelimeter)
                
                parserLine = detailLineParser.Lines[0];
                for member in parserLine.Items:
                    attrOrder = int(member.Attribute.order)
                    currentLineItemValue = currentLine[attrOrder]
                    
                    prq = ParserReturnQueue()
                    prq.Name = member.Value
                    prq.Value = currentLineItemValue
                    prq.Empty = member.Attribute.empty
                    prq.Order = member.Attribute.order
                    prq.Type = member.Attribute.type
                    
                    lst.append(prq)                    

            return lst;
        except CustomError as e:
            return e