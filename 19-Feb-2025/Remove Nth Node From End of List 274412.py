# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        dummy=ListNode()
        dummy.next=head
        curr=dummy
        while curr.next:
            curr=curr.next
            length+=1
        index=length-n
        current=dummy
        i=0
        while current.next and i<index:
            current=current.next
            i+=1
        current.next=current.next.next
        return dummy.next