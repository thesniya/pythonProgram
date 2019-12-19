class Base:
    def m(self):
        print('inside base class')

class Derived(Base):  #single inheritance
    def m2(self):
        print('inside is derived')

ob=Derived()
ob.m2()
ob.m()   #supports..bcz 'Base' id inherited by 'Derived'
        