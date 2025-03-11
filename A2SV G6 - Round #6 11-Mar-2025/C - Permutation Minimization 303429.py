# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    q=deque()
    for i in a:
        if not q or i<q[0]:
            q.appendleft(i)
        else:
            q.append(i)
    print(*q)


    