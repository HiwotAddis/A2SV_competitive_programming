# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
a = list(map(int, input().split()))

diffs=[a[i]-a[i-1] for i in range(1,n)]
diffs.sort(reverse=True)
max_cost=a[-1]-a[0]
for i in range(k-1):
    max_cost-=diffs[i]
print(max_cost)

