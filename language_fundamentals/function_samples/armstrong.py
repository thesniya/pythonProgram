def armstrong(org_num):
    sum=0
    num=org_num

    while(num!=0):
        digit=num%10
        sum=sum+(digit**3)
        num=num//10

    if(org_num==sum):
        print('sum=',sum,', thus an armstrong number')
    else:
        print('sum=',sum,', thus not an armstrong number')

armstrong(153)
