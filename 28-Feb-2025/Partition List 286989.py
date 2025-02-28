# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head=ListNode(0)
        greater_head=ListNode(0)
        less=less_head
        great=greater_head
        while head:
            if head.val<x:
                less.next=head
                less=less.next
            else:
                great.next=head
                great=great.next
            head=head.next
        great.next=None
        less.next=greater_head.next
        return less_head.next

        
    