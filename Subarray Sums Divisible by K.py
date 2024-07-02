class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        hashmap = {0: 1} 
        cumulative_sum = 0
        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k
        
        
            if remainder in hashmap:
                count += hashmap[remainder]
        
        
            hashmap[remainder] = hashmap.get(remainder, 0) + 1
    
        return count
