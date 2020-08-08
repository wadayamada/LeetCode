# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head==None:
            return False
        
        else:
        
        
            pointer=head
            data=[]
        
        
        
            now=pointer
            while True:
            
                if now in data:
                    return True
            
                if pointer.next==None:
                    return False
            
                data.append(now)
                pointer=pointer.next
                now=pointer
