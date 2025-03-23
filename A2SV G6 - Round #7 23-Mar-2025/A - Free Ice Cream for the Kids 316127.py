# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

n,x=map(int,input().split())
distressed=0
 
for _ in range(n):
    sign,d=input().split()
    if sign =='+':
        x+=int(d)
    else:
        if x>=int(d):
            x-=int(d)
        else:
            distressed+=1
print(x,distressed)