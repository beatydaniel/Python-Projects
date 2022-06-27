class Protected:
    #sets the private variable to 5 and creates a protected variable set to 0
    def __init__(self):
        self.__privateVar = 5
        self._protectedVar = 0
        
    def getPrivate(self):            #function that prints out the private variable
        print(self.__privateVar)
        
    def getProtected(self):         #function that prints out the protected variable
        print(self._protectedVar)

    def setProtected(self,protected): #sets the protected variable to be a new value
        self._protectedVar=protected
        
    def setPrivate(self, private): #sets the private variable to be a new value
        self.__privateVar= private

        
obj = Protected() #set obj to call the class Protected
obj.getPrivate() #gets the original private value
obj.getProtected() #gets the original protected value
obj.setProtected(3) #changes the protected value
obj.getProtected() #call to print the value of the changed protected variable
obj.setPrivate(3) #changes the private value
obj.getPrivate() #calls to print the value of the changed private variable
    
