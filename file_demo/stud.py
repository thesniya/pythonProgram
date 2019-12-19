f1=open('/home/luminar/PycharmProjects/luminar/file_demo/stud_all')
f2=open('/home/luminar/PycharmProjects/luminar/file_demo/stud_fail')
f3=open('/home/luminar/PycharmProjects/luminar/file_demo/stud_pass','w')
set_all=set()
for item in f1:
    set_all.add(item.rstrip('\n'))
set_fail=set()
for item in f2:
    set_fail.add(item.rstrip('\n'))
set_pass=set_all-set_fail
for item in set_pass:
    f3.write(item+'\n')



