def prime(num):
    i=2
    flag=0
    while(i<num):
        if(num%i==0):
            flag=flag+1
            break
        else:
            flag=0
        i+=1

    if(flag==0):
        print(num,'is a prime number')
    else:
        print(num,'is not a prime number')

prime(19)