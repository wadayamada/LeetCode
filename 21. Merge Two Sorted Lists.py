# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        first=l1
        second=l2
        count=0
                
        
        #print(l1.val,l1.next.val,l1.next.next.val)
        #a=l1.next.next.next
        #print(a==None)
        #pointer.val=1
        #print(pointer.val,pointer)
        #pointer.next=ListNode()
        #pointer=pointer.next
        #pointer.val=2
        #print(result_node,result_node.val,result_node.next)        
        result_node=None
        #result_node.val=None
                    
        while first!=None or second!=None:
            
            if count==0:                          
                result_node=ListNode()
                pointer=result_node
                count+=1
                
                if first==None:
                    #pointer.next=ListNode()
                    #pointer=pointer.next
                    pointer.val=second.val
                    second=second.next
                elif second==None:                
                    #pointer.next=ListNode()
                    #pointer=pointer.next
                    pointer.val=first.val
                    first=first.next
                
                elif first.val<second.val:                                                        
                    pointer.val=first.val
                    first=first.next
                    
                else:                                
                    pointer.val=second.val                
                    second=second.next
            
            
            elif first==None:
                pointer.next=ListNode()
                pointer=pointer.next
                pointer.val=second.val
                second=second.next
            elif second==None:                
                pointer.next=ListNode()
                pointer=pointer.next
                pointer.val=first.val
                first=first.next
            
            
            
            elif first.val<second.val:                
                pointer.next=ListNode()
                pointer=pointer.next
                pointer.val=first.val
                first=first.next
            else:                
                pointer.next=ListNode()
                pointer=pointer.next
                pointer.val=second.val
                second=second.next
            
            #pointer.val=None
            #print(pointer)
            
        #pointer_kari=result_node
        #while pointer_kari.next.val!=0:
            #pointer_kari=pointer_kari.next
            #print(pointer_kari)
        
        #pointer_kari.next=None
        #print(pointer.val,pointer.next)            
        #pointer.val=None
        #pointer=None
        
        if result_node==None:
            result_node=l1
        return result_node
