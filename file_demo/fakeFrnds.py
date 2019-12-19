import operator
f=open('/home/luminar/Downloads/fakefriends.csv')
f2=open('fakeOut','w')
dic={}

for item in f:
    item=item.rstrip('\n')
    data=item.split(',')
    #print(data)
    #id=data[0]
    #print(id)
    age=data[2]
    #print(age)


    if(age not in dic):
        dic[age]=1
    else:
        dic[age]+=1
dic=sorted(dic.items(),key=operator.itemgetter(0))
print(dic)
print(dic[0])  #print(dic[-1])

for i in dic:
    i=str(i)
    f2.write(i+'\n')


