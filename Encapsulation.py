class Protected:
    #sets the private variable to 5
    def __init__(self):
        self.__privateVar = 5
        self._protectedVar = 0
        
    def getPrivate(self):
        print(self.__privateVar)
    def getProtected(self):
        print(self._protectedVar)
        
    def setPrivate(self, private):
        self.__privateVar= private

        
obj = Protected()
obj._protectedVar = 10
obj.getPrivate()
obj.getProtected()
obj.setPrivate(3)
obj.getPrivate()
    
