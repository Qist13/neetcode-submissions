# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            cur.val = stack.pop()
            cur = cur.next
        
        return head