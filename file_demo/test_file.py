#to print names with length>5
f=open('/home/luminar/PycharmProjects/luminar/file_demo/test_file','r')
list=[]
for item in f:
    list.append(item.rstrip('\n'))

for i in list:
    val=len(i)
    if(val>5):
        print(i)