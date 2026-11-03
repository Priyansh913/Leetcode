# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        current = head
        count = 0

        while current:
            count += 1
            current = current.next

        posi = count - n

        if posi == 0:
            return head.next

        current = head

        for _ in range(posi - 1):
            current = current.next

        current.next = current.next.next

        return head