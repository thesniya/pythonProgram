#[CLUB,MP,W,D,L,GF,GA,GD,Pts]

list=[['ATK',5,3,1,1,10,3,7,10],['BENGALURU_FC',5,2,3,0,5,1,4,9],['GOA',4,2,2,0,10,5,5,8],['NORTHEAST_UNITED',4,2,2,0,5,3,2,8],['JAMSHEDPUR',4,2,1,1,6,5,1,7],['ODISHA',5,1,2,2,6,6,0,5],['KERALA_BLASTERS',5,1,1,3,3,5,2,4],['MUMBAI_CITY',4,1,1,2,5,8,3,4],['HYDERABAD',5,1,1,3,3,10,7,4],['CHENNAIYIN_FC',5,0,2,3,0,7,7,2]]

#team with highest points
pts=[]
for item in list:
    pts.append(item[8])
print(max(pts))

print('--------------------')

#mathes played >4
for item in list:
    if(item[1]>4):
        print(item[0])

print('--------------------')

#count of teams with GF<4
count=0
for item in list:
    if(item[7]<4):
        count+=1
print(count)