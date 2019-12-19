def SumOfEven(range):
    i=0
    sum=0
    while(i<=range):
        if(i%2==0):
            sum=sum+i
        i+=1
    print('sum of even numbers upto',range,'=',sum)

SumOfEven(10)