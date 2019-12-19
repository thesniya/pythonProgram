org_num=int(input('enter the number'))
sum=0
num=org_num

while(num!=0):
    digit=num%10
    sum = sum + (digit ** 3)
    num=num//10


if(sum==org_num):
    print('the number is armstrong')
else:
    print('the number is not armstrong')



