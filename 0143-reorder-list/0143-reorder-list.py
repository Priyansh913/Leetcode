# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseLinkedList (self, head):
        prev = None
        current = head
        next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev

    def reorderList(self, head):
        current = head

        n = 0
        while current:
            n += 1
            current = current.next

        current = head

        for _ in range(int(n/2)):
            current = current.next

        node = current.next
        current.next = None

        rev_list = self.reverseLinkedList(node)
        
        next = None
        current = head

        while current and rev_list:
            next = current.next        # 2
            rev_next = rev_list.next   # 3
            current.next = rev_list    # 1.next = 4
            rev_list.next = next       # 4.next = 3

            rev_list = rev_next        # 
            current = next             #

        head = current