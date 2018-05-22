# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        first = second = head
        
        for i in range(n):
            second = second.next
        
        if not second:
            return head.next

        while second.next :
            first, second = first.next, second.next

        first.next = first.next.next

        return head
    


  
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print(Solution().removeNthFromEnd(head, 2))
