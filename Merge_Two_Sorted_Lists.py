# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        def mergeList(first, second, merged):
        
            if first and second:

                if first.val <= second.val:
                    merged.next = first
                    first = first.next
                    merged.next.next = None

                else:
                    merged.next = second
                    second = second.next
                    merged.next.next = None

                return mergeList(first, second, merged.next)



            if first is None:
                merged.next = second
            if second is None:
                merged.next = first
            
            return merged.next


        head = ListNode(0)
        mergeList(l1, l2, head)
        return head.next






