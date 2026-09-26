# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        self.head = None

    def insert (self, data):
        new_node = ListNode(data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        count, middle = 0, 0
    
        while current:
            current = current.next
            count += 1

        if count % 2 == 0:
            middle = int(count / 2)
        else:
            middle = int(count / 2)

        current = head

        for _ in range(middle):
            current = current.next

        return current

if __name__ == "__main__":
    l = Solution()

    l.insert(1)   
    l.insert(2)       
    l.insert(3)  
    l.insert(4)  
    l.insert(5)  
    l.insert(6)

    result = l.middleNode(l.head)
    print(result.val)
