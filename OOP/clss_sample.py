class person:
    def setVal(self,nam,ag):
        self.name=nam
        self.age=ag

    def display(self):
        print('name :',self.name)
        print('age :',self.age)

ob1=person()
ob2=person()

ob1.setVal('ajay',26)
ob1.display()
ob2.setVal('vijay',28)
ob2.display()

print(ob1.age)   #here we can understand the need of self
