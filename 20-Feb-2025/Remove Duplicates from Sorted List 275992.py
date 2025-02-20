# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count={}
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        curr=head
        while curr:
            if curr.val not in count:
                count[curr.val]=count.get(curr.val,0)+1
                prev=curr
                curr=curr.next
            else:
                prev.next=curr.next
                curr=prev.next
        return dummy.next