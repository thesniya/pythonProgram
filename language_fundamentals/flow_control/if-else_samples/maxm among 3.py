num1=int(input('enter value 1'))
num2=int(input('enter value 2'))
num3=int(input('enter value 3'))
if(num1>num2):
    if(num1>num3):
        print(num1,' is greater')
    else:
        print(num3,' is greater')
elif(num2>num1):
    if(num2>num3):
        print(num2,' is greater')
    else:
        print(num3,' is greater')
elif(num3>num1):
    if(num3>num2):
        print(num3,' is greater')
    else:
        print(num2,' is greater')
else:
    print('all are same')


