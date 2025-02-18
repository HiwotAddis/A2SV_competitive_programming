# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n,k=map(int,input().split())
a=list(map(int,input().split()))
count=defaultdict(int)
l=0
unique=0
max_=0
L,R=0,0
for r in range(n):
    if count[a[r]]==0:
        unique+=1
    count[a[r]]+=1
    while unique>k:
        count[a[l]]-=1
        if count[a[l]]==0:
            unique-=1
        l+=1
    if r-l+1>max_:
        max_=r-l+1
        L=l
        R=r
print(L+1,R+1)