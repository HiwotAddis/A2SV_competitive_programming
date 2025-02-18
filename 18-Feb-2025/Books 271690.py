# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t=map(int,input().split())
lst=list(map(int,input().split()))
max_=0
Sum=0
l=0
for i in range(n):
    Sum+=lst[i]
    while Sum>t:
        Sum-=lst[l]
        l+=1
    max_=max(max_,i-l+1)
print(max_)
    