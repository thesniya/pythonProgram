dic={'name':'abc',102:'mno',103:'xyz'}
#print(dic)
print(dic[102])    #accessing elements

print('--------------------------')

dic[103]='rst'     #updating values
print(dic)

print('--------------------------')

for item in dic.keys():    #iterating keys
    print(item,end='\t')   #to print keys
    print(dic[item])       #to print corresponding values

print('--------------------------')

for item in dic:
    #print(item)  #print keys
    print(dic[item])  #print values

print('--------------------------')


print('name' in dic)   #check whether a key is present or not

