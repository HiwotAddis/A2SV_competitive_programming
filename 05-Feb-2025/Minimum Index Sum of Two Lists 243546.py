# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_idx=float(inf)
        res=[]
        for i,word in enumerate(list1):
            if word in list2:
                min_idx=min(min_idx,i+list2.index(word))
        for i,word in enumerate(list1):
            if word in list2 and i+list2.index(word)==min_idx :
                res.append(word)
        return res
            
        
        
            
                