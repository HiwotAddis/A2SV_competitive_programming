# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n=int(input())
m=list(list(map(int,input().split())) for _ in range(n))
idx=[]
val=[]
good=set()
for i in range(n):
    good.add((i,i))
    good.add((i,n-i-1))
mid=n//2
for i in range(n):
    good.add((mid,i))
    good.add((i,mid))
res=sum(m[i][j] for i,j in good)

print(res)