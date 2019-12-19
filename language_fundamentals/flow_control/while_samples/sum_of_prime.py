num=int(input('enter the range'))
j=1
i=1
sum=0
flag=0
while(i<=num):
    while(i<j):
        if(j%i==0):
           flag=flag+1
           break
        else:
           flag=0
        i+=1
    if(flag==0):
        sum=sum+j
    j+=1
print('sum of prime numbers =',sum)