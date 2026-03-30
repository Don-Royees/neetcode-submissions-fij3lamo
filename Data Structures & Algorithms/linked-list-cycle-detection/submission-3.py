# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = [] 
        while head:
            print(head.val)
            if head.next in temp:
                return True
            temp.append(head.next)
            head = head.next  
        return False    
        