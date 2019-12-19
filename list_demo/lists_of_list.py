# list=[[10,20],[30,40],[50,30]]
# for item in list:
#      print(item[0])


#sample-salaries above 15000

# list=[[10,'ABC',15000],[11,'CDE',20000],[12,'ASD',25000],[13,'EFG',30000]]
# for item in list:
#     if(item[2]>15000):
#         print(item)


#count of employees with salary above 8000
# list=[[10,'ABC',8000],[11,'CDE',20000],[12,'ASD',25000],[13,'EFG',30000]]
# count=0
# for item in list:
#     if(item[2]>8000):
#         count+=1
# print('count=',count)


#sum of salaries above 15000
list=[[10,'ABC',8000],[11,'CDE',20000],[12,'ASD',25000],[13,'EFG',30000]]
sum=0
for item in list:
    if(item[2]>15000):
        sum=sum+item[2]
print(sum)