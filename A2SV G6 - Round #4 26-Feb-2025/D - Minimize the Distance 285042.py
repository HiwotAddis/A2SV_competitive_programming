# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n=int(input())
lst=list(map(int,input().split()))
lst.sort()
if len(lst)%2==0:
    print( lst[(len(lst)//2)-1])
else:
    print(lst[len(lst)//2])