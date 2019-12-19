#to print even numbrs

f=open('/home/luminar/PycharmProjects/luminar/file_demo/even_no','r')
list=[]
for item in f:
    list.append(int(item.rstrip('\n')))
print(list)
even=[]
for i in list:
    if(i%2==0):
        even.append(i)
print(even)


