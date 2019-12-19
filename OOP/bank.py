#here minimum balance shoud be 3000
import datetime
class bank:
    bname='sbi' #static variable; utilise as memory efficient method; common as a global variable
    def createAccount(self,acno):
        self.acno=acno
        self.balance=3000

    def deposit(self,amnt):
        self.balance+=amnt
        print('your',bank.bname,'account has been credited with amount',amnt,'on',datetime.datetime.now())
        print('your current balance is:',self.balance)

    def withdraw(self,amnt):
        if(amnt>self.balance):
            print('insufficient fund')
        else:
            self.balance-=amnt
            print('your', bank.bname, 'account has been debited with amount', amnt, 'on', datetime.datetime.now())
            print('your current balance is:', self.balance)

    def balanceEnq(self):
        print('your current balance is',self.balance)


obj=bank()
obj.createAccount(1234)
obj.deposit(1000)
obj.withdraw(200)
obj.balanceEnq()


