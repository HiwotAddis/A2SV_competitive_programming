# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
ans=0
p1=p2=0
suma=sumb=0
if sum(a)!=sum(b):
    print(-1)
    exit()
while p1<n and p2<m :
    suma+=a[p1]
    sumb+=b[p2]
    p1+=1
    p2+=1
    while suma != sumb:
        if suma<sumb:
            suma+=a[p1]
            p1+=1
        else:
            sumb+=b[p2]
            p2+=1
    ans+=1
print( ans)
