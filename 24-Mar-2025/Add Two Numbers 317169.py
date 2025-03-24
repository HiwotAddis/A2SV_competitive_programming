# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=[]
        num2=[]
        curr1=l1
        while curr1:
            num1.append(str(curr1.val))
            curr1=curr1.next
        curr2=l2
        while curr2:
            num2.append(str(curr2.val))
            curr2=curr2.next
        num1=''.join(num1[::-1])
        num2=''.join(num2[::-1])
        s= str(int(num1) + int(num2))
        s=s[::-1]
        res=[]
        for i in s:
            res.append(int(i))
        print(res)
        dummy=ListNode()
        curr=dummy
        i=0
        while i<len(res) and curr:
            curr.next=ListNode(res[i])
            i+=1
            curr=curr.next
        return dummy.next
        