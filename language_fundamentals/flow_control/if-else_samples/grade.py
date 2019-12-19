m1=int(input('enter mark1'))
m2=int(input('enter mark2'))
m3=int(input('enter mark3'))
total=m1+m2+m3
if(total>=140):
    print('A+')
elif(total>=130)&(total<140):
    print('A')
elif(total>=120)&(total<130):
    print('B+')
elif(total>=110)&(total<120):
    print('B')
elif(total>=100)&(total<110):
    print('C+')
else:
    print('failed')
