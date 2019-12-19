f1=open('/home/luminar/PycharmProjects/luminar/file_demo/read_write','r')
f2=open('/home/luminar/PycharmProjects/luminar/file_demo/read_write_out','w')
for item in f1:
    f2.write(item)
