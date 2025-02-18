# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    max_sum=0
    curr_max=a[0]
    for i in range(1,n):
        if (a[i] >0 and a[i-1]>0) or (a[i]<0 and a[i-1]<0):
            curr_max=max(curr_max,a[i])
        else:
            max_sum+=curr_max
            curr_max=a[i]
    max_sum+=curr_max
    print(max_sum)
