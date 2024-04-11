def count_elements_less_or_equal(nums, x):
    count = 0
    for num in nums:
        if num <= x:
            count += 1
    return count
 
def find_x(nums, k):
    left, right = 1, 10**9
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        count = count_elements_less_or_equal(nums, mid)
        if count == k:
            result = mid
            break
        elif count < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
 
# Input
n, k = map(int, input().split())
nums = list(map(int, input().split()))
 
# Output
result = find_x(nums, k)
print(result)
