lines='hello hai how are you hello hai'

words=lines.split(' ')     #split using the space in between and a list is formed
#print(words)
dict={}

for item in words:
    if(item not in dict):
        dict[item]=1
    else:
        dict[item]+=1

print(dict)


