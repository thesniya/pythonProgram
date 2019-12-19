class student:
    def setVal(self,name,roll,std):
        self.name=name
        self.roll=roll
        self.std=std

    def display(self):
        print('name:',self.name)
        print('rollno:',self.roll)
        print('std:',self.std)

    def __str__(self):
        return self.name     #two string method; works in base class

list=[]
stud1=student()
stud2=student()

stud1.setVal('manu',33,12)
stud1.display()
stud2.setVal('rahul',21,8)
stud2.display()

#print(stud1)

list.append(stud1)
list.append(stud2)

for i in list:
    if(i.roll>24):
        print(i)
