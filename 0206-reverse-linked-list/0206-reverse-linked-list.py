class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def push (self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev = None
        current = head
        next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        head = prev

        return prev