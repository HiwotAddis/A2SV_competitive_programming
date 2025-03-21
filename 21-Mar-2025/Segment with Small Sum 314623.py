# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,s=map(int,input().split())
a=list(map(int,input().split()))
sum_=0
i=j=0
l=float('-inf')
while j<len(a):
    sum_+=a[j]
    while sum_>s:
        sum_-=a[i]
        i+=1
    l=max(l,j-i+1)
    j+=1
    
print(l)