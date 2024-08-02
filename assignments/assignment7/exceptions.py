class InvalidMenuItemError(Exception):
    def __init__(self,err):
        self.err=err
    
    def __str__(self):
        return self.err
    
class InsufficientQuantityError(Exception):
    def __init__(self,err):
        self.err=err
    
    def __str__(self):
        return self.err

class DataCleaningError(Exception):
    def __init__(self,err):
        self.err=err
    
    def __str__(self):
        return self.err