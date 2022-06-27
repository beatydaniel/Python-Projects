from abc import ABC, abstractmethod #imports the abstractmethod from the ABC module
class house(ABC):
    def paySlip(self,amount):
        print("Your total amount: ",amount)
    #this function is telling us to pass in an argument,but won't tell you how or what
    #kind of data it will be.
        @abstractmethod
        def payment(self,amount):
            pass
        
class CreditCardPayment(house):
#defined how to implement the payment function from its parent paySlip class
    def payment(self,amount):
        print('Your purchase amount of {} exceeded your credit limit by 300$ '.format(amount))

obj = CreditCardPayment()
obj.paySlip("$10000")
obj.payment("$10000")
