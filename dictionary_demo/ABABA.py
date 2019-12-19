#to find first recursive character in ABABA

words='ABABA'
dic={}
for item in words:
    if(item not in dic):
        dic[item]=1
    else:
        print('first recursive character is:',item)
        break

