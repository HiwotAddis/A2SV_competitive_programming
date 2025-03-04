# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t=int(input())
for _ in range(t):
    n=int(input())
    r=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    prefix_r=[0]*n
    prefix_b=[0]*m
    curr=0
    current=0


    for i in range(n):
        curr+=r[i]
        prefix_r[i]=curr
    for i in range(m):
        current+=b[i]
        prefix_b[i]=current

    
    print(max(0,max(prefix_b))+max(0,max(prefix_r)))