ctype=int(input("select cloth type 1)silk 2)linen 3)cotton: "))
rate=int(input('enter purchase rate: '))
if(ctype==1):
    if(rate>=5000):
        offrate=rate-(rate*(20/100))
        print('amount to be paid -',offrate)
    elif(rate>=4000)&(rate<5000):
        offrate=rate-(rate*(10/100))
        print('amount to be paid -', offrate)
    elif(rate>=3000)&(rate<4000):
        offrate=rate-(rate*(8/ 100))
        print('amount to be paid -', offrate)
    elif(rate>=2000)&(rate<3000):
        offrate=rate-(rate*(7/100))
        print('amount to be paid -', offrate)
    else:
        offrate = rate - (rate * (0/ 100))
        print('amount to be paid -', offrate)




if(ctype==2):
    if(rate>=5000):
        offrate=rate-(rate*(20/100))
        print('amount to be paid -',offrate)
    elif(rate>=4000)&(rate<5000):
        offrate=rate-(rate*(10/100))
        print('amount to be paid -', offrate)
    elif(rate>=3000)&(rate<4000):
        offrate=rate-(rate*(9/ 100))
        print('amount to be paid -', offrate)
    elif(rate>=2000)&(rate<3000):
        offrate=rate-(rate*(7/100))
        print('amount to be paid -', offrate)
    else:
        offrate = rate - (rate * (5 / 100))
        print('amount to be paid -', offrate)

if(ctype==3):
    if(rate>=5000):
        offrate=rate-(rate*(20/100))
        print('amount to be paid -',offrate)
    elif(rate>=4000)&(rate<5000):
        offrate=rate-(rate*(10/100))
        print('amount to be paid -', offrate)
    elif(rate>=3000)&(rate<4000):
        offrate=rate-(rate*(8/ 100))
        print('amount to be paid -', offrate)
    elif(rate>=2000)&(rate<3000):
        offrate=rate-(rate*(7/100))
        print('amount to be paid -', offrate)
    else:
        offrate = rate - (rate * (5/ 100))
        print('amount to be paid -', offrate)

