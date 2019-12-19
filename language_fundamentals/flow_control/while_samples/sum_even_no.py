'''r=int(input('enter the range'))
i=0
sum=0
while(i<=r):
    if(i%2==0):
        sum=sum+i

    i+=1
print(sum)'''

#sum of even numbers using upper and lower limit

m=int(input('enter lower limit'))
n=int(input('enter upper limit'))
i=m
sum=0
while(i<=n):
    if(i%2==0):
        sum=sum+i
    i+=1
print(sum)