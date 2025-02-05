# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_idx=float(inf)
        res=[]
        dict_lst2={}
        for i,word in enumerate(list2):
            dict_lst2[word]=i
        for i,word in enumerate(list1):
            if word in dict_lst2:
                min_idx=min(min_idx,i+dict_lst2[word])
        for i,word in enumerate(list1):
            if word in dict_lst2 and i+dict_lst2[word]==min_idx :
                res.append(word)
        return res
                 