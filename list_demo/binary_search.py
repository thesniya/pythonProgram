#list should be sorted

list=[4,3,6,1,2,8]
list=sorted(list) #sort the list and store it into the same list
flag=0
low=0
upp=len(list)-1
mid=(upp+low)//2
elem=int(input('enter the element to be searched'))
while(low<=upp):
    if(elem>list[mid]):
        low=mid+1
    elif(elem<list[mid]):
        upp=mid-1
    elif(elem==list[mid]):
        flag+=1
        break
    mid=(upp+low)//2
if(flag>0):
    print('element found')
else:
    print('not found')


