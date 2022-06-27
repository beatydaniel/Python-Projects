from abc import ABC, abstractmethod
class house(ABC):
    def paySlip(self,amount):
        print("Your total amount: ",amount)
        @abstractmethod
        def payment(self,amount):
            pass
        
class CreditCardPayment(house):
    def payment(self,amount):
        print('Your purchase amount of {} exceeded your credit limit '.format(amount))

obj = CreditCardPayment()
obj.paySlip("$10000")
obj.payment("$10000")
