
#a network is sorting data packets based on their frequency of arrival.you are given an integers packets.write a program to sort the array in ascending Border
#1<=packets.length<=100
#-100<=packets[i<=100]
#[1,1,2,2,2,3]
#o/p[3,1,1,2,2,2]
#[2,3,1,3,2]
#o/p[1,3,3,2,2]
#packets=list(map(int,input().split()))
packets=[1,1,2,2,2,3]
d={}
freq=0
for i in range(len(packets)):
    for j in range(len(packets)):
        if packets[i]==packets[j]:
            freq+=1
    print(packets[i],freq)


