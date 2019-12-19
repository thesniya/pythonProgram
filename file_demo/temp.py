f1=open('temp')
f2=open('temp_out','w')
dic={}
for item in f1:
    item=item.rstrip('\n')
   # print(item)
    data=item.split(' ')
   # print(data)
    district=data[0]
    temp=data[1]
    #print('temp',temp)
    #print('district',district)

    if(district not in dic):
        dic[district]=temp
    else:
        old=dic[district]
        #print(dic[district])
        if(old<temp):
            dic[district]=temp
        else:
            dic[district]=old
#print(dic)

for i,j in dic.items():
    i=str(i)
    j=str(j)
    f2.write('\n')
    f2.write(i)
    f2.write('\t')
    f2.write(j)


