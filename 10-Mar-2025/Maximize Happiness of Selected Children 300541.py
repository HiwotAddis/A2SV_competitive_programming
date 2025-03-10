# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res=0
        diff=0
        for i in range(len(happiness)):
            if k>0:
                if happiness[i]>0 :
                    x=happiness[i]-diff
                    if x>0:
                        res+= x
                        diff+=1
                        k-=1
                else:
                    break
            else:
                break
    
        return res


