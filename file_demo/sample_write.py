#in write mode the old file will be overwrited by new file
# list=['abc','cde','efg']
# f=open('/home/luminar/PycharmProjects/luminar/file_demo/even_no','w')
# for item in list:
#     f.write(item+'\n')



#in append mode we can preserve the old file along with new data
list=['abc','cde','efg']
f=open('/home/luminar/PycharmProjects/luminar/file_demo/even_no','a')
for item in list:
    f.write(item+'\n')