# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        
        if head==None:
            return None
        
        address_list=[]
        
        pointer=head
        
        while not pointer in address_list:
            address_list.append(pointer)
            
            if pointer.next==None:
                return None
            pointer=pointer.next
            
        return pointer
        
