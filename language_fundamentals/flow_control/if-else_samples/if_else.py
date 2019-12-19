'''num=int(input('enter value'))
if(num>0):
    print('num is positive')
elif(num<0):
    print('num is negative')
else:
    print('num is 0')'''

num1=int(input('enter 1st value'))
num2=int(input('enter 2nd value'))
if(num1>num2):
    print(num1,'is greater')
elif(num1<num2):
    print(num2,'is greater')
elif(num1==num2):
    print('both are equal')
else:
    print('invalid number')