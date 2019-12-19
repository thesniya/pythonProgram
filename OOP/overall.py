class student:
    schoolname='luminar technolab'   #static variable
    def setval(self,id,name):
        self.id=id   #instance variable
        self.name=name

    def printval(self):
        print(self.id,'==',self.name,'===',student.schoolname)

    @classmethod
    def setschool(cls,name):
            cls.schoolname=name

    @staticmethod
    def greetings():
        print('welcome')

s=student()
s.setval(100,'noname')
s.printval()
s.setschool('luminar technolab sol')
s.printval()
student.greetings()
