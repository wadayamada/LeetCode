# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head==None:
            return head
        
        pointer=head        
        node_list=[]
        while True:        
            if pointer==None:
                break            
            node_list.append(pointer.val)            
            pointer=pointer.next
        
        result=ListNode()                      
        pointer=result
        pointer.val=3
           
        for n in range(len(node_list)):            
            pointer.val=node_list[(n+1)*-1]            
            if not n==len(node_list)-1:
                pointer.next=ListNode()            
                pointer=pointer.next        
            
        return result
