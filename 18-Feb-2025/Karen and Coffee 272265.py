# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q=map(int,input().split())
prefix=[0]*(200000+2)
for _ in range(n):
    l,r=map(int,input().split())
    prefix[l]+=1
    prefix[r+1]-=1
for i in range(1,len(prefix)):
    prefix[i]+=prefix[i-1]

for i in range(len(prefix)):
    if prefix[i]<k:
        prefix[i]=0
    else:
        prefix[i]=1
for i in range(1,len(prefix)):
    prefix[i]+=prefix[i-1]
for i in range(q):
    l,r=map(int,input().split())
    if l==0:
        print(prefix[r])
    else:
        print(prefix[r]-prefix[l-1])
