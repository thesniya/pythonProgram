import itertools
#counter function
#counter=itertools.count(start=5,step=2)    #by default: start=0,step=1
# counter=itertools.count(start=5,step=-2.5)
# print(next(counter))
# print(next(counter))



#zip function
# lst=[100,200,300,400]
#
# daily_data=list(zip(itertools.count(start=1,step=1),lst))
# print(daily_data)


#repeat function
# counter=itertools.repeat(2,times=3)
# print(next(counter))
# print(next(counter))
# print(next(counter))



#star map
# sq=itertools.starmap(pow,[(0,2),(1,2),(2,2),(3,3)])  #here using starmap we can avoid normal iterations which lead to large code
# print(list(sq))


#combinations
# letters=['a','b','c','d']
# result=itertools.combinations(letters,2)
# for item in result:
#     print(item)



#permutation
# letters=['a','b','c','d']
# result=itertools.permutations(letters,2)
# for item in result:
#     print(item)

##### permutation n combination does not return same pair (a,a),(b,b)



#product that allows repeat
# numbers=[1,2,3,4]
# result=itertools.product(numbers,repeat=2)
# for item in result:
#     print(item)



#chain -> used to combine lists
# letters=['a','b','c','d']
# numbers=[1,2,3,4]
# combined=itertools.chain(letters,numbers)
# for item in combined:
#     print(item)




#slice
# result=itertools.islice(range(10),1,5)
# #result=itertools.islice(range(10),1,5,2) #step=2
# for item in result:
#     print(item)




compress
letters=['a','b','c','d']
selectors=[1,0,1,1]
#selectors=[True,True,False,True]
result=itertools.compress(letters,selectors)
for item in result:
    print(item)



