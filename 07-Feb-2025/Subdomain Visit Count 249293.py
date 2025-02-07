# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans=Counter()
        for cpdomain in cpdomains:
            count,domain=cpdomain.split(' ')
            d=domain.split('.')
            count=int(count)
            for i in range(len(d)):
                ans[".".join(d[i:])]+=count
        return ["{} {}".format(count,dmn) for dmn,count in ans.items()]