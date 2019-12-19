#val = 20
# def demo():
#     val=10
#     print(val*20)
# demo()
# print(val)


val = 20
def demo():
    global val   #if declared as global variable, the value will effect outside the functn too
    val=10
    print(val*20)
demo()
print(val)

print('--------------------------')

def arg(*data):
    print(data)
arg(10)



