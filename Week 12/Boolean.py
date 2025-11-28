# cualquier boolean solo puede ser true o false. 

class Boolean:
   
    def __init__(self):
        self.__value__ = None

    @property
    def is_true(self):
        return self.__value__ 

    @is_true.setter
    def is_true(self, new_value):
        self.__value__ = new_value