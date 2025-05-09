# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap=[-pile for pile in piles]
        heapify(max_heap)
        for _ in range(k):
            largest=-heappop(max_heap)
            redused=ceil(largest/2)
            heappush(max_heap,-redused)
        return -sum(max_heap)