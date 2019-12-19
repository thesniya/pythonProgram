#to create empty list

# list=[]
# len=int(input('enter the length'))
# for i in range(0,len):
#     element=int(input('enter the element'))
#     list.append(element)   #store the element to the list
# print(list)


#to print even and odd separately

list=[]
even=[]
odd=[]
len=int(input('enter the length'))
for i in range(0,len):
    element=int(input('enter the element'))
    if(element%2==0):
        even.append(element)
    else:
        odd.append(element)
print('even=',even)
print('odd=',odd)



