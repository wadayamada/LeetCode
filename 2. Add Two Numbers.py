# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result_node=ListNode()
        pointer_result=result_node
        pointer1=l1
        pointer2=l2
        
        while True:
            
            
            if pointer1.val+pointer2.val<10:                            
                pointer_result.val=pointer1.val+pointer2.val
                #print(pointer_result.val)
                inclement=0
            else:
                pointer_result.val=(pointer1.val+pointer2.val)%10
                #print(pointer_result.val)
                inclement=1
                
            
            
            if pointer1.next==None and pointer2.next==None and inclement==0:
                return result_node
            
            if pointer1.next==None:
                pointer1.next=ListNode()            
            if pointer2.next==None:
                pointer2.next=ListNode()
            
            pointer_result.next=ListNode()        
            pointer_result=pointer_result.next
            pointer1=pointer1.next
            pointer2=pointer2.next
            
            pointer1.val=pointer1.val+inclement
