class A:
    def m1(self):
        print('inside A')

class B(A):
    def m2(self):
        print('inside B')

class C(B):
    def m3(self):
        print('inside C')

c=C()
c.m1()
c.m2()
c.m3()
