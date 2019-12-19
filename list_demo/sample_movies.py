list=[['toy story',1991,4],['dracula',1997,4.8],['cocktail',1991,5],['conjuring',2006,4.9]]

#list of movies rating>4.5-----
# for item in list:
#     if(item[2]>4.5):
#         print(item[0])

#count of movies released in 1991-----
# count=0
# for item in list:
#     if(item[1]==1991):
#         count+=1
# print('count=',count)


#highest rating movie-----
rating=[]
for item in list:
    rating.append(item[2])
#rating=sorted(rating)
print(max(rating))


