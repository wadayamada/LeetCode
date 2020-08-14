# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if head==None:
            return True
        
        pointer=head
        length_listnode=0
        list_listnode=[]
        
        while True:
            
            length_listnode+=1
            if pointer.next==None:
                break            
            pointer=pointer.next
                
        print(length_listnode)
        
        pointer=head
        
        for a in range(int(length_listnode/2)):
            list_listnode.append(pointer.val)    
            pointer=pointer.next
        
        list_listnode=reversed(list_listnode)
        
        if length_listnode%2==1:
            pointer=pointer.next
            
        for ll in list_listnode:
            if ll!=pointer.val:
                return False
            pointer=pointer.next
            
        return True
