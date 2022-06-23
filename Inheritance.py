
#my parent class
class Vehicle:
    steering = "move left and right"
    acceleration = ""
    brakes = ""
    model = "" #both cars and bycicles share these attributes
                    
class Car(Vehicle): #creating a new class Car and calling the class Vehicle as a parent.
    engine = "" # cars have a engine
    mirrors = "" #cars have mirrors (bikes can but are optional)
    

class Bycycle(Vehicle): 
    handlebars = ""  #only a bike has handlebars
    chain = "function to make the pedals move" #bikes use chains to spin the pedals
    
    
    
    
    
