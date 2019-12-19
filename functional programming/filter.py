#even no using filter
lst=[1,2,3,4,5,6,7,8]
# def check(no):
#     return no%2==0
# lst=list(filter(check,lst))  #instead of iteration
# print(lst)


#even no using filter and lambda
lst=list(filter(lambda no:no%2==0,lst))
print(lst)