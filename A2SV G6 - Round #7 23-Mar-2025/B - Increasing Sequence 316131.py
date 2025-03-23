# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    last=0
    for num in a:
        last+=1
        if last==num:
            last+=1
    print(last)