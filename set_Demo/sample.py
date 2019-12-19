# set={}   #if creating set like this, by default it is considered as type dictionary
# print(type(set))

# set=set()
# print(type(set))

# set={10,20,"edc",50,44,"abc"}
# print(set)                   #thus insertion order is not preserved


# set={10,10,10,20,20,40,50}
# print(set)                 #remove duplicates

# set={20,30,40}
# set.add(60)       #to add an element to a set
# print(set)


# set={40,50,30,55,77,23}
# set.pop()      #to delete an element
# print(set)

#UNION
set1={20,'ju',98,9.9}
set2={34,'ty',77}
#set3=set1|set2
#OR
set3=set1.union(set2)
print(set3)

#INTERSECTION
set1={30,50,44,76,'ki','ju'}
set2={33,50,'ki',67,50}
#set3=set1&set2    #----can be chained in case of more than 2 sets
#OR
set3=set1.intersection(set2)
print(set3)


#DIFFERENCE
set1={45,76,90,'hi'}
set2={45,'hi',89}
#set3=set1-set2
#OR
set3=set1.difference(set2)
print(set3)