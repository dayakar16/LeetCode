# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], reversedList = None) -> Optional[ListNode]:
        if not head: 
            return reversedList
        next = head.next 
        head.next = reversedList 
        return self.reverseList(next,hea)
