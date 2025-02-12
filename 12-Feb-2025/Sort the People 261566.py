# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

#insertion sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(1, n):
            h = heights[i]
            N = names[i]
            j = i - 1
            
            while j >= 0 and heights[j] < h:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            
            heights[j + 1] = h
            names[j + 1] = N
        
        return names
    
    

