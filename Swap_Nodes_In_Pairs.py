'''mine'''
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        node.next = head

        temp = node

        while temp.next and temp.next.next:
        	node1 = temp.next
        	node2 = temp.next.next
        	temp.next = node1.next
        	node1.next = node2.next
        	node2.next = node1

        	temp = temp.next.next

        return node.next

'''learn from others'''      	
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(-1)
        prev.next = head
        temp = prev
        while temp.next and temp.next.next:
            node1 = temp.next  # A
            node2 = temp.next.next  # B
            temp.next = node2  # A->C
            node1.next = node2.next  # B->D
            node2.next = node1  # C->B?
            temp = temp.next.next  # 跳过两个
        return prev.next
