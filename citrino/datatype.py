class TypeDef(object):
    
    def __init__(self, value: object):
        self.__value = value
        
    @property
    def value(self):
        return self.__value
    
    def is_type(self, value):
        if  value.__class__ is self:
           return True
        return False