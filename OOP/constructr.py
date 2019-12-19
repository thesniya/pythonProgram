class student:
    clgname='luminar'

    def __init__(self,stname,id):
        self.stname=stname
        self.id=id

    def printVal(self):
        print('student name=',self.stname)
        print('student id is',self.id)

ob1=student('ajay',123)  #constructor is invoked automatically while object creation
ob2=student('vijay',456)
ob1.printVal()
ob2.printVal()