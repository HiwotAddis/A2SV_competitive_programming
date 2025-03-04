# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n=int(input())
costs=list(map(int,input().split()))
original =costs[:]
costs.sort()
prefix_sorted=[0]*n
prefix=[0]*n
curr=0
current=0
for i in range(n):
    curr+=costs[i]
    prefix[i]=curr
for i in range(n):
    current+=original[i]
    prefix_sorted[i]=current
m=int(input())
for _ in range(m):
    t,l,r=map(int,input().split())
    if t==2:
        if l-1==0:
            print(prefix[r-1])
        else:
            print(prefix[r-1]-prefix[l-2])
    else:
        if l-1==0:
            print(prefix_sorted[r-1])
        else:
            print(prefix_sorted[r-1]-prefix_sorted[l-2])