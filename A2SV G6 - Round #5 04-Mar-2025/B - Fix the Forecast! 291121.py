# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    b.sort()
    ans=[0]*n
    a=[(a[i],i) for i in range(n)]
    a.sort()
    for i in range(n):
        ans[a[i][1]]=b[i]
    print(*ans)

