# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val , next=None):
        self. val = val
        self.next= None
        


class MyLinkedList:

    def __init__(self):

        self.dummy = Node(0)
        # self.head= None
        self.length= 0
        self.tail= None


    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        else:
            i =0
            curr= self.dummy.next
            while i < index:
                curr=  curr.next
                i+=1
            return curr.val

    def addAtHead(self, val: int) -> None:
        head= self.dummy.next

        new_node= Node(val, None)

        self.dummy.next= new_node

        new_node.next= head
        
        self.length +=1

        if not self.tail:
            self.tail = new_node 

    def addAtTail(self, val: int) -> None:

        new_node= Node(val, None)
        if not self.tail:
            self.dummy.next= new_node
            self.tail= new_node
        else:
            self.tail.next= new_node
            self.tail= new_node
        self.length +=1

        # to avoid On add at tail we can have a self.tail at our linked list

        # new_node= Node(val, None)
        # curr= self.head
        # while curr.next:
        #     curr= curr.next   
        # curr.next= new_node

        # self.length+=1


    def addAtIndex(self, index: int, val: int) -> None:

        # dummy = Node(0, None)
        # dummy.next= self.head
        new_node= Node(val, None)

        if index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
        else:

            i=0
            curr= self.dummy
            while curr.next and i < index:
                curr= curr.next
                i+=1
            new_node.next= curr.next
            curr.next= new_node

            self.length +=1

    def deleteAtIndex(self, index: int) -> None:
        if self.length <=index:
            return 

        # dummy = Node(0, None)
        # dummy.next= self.head 
        i =0
        curr= self.dummy

        while i <index:
            curr= curr.next
            i+=1
        to_del = curr.next
        curr.next = to_del.next

        if not curr.next:
            self.tail= curr

        self.length -=1

        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
