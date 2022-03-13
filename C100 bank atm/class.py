from cmath import pi


class Atm:

    def __init__(self, cardnumber, pinnumber):
        self.cardnumber = cardnumber 
        self.pinnumber = pinnumber 

    def check_Balance(self):
        print('Your current balance is 5000.')

    def debit_history(self, amount):
        new_amount = 5000-amount
        print('Your debit history is ' + str(amount) + '. Your remaining balance is ' + str(new_amount))

def main():
    credit = input("Enter card number: ")
    pin = input("Enter pin number: ")
    new_user = Atm(credit, pin)

    print("Choose debit/credit or balance.")
    print("1. Balance enquiry, 2. Debit history ")
    activity = int(input("Enter activity number: "))

    if(activity == 1): 
        new_user.check_Balance()

    elif(activity == 2):
        amount = int(input("Enter amount to be withdrawn: "))
        new_user.debit_history(amount)

    else:
        print("Enter a valid number.")

main()