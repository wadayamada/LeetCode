# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head==None or head.next==None:
            return head
        
        pointer=head
        
        while True:
            
            if pointer==None:
                break
            
            if pointer.next==None:
                break
            
            if pointer.val==pointer.next.val:
                pointer.next=pointer.next.next
                continue
            
            else:
            
                pointer=pointer.next
                                                            
        return head
        
