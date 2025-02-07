# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp=defaultdict(list)
        for s in strs:
            temp[str(sorted(s))].append(s)
        return list(temp.values())