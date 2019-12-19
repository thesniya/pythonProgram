class parent1:
    def m1(self):
        print('inside p1')

class parent2:
    def m1(self):
        print('inside p2')

class child(parent1,parent2):
    def m3(self):
        print('inside child')

c=child()
c.m3()
c.m1()   #here m1 of parent1 will get invoked, according to the priority; here parent1 is inherited first