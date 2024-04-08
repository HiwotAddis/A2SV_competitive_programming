def is_possible(n, arr):
    arr.sort()  
    for i in range(n - 1):
        if arr[i + 1] - arr[i] > 1:  
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(is_possible(n, arr))
