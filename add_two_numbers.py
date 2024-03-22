# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # Create the head of the ListNode()
        # Appoint a current to traverse
        head = ListNode()
        current = head
        carry = 0

        # While the list is not empty and their is not a carry
        while (l1 != None or l2 != None or carry == 1):
            
            
            l1_value = l1.val if l1 != None else 0
            l2_value = l2.val if l2 != None else 0
            total = l1_value + l2_value + carry
            current.next = ListNode(total % 10)
            carry = total // 10

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            current = current.next

        return head.next


        