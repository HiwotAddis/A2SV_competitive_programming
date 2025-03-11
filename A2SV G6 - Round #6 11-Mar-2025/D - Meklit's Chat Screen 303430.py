# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
n,k=map(int,input().split())
id=list(map(int,input().split()))
q=deque()
d=set()
for i in range(n):
    if id[i] not in d:
        if len(q)==k:
            x=q.pop()
            d.remove(x)
        q.appendleft(id[i])
        d.add(id[i])
        
print(len(q))
print(*q)