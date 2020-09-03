# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head==None:
            return head
        if head.next==None:
            return head
        
        head_pre=ListNode()
        head_pre.next=head
        pointer_pre=head_pre
        pointer=head
        
        while True:
            
            if pointer.val==pointer.next.val:
                remove_num=pointer.val
            
                while True:
                    if pointer.val==remove_num:                        
                            pointer_pre.next=pointer.next
                            pointer=pointer.next
                            if pointer==None:
                                break                        
                    else:
                        break
                      
            else:
                pointer_pre=pointer
                pointer=pointer.next
            
            if pointer==None:
                break
            
            if pointer.next==None:
                break
                                
        return head_pre.next
