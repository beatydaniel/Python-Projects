
#Parent Class
class User:
    name = ""
    email = ""
    password = ""
#Parent Class Method
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The password or email is incorrect.")
#Child Class
class Employee(User):
    base_pay = 11.00
    department = 'General'
    pin_number = ""
#Child Class method utilizing the parent class
    def getLoginInfo(self):
        entry_name = input("Enter your name:")
        entry_email = input ("Enter your email: ")
        entry_pin = input ("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The pin or email is incorrect.")
#Child Class
class Boss(User):
     management = ""
     account_number = ''
#Child Class method utilizing the parent class
     def getLoginInfo(self):
            entry_name = input("Enter your name:")
            entry_email = input ("Enter your email: ")
            entry_account = input("Enter your account number: ")
            if (entry_email ==self.email and entry_account == self.account_number):
                print("Welcome back, {}".format(entry_name))
            else:
                print("The account number is incorrect. ")
#Calling the functions to run the program
customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

owner = Boss()
owner.getLoginInfo()
