f=open('wordcount')
dict={}
list=[]

for word in f:
    list=(word.rstrip('\n').split(' '))
    for item in list:
          if(item not in dict):
            dict[item]=1
          else:
            dict[item]+=1
print(dict)
f2=open('wordcount_out','w')
for i,j in dict.items():  #default function
    i=str(i)
    j=str(j)
    f2.write('\n')
    f2.write(i)
    f2.write('\t')
    f2.write(j)





