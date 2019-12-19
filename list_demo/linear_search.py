list=[10,30,60,20]
item=int(input('enter the item to be searched'))
for i in list:
    if(i==item):
        flag=1
        break
    else:
        flag=0

if(flag==1):
    print('matching')
else:
    print('not matching')



