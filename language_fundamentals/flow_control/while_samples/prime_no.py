num=int(input('enter the value'))
i=2
flag=0
while(i<num):
    if(num%i==0):
        flag=flag+1
        break
    else:
        flag=0
    i+=1
if(flag==0):
    print('a prime number')
else:
    print('not a prime number')
