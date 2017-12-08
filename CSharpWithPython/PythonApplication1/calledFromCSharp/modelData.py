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
    
    #@property
    #def IsDelimeterValue(self):
    #    return self.__IsDelimeterValue

    #@IsDelimeterValue.setter
    #def IsDelimeterValue(self,clr):
    #    self.__IsDelimeterValue = clr


class ParsingValidation:

    def __init__(self):
        self.__DetailMessage = [ ]
        self.__SummaryMessage = [ ]
        

    @property
    def DetailMessage(self):
        return self.__DetailMessage

    @DetailMessage.setter
    def DetailMessage(self,clr):
        self.__DetailMessage = clr

    @property
    def SummaryMessage(self):
        return self.__SummaryMessage

    @SummaryMessage.setter
    def SummaryMessage(self,clr):
        self.__SummaryMessage = clr
    