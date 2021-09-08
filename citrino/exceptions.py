class InvalidNameException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class InheritanceException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class NotCallableException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class InvalidContractException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class NotCompatibleException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class NotCompatibleOperationException(NotCompatibleException):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class NotSettedAttributeException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class NoneException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class TypeNotValidException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class NotValidValueException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class InvalidOperationException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class NotConnectedException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)