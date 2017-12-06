class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self): # __str__ method: showing error message        
        return self.msg
