# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
t=int(input())

for _ in range(t):
    n=int(input())
    s=input()
    right=Counter(s)
    left=Counter()
    max_=0
    for i in s:
        left[i]+=1
        right[i]-=1
        if right[i]==0:
            del right[i]
        max_=max(max_,len(right)+len(left))
    print(max_)