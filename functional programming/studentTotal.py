class student:
    def __init__(self,id,name,total):
        self.id=id
        self.name=name
        self.total=total
    def __str__(self):
        return self.name

f1=open("student",'r')
lst=[]
studentlist=[]
for data in f1:
    lst=(data.rstrip("\n").split(','))
    print(lst)
    id=lst[0]
    name=lst[1]
    total=lst[2]
    studentlist.append(student(id,name,total))

mlist=list(filter(lambda o:int(o.total)>150,studentlist))
for ob in mlist:
    print(ob)