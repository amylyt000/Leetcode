# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        pointer = head
        while pointer is not None and pointer.next is not None:
            while pointer.next.val == pointer.val: 
                if pointer.next.next != None:
                    pointer.next = pointer.next.next
                else:
                    pointer.next = None
                    break
            pointer = pointer.next
        return head
    

# class Solution:
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         p = head
#         while p != None:
#             while p.next != None and p.val == p.next.val :
#                 p.next = p.next.next
#             p = p.next
#         return head